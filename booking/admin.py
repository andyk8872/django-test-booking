from django.contrib import admin
from .models import Booking

# Register your models here.
# admin.site.register(models.Booking)


@admin.register(Booking)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_guests', 'creation_date', 'timeslot')
    list_filter = ('date_until', 'creation_date')
    search_fields = ('user', 'email')
