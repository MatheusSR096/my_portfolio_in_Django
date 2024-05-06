from django.db import models

class Intro(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    
    def __str__(self):
        return self.title

class Links(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    
    def __str__(self):
        return self.title

class Resume(models.Model):
    prof_exp = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    certifications = models.TextField()
    
    def __str__(self):
        return f"Resume #{self.id}"

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name