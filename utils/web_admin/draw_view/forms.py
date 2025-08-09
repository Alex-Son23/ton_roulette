from django import forms
from .models import GlobalPrompt

class GlobalPromptForm(forms.ModelForm):
    class Meta:
        model = GlobalPrompt
        fields = ["prompt_text"]
        widgets = {
            "prompt_text": forms.Textarea(attrs={"rows": 10, "cols": 100})
        }