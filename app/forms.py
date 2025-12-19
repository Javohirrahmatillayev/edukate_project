from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    full_name = forms.CharField(max_length=100, label="To'liq ism")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.save()
        return user
