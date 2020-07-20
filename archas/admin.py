from django.contrib import admin

from .models import *


admin.site.register(ArchitectureRealm) 
admin.site.register(ArchitectureCategory) 
admin.site.register(ArchitectureSubCategory) 

admin.site.register(AutomatedSystem)
admin.site.register(Interaction) 
