from django.contrib import admin
from .models import Postmodels
from .models import messagebox



# Register your models here.
class PostMoldeAdmin(admin.ModelAdmin):
    list_display = ('title','date_created')

admin.site.register(Postmodels,PostMoldeAdmin)
admin.site.register(messagebox)



