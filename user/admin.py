from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
from .forms import UpdateUserForm, CustomUserCreationForm

UserModel = get_user_model()


class CustomerProxy(UserModel):
    class Meta:
        proxy = True
        verbose_name = "customer"
        verbose_name_plural = "customers"


@admin.register(CustomerProxy)
class CustomerAdmin(BaseUserAdmin):
    ordering = ("-id",)
    list_display = ("mobile_number", "is_active", "is_staff", "is_superuser")
    form = UpdateUserForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (
            "General Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "mobile_number",
                    "password",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "General Info",
            {"fields": (("first_name",), "last_name", "mobile_number")},
        ),
        ("Password Setting", {"fields": ((("password1")),)}),
    )

    def get_queryset(self, request):
        queryset = super(CustomerAdmin, self).get_queryset(request)
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        return queryset.filter(
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )


class SuperUserProxy(UserModel):
    class Meta:
        proxy = True
        verbose_name = "super admin"
        verbose_name_plural = "super admins"


@admin.register(SuperUserProxy)
class SuperUserAdmin(BaseUserAdmin):
    ordering = ("-id",)
    search_fields = ["mobile_number", "first_name", "last_name"]
    list_filter = []
    list_display = ("mobile_number", "is_active", "is_staff", "is_superuser")
    list_display_links = ("mobile_number", "is_active", "is_staff", "is_superuser")
    form = UpdateUserForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (
            "General Info",
            {
                "fields": (
                    ("first_name",),
                    "last_name",
                    "mobile_number",
                    "password",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            "General Info",
            {"fields": (("first_name",), "last_name", "mobile_number")},
        ),
        ("Password Setting", {"fields": ((("password1")),)}),
    )

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        super(SuperUserAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super(SuperUserAdmin, self).get_queryset(request)
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        return queryset.filter(
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )


class StaffUserProxy(UserModel):
    class Meta:
        proxy = True
        verbose_name = "staff"
        verbose_name_plural = "staffs"


@admin.register(StaffUserProxy)
class StaffUserAdmin(BaseUserAdmin):
    ordering = ("-id",)
    search_fields = ["mobile_number", "first_name", "last_name"]
    list_filter = []
    list_display = ("mobile_number", "is_active", "is_staff", "is_superuser")
    list_display_links = ("mobile_number", "is_active", "is_staff", "is_superuser")
    form = UpdateUserForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (
            "General Info",
            {
                "fields": (
                    ("first_name",),
                    "last_name",
                    "mobile_number",
                    "password",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            "General Info",
            {"fields": (("first_name",), "last_name", "mobile_number")},
        ),
        ("Password Setting", {"fields": ((("password1")),)}),
    )

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        super(StaffUserAdmin, self).save_model(request, obj, form, change)
        try:
            staff_group = Group.objects.get(name="staff")
            obj.groups.add(staff_group)
        except ObjectDoesNotExist:
            pass

    def get_queryset(self, request):
        queryset = super(StaffUserAdmin, self).get_queryset(request)
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        return queryset.filter(
            is_superuser=False,
            is_staff=True,
            is_active=True,
        )

    def has_change_permission(self, request, obj=None):
        base_change_permission = super(StaffUserAdmin, self).has_change_permission(request, obj=None)
        if base_change_permission:
            if bool(request.user == obj or request.user.is_superuser):
                return True
        return False
