from django import forms
from classifieds.models import Category,Page

class CategoryForm(forms.ModelForm):
	name=forms.CharField(max_length=128,help_text="Please enter the category name")
	views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	likes=forms.IntegerField(widget=forms.HiddenInput(),initial=0)

	class Meta:   # An inline class to provide additional information on the form.
		model=Category    # Provide an association between the ModelForm and a model


class PageForm(forms.modelForm):
	title=forms.CharField(max_length=128,help_text="Please enter the title of the page")
	url=form.URLField(max_length=200,help_text="Please enter the URL of the page")
	views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)

	class Meta:
		model=Page


        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.

        fields=('title','url','views')
