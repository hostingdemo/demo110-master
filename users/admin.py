from django.contrib import admin
from .models import Student, Documents, ParentDetails, AdditionalDetails, ContactDetails,Profile

admin.site.register(Student)
admin.site.register(Documents)
admin.site.register(ParentDetails)
admin.site.register(AdditionalDetails)
admin.site.register(ContactDetails)
admin.site.register(Profile)