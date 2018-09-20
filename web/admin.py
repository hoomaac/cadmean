from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User,Post


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'is_active', 'is_admin', 'is_staff', 'password', 'avatar', 
        'joined_at')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'is_admin', 'is_staff')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('name','username')}),
        ('Permissions', {'fields': ('is_admin','is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
        ),
    )

    

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()



class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        fields = ('content', 'user')


    fieldsets = (
        ('Post', {'fields':('content', 'user',)}),
    )

    list_display = ('user', 'content', 'timestamp')
    search_fields = ('user__username',)
    odering = ('-timestamp',)

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)
