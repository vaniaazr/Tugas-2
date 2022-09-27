from django import forms

class FormTask(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description", widget=forms.Textarea)