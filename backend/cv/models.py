from django.db import models
from django.contrib.auth.models import User

class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    template = models.CharField(max_length=50, default='modern')
    
    # Informations personnelles
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    # Résumé professionnel
    summary = models.TextField(blank=True)

class Experience(models.Model):
    cv = models.ForeignKey(CV, related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

class Education(models.Model):
    cv = models.ForeignKey(CV, related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Skill(models.Model):
    cv = models.ForeignKey(CV, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    level = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
