from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Film(BaseModel):
    title = models.CharField(max_length=200, null=False)
    language_id = models.IntegerField(null=False)
    release_year = models.IntegerField()


class Category(BaseModel):
    name = models.CharField(max_length=200)


class Customer(BaseModel):
    name = models.CharField(max_length=200)
    age = models.IntegerField()


class Actor(BaseModel):
    name = models.CharField(max_length=200)
