from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display  = ('name', 'company', 'phone', 'email', 'product', 'submitted_at', 'is_read')
    list_filter   = ('product', 'is_read', 'submitted_at')
    search_fields = ('name', 'company', 'email', 'phone')
    readonly_fields = ('submitted_at',)
    list_editable = ('is_read',)
    ordering      = ('-submitted_at',)
    date_hierarchy = 'submitted_at'
    list_per_page = 25

    fieldsets = (
        ('Contact Details', {
            'fields': ('name', 'company', 'phone', 'email')
        }),
        ('Enquiry', {
            'fields': ('product', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'submitted_at')
        }),
    )
