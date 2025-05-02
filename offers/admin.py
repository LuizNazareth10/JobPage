from django.contrib import admin
from .models import Offer

# Register your models here.
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'created_at', 'is_remote', 'salary', 'is_salary_visible')
    search_fields = ('title', 'company_name', 'description')
    list_filter = ('is_remote', 'experience_level', 'contract_type', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_editable = ('is_remote', 'salary', 'is_salary_visible')