from django import forms

STATES = (('', 'Choose'), ('MP','Madhya Pradesh'), ('MH', 'Maharashtra'), ('GO', 'Goa'))

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address1 = forms.CharField(label = 'Address', widget=forms.TextInput( attrs={'placeholder': '123 Om Building'}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='zip')
    check_me_out = forms.BooleanField(required=False)


