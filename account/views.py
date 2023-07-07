from django.shortcuts import redirect, render
from .forms import RegistrationForm, LoginForm, UpdateUserForm, CustomUser
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from . token import user_tokenizer_generate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
import boto3
import base64
from django.http import JsonResponse
import botocore.exceptions
import re
import requests

#AWS Credentials
aws_access_key_id = ''
aws_secret_access_key = ''
aws_region_name = ''

# Configure Boto3 with the environment variables
boto3.setup_default_session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region_name
)

def register(request):

    form = RegistrationForm()

    if request.method == 'POST':

        id_number = request.POST.get('id_number')
        email = request.POST.get('email')
       
        name =  request.POST.get('username')
        image_data = request.POST.get('image', '')

        # Connect to Amazon Rekognition
        rekognition = boto3.client('rekognition', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')

        try:

            TABLE_NAME = 'TABLE-NAME'

            client = boto3.client('rekognition', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')
            
            response = client.search_faces_by_image(
            CollectionId='COLLECTION-ID',
            Image={
                'Bytes': base64.b64decode(image_data)
            }
            )

            face_matches = response['FaceMatches']

            if face_matches:

                for match in face_matches:

                    face = match['Face']

                    query_result = dynamodb.get_item(
                        TableName=TABLE_NAME,  
                        Key={'faceid': {'S': face['FaceId']}}
                        )
                    
                    if 'Item' in query_result:

                        db_idnumber = query_result['Item']['idnumber']['S']
                        if db_idnumber != id_number:
                            messages.error(request, "The picture you have provided does not match with the id number registered in the DynamoDB database")
                            return redirect("register")
                        else:
                            
                            #Phase 2 Indexing
                            response = rekognition.index_faces(
                            CollectionId='COLLECTION-ID',
                            Image={
                                'Bytes': base64.b64decode(image_data)
                            },
                            ExternalImageId=name
                            )
                            
                            face_records = response['FaceRecords']

                            if len(face_records) == 0:
                                messages.error(request, "No faces were detected in the image captured.")
                                return redirect("my-login")
                            else:
                            # Check if the face was successfully registered
                            # Face registered successfully
                            # ... save user information to the database
                                form = RegistrationForm(request.POST)
                                if form.is_valid():
                                    user = form.save() #save data to the database
                                    user.is_active = False
                                    user.save()
                                
                                    #Email verification setup (template)

                                    current_site = get_current_site(request)

                                    subject = 'Account verification email'

                                    message = render_to_string('account/registration/email-verification.html', {
                                        'user': user,
                                        'domain': current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        'token': user_tokenizer_generate.make_token(user),
                                    
                                    })
                                    print("Managed to get here- this is the second stop")
                                    send_mail( subject, message, 'YOUR-EMAIL', [email])

                                    return redirect('email-verification-sent')
                    
            else:
                messages.error(request, "Your face is not in database image collection")
                return redirect("register")

        # return JsonResponse(response)

        except Exception as e:
            messages.error(request, "The are no faces detected in the picture.")
            return redirect("register")
        
    context = {'form': form}

    return render(request, 'account/registration/register.html', context=context)


def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        image_data = request.POST.get('image', '')

        # Get the uploaded image file from the request

        # Initialize the Rekognition client
        client = boto3.client('rekognition', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')

        try:
            response = client.search_faces_by_image(
                CollectionId='COLLECTION-ID',
                Image={
                    'Bytes': base64.b64decode(image_data)
                }
            )

            # Check if there are any matched faces
            face_matches = response['FaceMatches']
            if len(face_matches) == 0:
                messages.error(request, "Your face was not found in the collection.")
                return redirect("my-login")
            else:
                form = LoginForm(request, data=request.POST)
                context = {'form':form}
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'account/dashboard.html', {'error': 'You have logged in.'})
                else:
                    return render(request, 'account/my-login.html',context=context)
        
        except botocore.exceptions.ParamValidationError as e:
            error_message = e.response['Error']['Message']
            if 'There are no faces in the image' in error_message:
                messages.error(request, "No faces found in the image")
                return render(request, 'capture_image.html')
            else:
                return JsonResponse({'error': error_message})
        except Exception as e:
             messages.error(request, "No faces were detected in the image captured.")
        
    context = {'form':form}

    return render(request, 'account/my-login.html', context=context)

 
    
def email_verification(request, uidb64, token):

    # uniqueid

    unique_id = force_str(urlsafe_base64_decode(uidb64))

    user = CustomUser.objects.get(pk=unique_id)
    
    # Success

    if user and user_tokenizer_generate.check_token(user, token):

        user.is_active = True

        user.save()

        return redirect('email-verification-success')


    # Failed 

    else:

        return redirect('email-verification-failed')


def email_verification_sent(request):

    return render(request, 'account/registration/email-verification-sent.html')


def email_verification_success(request):

    return render(request, 'account/registration/email-verification-success.html')



def email_verification_failed(request):

    return render(request, 'account/registration/email-verification-failed.html')


# logout
def user_logout(request):

    try:

        for key in list(request.session.keys()):

            if key == 'session_key':

                continue

            else:

                del request.session[key]


    except KeyError:

        pass

    
    messages.success(request, "Logout success")
    return redirect("store")


#Dashboard
@login_required(login_url='my-login')
def dashboard(request):


    return render(request, 'account/dashboard.html')


#Profile page
@login_required(login_url='my-login')
def profile_management(request):    

    # Updating our user's username and email

    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':

        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():

            user_form.save()

            messages.info(request, "Update success!")

            return redirect('dashboard')

   

    context = {'user_form':user_form}

    return render(request, 'account/profile-management.html', context=context)
    

#Delete Account
@login_required(login_url='my-login')
def delete_account(request):

    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':

        user.delete()


        messages.error(request, "Account deleted")


        return redirect('store')


    return render(request, 'account/delete-account.html')

 











