from django.forms import ModelForm
from recipes.models import Recipe

class RecipeForm(ModelForm):
#	email_address = forms.EmailField(max_length=300)

	class Meta:
		model = Recipe
		fields = (
			"title",
			"picture",
			"description",
		)
