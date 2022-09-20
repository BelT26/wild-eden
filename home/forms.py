from django import forms

# Create your forms here.


class ContactForm(forms.Form):
    """
    A form for customers to submit enquiries
    """
    full_name = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
