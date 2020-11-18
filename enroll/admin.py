from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)
# class Useradmin(admin.ModelAdmin):
#     list_display = ('id','name','userName','email','phoneNumber','password','image','comment')


