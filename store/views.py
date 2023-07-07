from django.shortcuts import render, HttpResponse, redirect

from . models import Category, Product, Conf

from django.shortcuts import get_object_or_404

from django.contrib import messages

from django.core.mail import send_mail

import boto3

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string

from django.contrib.sites.shortcuts import get_current_site

import uuid
import random
import string
from datetime import datetime

def generate_confirmation_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(15))
    return code

def store(request):
 
    all_products = Product.objects.all()

    context = {'my_products':all_products}

    return render(request, 'store/store.html', context)



def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}



def list_category(request, category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)


    return render(request, 'store/list-category.html', {'category':category, 'products':products})


# @login_required(login_url='my-login')
def party_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)

    context = {'product': product}

    return render(request, 'store/partyinfo.html',context)


def result(request, pk):
    partyid = Product.objects.get(id=pk)
    if request.method == 'POST':
        user = request.user
        email = user.email
        user.vote_status = True
        partyid.vote += 1

        confirmation_code = generate_confirmation_code()
        context = {'confirmation_code':confirmation_code}

        user.save()
        partyid.save()



        current_site = get_current_site(request)
        current_datetime = datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        message = render_to_string('email-verification.html', {
                
            'user': user,
            'domain': current_site.domain,
            'date':current_date,
            'time': current_time,
            'confirmation_code':confirmation_code
        })

        send_mail('Submission confirmed: Nation Elections', message, 'your-email', [email])

        instance = Conf(confirmation_code=confirmation_code, votername=user.username)
        instance.save()


    return render(request, 'ballot-confirmation.html', context)


def results(request):
    
    all_products = Product.objects.all()

    context = {'my_products':all_products}

    return render(request, 'store/result.html', context)

def success(request):
    return render(request, 'success.html')

# Ballot
@login_required(login_url='my-login')
def ballot(request):

    all_parties = Product.objects.all()

    context = {'allParties':all_parties}

    return render(request, 'ballot.html', context)

# Ballot Review
def ballot_review(request, pk):
    partyid = Product.objects.get(id=pk)

    partyTitle = partyid.title

    partyImage = partyid.image

    partyid = partyid.id

    return render(request, 'ballot-review.html', {'pk':partyid,'title':partyTitle, 'image':partyImage})

# Confirmation Table
def table_conf(request):
     all_confs = Conf.objects.all()

     context = {'all_confs':all_confs}

     return render(request, 'table.html', context)

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #Sending the email
        subject = 'Quick Vote Contact Form'
        

        message = render_to_string('contact-form-email.html', {
                
            'user': name,
            'email': email,
            'subject': subject,
            'message': message
        })

        send_mail( subject, message, 'sender-your-email', ['receiver-email'])

        messages.success(request, "Your message has been successfully submited.")
        return redirect("contact")

    return render(request, 'contact.html')