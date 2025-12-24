from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUSerCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'full_name', 'gender', 'birth_date', 'password1', 'password2']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }
        
class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget = forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

class CustomSignupForm(SignupForm):
    full_name = forms.CharField(max_length=100, label="Full name")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=(('male', 'Male'), ('female', 'Female')))

    def save(self, request):
        user = super().save(request)
        user.full_name = self.cleaned_data['full_name']
        user.birth_date = self.cleaned_data['birth_date']
        user.gender = self.cleaned_data['gender']
        user.save()
        return user