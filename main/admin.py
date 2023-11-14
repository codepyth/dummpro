from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Registration, Dependent
from django.contrib.auth.models import User
class DependentInline(admin.TabularInline):
    model = Dependent
    extra = 1

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'occupation', 'passport_number', 'status', 'visa_status')
    search_fields = ('user__username', 'name', 'passport_number', 'visa_status')
    inlines = [DependentInline]

    # Custom admin actions
    actions = ['approve_registration', 'reject_registration', 'suspend_membership']

    def approve_registration(self, request, queryset):
        # Implement logic to approve registration
        # For example, you can update the status of selected registrations to 'APPROVED'
        queryset.update(status='APPROVED')

    def reject_registration(self, request, queryset):
        # Implement logic to reject registration
        # For example, you can update the status of selected registrations to 'REJECTED'
        queryset.update(status='REJECTED')

    def suspend_membership(self, request, queryset):
        # Implement logic to suspend membership
        # For example, you can update the status of selected registrations to 'SUSPENDED'
        queryset.update(status='SUSPENDED')

    # Define a custom filter for 'dependents'
    class HasDependentsListFilter(admin.SimpleListFilter):
        title = _('Has Dependents')
        parameter_name = 'has_dependents'

        def lookups(self, request, model_admin):
            return (
                ('yes', _('Yes')),
                ('no', _('No')),
            )

        def queryset(self, request, queryset):
            if self.value() == 'yes':
                return queryset.filter(dependents__isnull=False)
            if self.value() == 'no':
                return queryset.filter(dependents__isnull=True)
    def changelist_view(self, request, extra_context=None):
        approved_count = Registration.objects.filter(status='APPROVED').count()
        rejected_count = Registration.objects.filter(status='REJECTED').count()
        pending_count = Registration.objects.filter(status='PENDING').count()

        extra_context = {
            'approved_count': approved_count,
            'rejected_count': rejected_count,
            'pending_count': pending_count,
        }

        return super().changelist_view(request, extra_context=extra_context)
    list_filter = ('occupation', 'visa_status', 'status', HasDependentsListFilter)

# Register the models and admins
admin.site.register(Registration, RegistrationAdmin)
 # Unregister the User model to prevent accidental edits
