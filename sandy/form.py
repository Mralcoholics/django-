from django.forms import ModelForm
from .models import Doctor
class medicallist(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'