from django.contrib import admin
from . models import Jobs, CompanyProfile, Students



# Register your models here.
# from . import models
# # Register your models here.

admin.site.register(Jobs)
admin.site.register(CompanyProfile)
admin.site.register(Students)
# admin.site.register(CustomUser)