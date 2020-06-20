from django.forms import ModelForm
from apps.newsletters.models import NewsLetters


class NewsLetterModelForm(ModelForm):
    class Meta:
        model = NewsLetters
        fields = ['email']