from django.db import models
from phonenumber_field.modelfields import PhoneNumberField as PhoneField
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class MuseumInfo(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    contact_mail = models.EmailField(null=True,blank=True)
    contact_phone = PhoneField(max_length=255,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    halls_number = models.PositiveSmallIntegerField(null=True,blank=True)
    def __str__(self) -> str:
                return self.name
    
@receiver(pre_save, sender=MuseumInfo)
def limit_website_instances(sender, instance, **kwargs):
    # Check the number of instances of the Website model
    website_info_count = MuseumInfo.objects.count()
    if website_info_count > 0 and not instance.pk:
        raise ValidationError('Information of the Website can be entered only once')    
        
    
class OpenningHour(models.Model):
    DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    )

    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK,null=True,blank=True)
    open_time = models.TimeField(null=True,blank=True)
    close_time = models.TimeField(null=True,blank=True)
    museum_info = models.ForeignKey('MuseumInfo',related_name= 'openinghours', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.day

class Event(models.Model): 
    name = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    event_about = models.TextField(null=True,blank=True)
    museum_info = models.ForeignKey('MuseumInfo',related_name= 'event', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Media(models.Model):
    media = models.ImageField(upload_to= 'images', blank= True, null=True)
    name = models.CharField(max_length=255, blank= True,null = True)
    museum_info = models.ForeignKey('MuseumInfo', on_delete=models.PROTECT,related_name= 'media')

    def __str__(self) -> str:
        return self.name

    


