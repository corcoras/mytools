from django import forms
from .models import Product, CDP

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'featured'
        ]
        



class RawProductForm(forms.Form):
    title =       forms.CharField()
    description = forms.CharField()
    #interface_config = forms.CharField(widget=forms.Textarea(attrs={"rows": 40, "cols": 60}))
    price = forms.DecimalField()
    featured = forms.BooleanField()

class CDP_Form(forms.Form):
    cmf = forms.CharField()
    client_name = forms.CharField()
    device_name = forms.CharField()
    device_ip = forms.CharField()
    cdp_scrape = forms.CharField(widget=forms.Textarea(attrs={"rows": 40, "cols": 60}))
    interface_description = forms.CharField(widget=forms.Textarea(attrs={"rows": 40, "cols": 60}))

