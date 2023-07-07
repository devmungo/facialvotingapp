
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import CustomUser
from django import forms
from django.forms.widgets import PasswordInput, TextInput


# Registration form
class CompareFacesForm(forms.Form):
    image = forms.ImageField()

class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2','id_number']

    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        # Mark email as required

        self.fields['email'].required = True
        self.fields['id_number'].required = True


    # Email validation
    
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if CustomUser.objects.filter(email=email).exists():

            raise forms.ValidationError('This email is already exists')

        # len function updated ###

        if len(email) >= 350:

            raise forms.ValidationError("Your email is too long")


        return email
    
    def clean_id_number(self):

        id_number = self.cleaned_data.get("id_number")

        if CustomUser.objects.filter(id_number=id_number).exists():

            raise forms.ValidationError('This Id number already exists')

        return id_number


# Login form

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Update form

class UpdateUserForm(forms.ModelForm):

    password = None


    class Meta:

        model = CustomUser

        fields = ['username', 'email']
        exclude = ['password1', 'password1']
    

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        # Mark email as required

        self.fields['email'].required = True

        
    # Email validation
    
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():

            raise forms.ValidationError('This email is invalid')

        # len function updated ###

        if len(email) >= 350:

            raise forms.ValidationError("Your email is too long")


        return email
        
        
 
 

    