import datetime
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Addoption, Family, Child, VisitSchedule
# Register your models here.

admin.site.site_header = 'Hope And Homes For Children Dashboard'
admin.site.unregister(Group)

class FamilyAdmin(admin.ModelAdmin):
    list_display = ('father', 'mother', 'province','district','sector','cell','village','isibo', 'dependent_children', 'father_phone', 'mother_phone', 'father_email', 'mother_email', 'father_occupation', 'mother_occupation', 'father_occupation_other', 'mother_occupation_other', 'religion','ubudehe')
    list_filter = ('father', 'mother', 'province','district','sector','cell','village','isibo', 'dependent_children', 'father_alive', 'mother_alive')
    search_fields = ('father', 'mother', 'province','district','sector','cell','village','isibo', 'dependent_children')
    ordering = ('father', 'mother', 'province','district','sector','cell','village','isibo', 'dependent_children')
    


class HasFamilyFilter(admin.SimpleListFilter):
    title = _('Has Family')
    parameter_name = 'has_family'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(family__isnull=False)
        if self.value() == 'no':
            return queryset.filter(family__isnull=True)


class AgeFilter(admin.SimpleListFilter):
    title = _('Age')
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return (
            (0, 'less than 2 year'),  
            (1, '2 - 10 years'),
            (2, '10 - 18 years'),
            (3, '18 and above'),
        )

    def queryset(self, request, queryset):
        if self.value()== "0":
            return queryset.filter(date_of_birth__gte=datetime.date.today() - datetime.timedelta(days=365*2))
        elif self.value() == "1":
            return queryset.filter(date_of_birth__gte=datetime.date.today() - datetime.timedelta(days=365*10), date_of_birth__lte=datetime.date.today() - datetime.timedelta(days=365*2))

        elif self.value() == "2":
            return queryset.filter(date_of_birth__gte=datetime.date.today() - datetime.timedelta(days=365*18), date_of_birth__lte=datetime.date.today() - datetime.timedelta(days=365*10))

        elif self.value() == "3":
            return queryset.filter(date_of_birth__lte=datetime.date.today() - datetime.timedelta(days=365*18))        

class ChildAdmin(admin.ModelAdmin):
    list_display = ('names', 'age', 'family', 'picture_tag')
    search_fields = ('names', 'age', 'family')
    list_filter = (HasFamilyFilter, AgeFilter, 'names', 'family')

class AddoptionAdmin(admin.ModelAdmin):
    list_display = ('child', 'family', 'addoption_status', 'approved', 'confirmed')
    list_filter = ('child', 'family', 'status', 'approved')
    search_fields = ('child', 'family', 'status', 'approved')
    ordering = ('child', 'family', 'status', 'approved')

    def addoption_status(self, obj):
        colors = {
            'Pending': '#9C9206',
            'Approved': 'green',
            'Rejected': 'red',
        }
        # get status from enum as whole word
        status = obj.get_status_display()
        return format_html(
            '<span style="color: {};">{}</span>',
            colors[status],
            status,
        )
    def has_module_permission(self, request) -> bool:
        if request.user.is_staff or request.user.is_superuser:
            return True
        return False

    
    
    # confirm addoption only visible for users not superuser
    # add confirm_addoption action
    actions = ['confirm_addoption','approve_addoption',]

    def confirm_addoption(self, request, queryset):
        queryset.update(confirmed=True)

    def approve_addoption(self, request, queryset):
        queryset.update(approved=True)
        queryset.update(status='Approved')

    def has_add_permission(self, request) -> bool:
        if not request.user.is_superuser:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        # if user is not superuser return False
        if not request.user.is_superuser:
            return False
        return True

    def has_change_permission(self, request, obj=None):
        # if user is not superuser return False
        if not request.user.is_superuser:
            return False
        else:
            return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        print(actions)
        if request.user.is_superuser:
            del actions['confirm_addoption']
            return actions
        del actions['approve_addoption']
        return actions

class VisitScheduleAdmin(admin.ModelAdmin):
    list_display = ('child', 'family', 'date', 'time')
    list_filter = ('child', 'family', 'date', 'time')
    search_fields = ('child', 'family', 'date', 'time')
    ordering = ('child', 'family', 'date', 'time')

admin.site.register(Family, FamilyAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Addoption, AddoptionAdmin)
admin.site.register(VisitSchedule, VisitScheduleAdmin)