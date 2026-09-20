from django.contrib import admin
from .models import College, Principal, Subject, Teacher

# Register your models here.
admin.site.register(College)
admin.site.register(Principal)
admin.site.register(Subject)
admin.site.register(Teacher)