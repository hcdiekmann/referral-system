from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Referral(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='referrals')
    referral_date = models.DateField()
    referrer_name = models.CharField(max_length=100)
    referral_reason = models.TextField()
    note = models.TextField()
    document = models.FileField(upload_to='referral_documents/', null=True, blank=True)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} on {self.referral_date}"