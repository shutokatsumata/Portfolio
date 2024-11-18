from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.

class ContactView (FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = '{}'.format(title)
        message = (
            '送信者:{0}\nメールアドレス:{1}\n件名:{2}\nお問い合わせ内容:\n{3}'
            .format(name, email, title, message)
        )

        form_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list
        )

        message.send()

        message.success(
            self.request, 'お問い合わせは正常に送信されました。')
        
        return super().form_valid(form)