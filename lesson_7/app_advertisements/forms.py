from django import forms
from django.forms import ModelForm, modelformset_factory
from .models import Advertisement
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}))
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Ваш заголовок не может начинаться с вопросительного знака (?), поэтому ваша форма была отклонена')
            
        else:
            return title        
            