from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from .models import Student

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created and instance.role == 'student':
        Student.objects.create(
            user=instance,
            register_number=f"REG{instance.id}",
            department="Not Assigned",
            year=1,
            family_income=0,
            distance_km=0,
        )
