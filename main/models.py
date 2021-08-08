from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class House(models.Model):
    name = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Se crea un campo virtual "wizards" con la lista de magos.

class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.ForeignKey(House, related_name="wizards", on_delete = models.CASCADE)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()

    def __repr__(self) -> str:
        return f'{self.id}: {self.name}'

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)