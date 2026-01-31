from django.contrib import admin
from .models import Post
from .models import Product

admin.site.register(Product)
admin.site.register(Post)
