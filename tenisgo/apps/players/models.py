from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)
    club = models.CharField(max_length=100)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def age(self):
        bday = self.birthdate
        today = timezone.now().date()

        one_or_zero = 0
        if (today.month, today.day) < (bday.month, bday.day):
            one_or_zero = 1

        year_difference = today.year - self.birthdate.year
        age = year_difference - one_or_zero

        return age
