import datetime
from django.utils.html import mark_safe
from django.db import models

class Family(models.Model):
    father = models.CharField(max_length=100)
    father_alive = models.BooleanField(default=True)
    father_phone = models.CharField(max_length=15, blank=True, null=True),
    father_email = models.EmailField(blank=True, null=True)
    father_occupation = models.CharField(max_length=100, blank=True, null=True),
    father_occupation_other = models.CharField(max_length=100, blank=True, null=True),

    mother = models.CharField(max_length=100)
    mother_alive = models.BooleanField(default=True)
    mother_phone = models.CharField(max_length=15, blank=True, null=True),
    mother_email = models.EmailField(blank=True, null=True)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True),
    mother_occupation_other = models.CharField(max_length=100, blank=True, null=True),

    location = models.CharField(max_length=100)
    dependent_children = models.IntegerField()
    religion = models.CharField(max_length=100, blank=True, null=True),

    class Meta:
        verbose_name = "Family"
        verbose_name_plural = "Families"

    def __str__(self):
        return self.father + " and " + self.mother

class Child(models.Model):
    name = models.CharField(max_length=100) 
    date_of_birth = models.DateField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name = "Child"
        verbose_name_plural = "Children"

    def __str__(self):
        return self.name

    @property
    def has_family(self):
        return self.family is not None

    @property
    def age(self):
        age = datetime.date.today() - self.date_of_birth
        return int(age.days/365.25)    

    def picture_tag(self):
        return mark_safe('<img src="{}" height="150" width="200"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'
    picture_tag.allow_tags = True