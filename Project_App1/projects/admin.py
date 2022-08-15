from django.contrib import admin

# Register your models here.
from .models import Project,Review,Tag,Contactus

# hey get these models and show in the damin panel here

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Contactus)