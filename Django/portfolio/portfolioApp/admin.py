from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contributer)
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(ContributerTechnology)
admin.site.register(ContributorProjectContribution)
