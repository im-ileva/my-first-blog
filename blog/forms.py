from django import forms
from .models import Product
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'image',)
