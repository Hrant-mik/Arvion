# main/migrations/0002_populate_initial_data.py
from django.db import migrations

BLOOD_GROUPS = [
    "O(I) Rh+", "O(I) Rh-", "A(II) Rh+", "A(II) Rh-",
    "B(III) Rh+", "B(III) Rh-", "AB(IV) Rh+", "AB(IV) Rh-",
]
GENDERS = ["Արական", "Իգական", "Այլ"]

def populate_data(apps, schema_editor):
    BloodGroup = apps.get_model('main', 'BloodGroup')
    for group_name in BLOOD_GROUPS:
        BloodGroup.objects.get_or_create(group_name=group_name)
    
    Gender = apps.get_model('main', 'Gender')
    for gender_name in GENDERS:
        Gender.objects.get_or_create(name=gender_name)

def remove_data(apps, schema_editor):
    BloodGroup = apps.get_model('main', 'BloodGroup')
    BloodGroup.objects.filter(group_name__in=BLOOD_GROUPS).delete()
    
    Gender = apps.get_model('main', 'Gender')
    Gender.objects.filter(name__in=GENDERS).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(populate_data, remove_data),
    ]