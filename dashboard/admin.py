import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Family, Child
# Register your models here.

class FamilyAdmin(admin.ModelAdmin):
    # list_display = ('father', 'mother', 'location', 'dependent_children')
    # list_filter = ('father', 'mother', 'location', 'dependent_children')
    # search_fields = ('father', 'mother', 'location', 'dependent_children')
    # ordering = ('father', 'mother', 'location', 'dependent_children')

    # # fieldsets = (
    # #     (None, {
    # #         'fields': ('father', 'father_alive', 'father_phone', 'father_email', 'father_occupation', 'father_occupation_other', 'mother', 'mother_alive', 'mother_phone', 'mother_email', 'mother_occupation', 'mother_occupation_other', 'location', 'dependent_children', 'religion', 'income')
    # #     }),
    # # )

    # # add_fieldsets = (
    # #     (None, {
    # #         'classes': ('wide',),
    # #         'fields': ('father', 'father_alive', 'father_phone', 'father_email', 'father_occupation', 'father_occupation_other', 'mother', 'mother_alive', 'mother_phone', 'mother_email', 'mother_occupation', 'mother_occupation_other', 'location', 'dependent_children', 'religion', 'income')
    # #     }),
    # # )
    pass



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
    list_display = ('name', 'age', 'family', 'picture_tag')
    search_fields = ('name', 'age', 'family')
    list_filter = (HasFamilyFilter, AgeFilter, 'name', 'family')

    

admin.site.register(Family, FamilyAdmin)
admin.site.register(Child, ChildAdmin)