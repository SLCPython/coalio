#encoding: utf-8

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from profiles.models import CoalioUser

class CoalioUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the
       required fields, plus a repeated password.
    """
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)

    class Meta:
        model = CoalioUser
        fields = ("email", "first_name", "last_name", "role")

    def clean_password2(self):
        # Check that the two password entries match.
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = "Passwords don't match"
            raise forms.ValidationError(msg)
        return password2

    def save(self, commit=True):
        # Save the password in hashed format
        user = super(CoalioUserCreationForm, 
                        self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CoalioUserChangeForm(forms.ModelForm):
    """ A form for updating users. Includes all the fields
    on the user, but replaces the password field with
    admin's password hash display field.
    """
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = CoalioUser
    def clean_password(self):
        # Regardless of what the user provides, return the
        # initial value. This is done here, rather than on
        # the field, because the field does not have access
        # to the initial value
        return self.initial["password"]


class CoalioUserAdmin(UserAdmin):
    # Set the add/modify forms
    add_form = CoalioUserCreationForm
    form = CoalioUserChangeForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("email", "is_staff", "role", "first_name", "last_name")
    list_filter = ("role",
                    "is_staff", "is_superuser",
                    "is_active", "groups")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields":
                ("first_name",
                "last_name")}),
        ("Permissions", {"fields": (
                "role",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email",
                "password1", "password2")}
        ),
    )

# Register the new CoalioUserAdmin
admin.site.register(CoalioUser, CoalioUserAdmin)
