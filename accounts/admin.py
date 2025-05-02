from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'profile_picture')}),
        (_('Address'), {'fields': ('country', 'state', 'city', 'address_line', 'zip_code')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Account type'), {'fields': ('role',)}),
        (_('Recruiter data'), {'fields': ('company_name', 'company_website', 'company_description')}),
        (_('Candidate data'), {'fields': ('linkedin_url',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email','username')

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)