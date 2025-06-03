from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['popis', 'rating']
        labels = {
            'popis': 'Vaše hodnocení',
            'rating': 'Počet hvězdiček (1-5)'
        }
        widgets = {
            'popis': forms.Textarea(attrs={'rows': 5}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }
