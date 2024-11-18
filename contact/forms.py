from django import forms

class ContactForm(forms.Form):
    name = forms.CharField (label='お名前')
    email = forms.EmailField (label='メールアドレス')
    title = forms.CharField (label='件名')
    message = forms.CharField (label='お問い合わせ内容')