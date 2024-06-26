from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
   email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
   first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first Name'}))
   last_name = forms.CharField(label="", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last Name'}))


   class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

   def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)

      self.fields['username'].widget.attrs['class'] = 'form-control'
      self.fields['username'].widget.attrs['placeholder'] = 'User Name'
      self.fields['username'].widget.label = ''
      self.fields['username'].help_text = '<small>enter user name 8 charater and number</small>'

      self.fields['password1'].widget.attrs['class'] = 'form-control'
      self.fields['password1'].widget.attrs['placeholder'] = 'Pass Word'
      self.fields['password1'].widget.label = ''
      self.fields['password1'].help_text = '<small>enter complex password for safe login</small>'

      self.fields['password2'].widget.attrs['class'] = 'form-control'
      self.fields['password2'].widget.attrs['placeholder'] = 'Pass Word Confrim'
      self.fields['password2'].widget.label = ''
      self.fields['password2'].help_text = '<small>reenter password</small>'


class AddRecordForm(forms.ModelForm):
   first_name = forms.CharField(required=True, label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first Name'}))
   last_name = forms.CharField(required=True, label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last Name'}))
   address =  forms.CharField(required=True, label="", max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address Name'}))
   city =  forms.CharField(required=True, label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
   zipcode =  forms.CharField(required=True, label="", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZipCode'}))
   email =  forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
   phone =  forms.CharField(required=True, label="", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))

   class Meta:
      model = Record
      exclude = ("user",)
