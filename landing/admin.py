from django.contrib import admin
from .models import *
# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Subscriber._meta.fields]
#     fields = ["email"]
    list_filter = ["name", "email"]
    search_fields = ["name", "email"]
    # exclude = ["email"]


    class Meta:
        model = Subscriber
admin.site.register(Subscriber, SubscriberAdmin)
