'''
create a signal to send email when an addoption is approved
'''
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from dashboard.models import Addoption, VisitSchedule

@receiver(post_save, sender=Addoption)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Hope and Home Addoption',
            'Your addoption has been received and is being processed',
            settings.EMAIL_HOST_USER,
            [instance.family.mother_email, instance.family.father_email],
            fail_silently=False,
        )

    if(instance.status == 'Approved'):
        instance.approved = True
        instance.save()

    if instance.approved:
        instance.status = 'approved'

        send_mail(
            'Hope and Home Addoption',
            'Your addoption has been approved',
            settings.EMAIL_HOST_USER,
            [instance.family.mother_email, instance.family.father_email],
            fail_silently=False,
        )
    else:
        print("not sending email")


# signal to send email to the parents when a schedule was created
@receiver(post_save, sender=VisitSchedule)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Hope and Home Addoption',
            f"A visit schedule has been created for you for the child '{instance.child}' you requested to addopt adopted \non {instance.date} at {instance.time}",
            settings.EMAIL_HOST_USER,
            [instance.family.mother_email, instance.family.father_email],
            fail_silently=False,
        )