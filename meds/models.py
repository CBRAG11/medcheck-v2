from django.db import models


class Med(models.Model):
    med_name = models.CharField(max_length=255)
    avg_dosage = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.med_name

class User(models.Model):
    user_name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    allergies = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name