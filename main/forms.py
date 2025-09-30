from django import forms
from .models import AppSetting

class AppSettingForm(forms.ModelForm):
    class Meta:
        model = AppSetting
        fields = ['file_path']
        widgets = {
            'file_path': forms.TextInput(attrs={'class': 'form-control'}),
        }