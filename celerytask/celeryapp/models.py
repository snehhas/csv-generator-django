from django.db import models

# Create your models here.
class Details(models.Model):
    id=models.BigAutoField(primary_key=True)
    filename=models.CharField(max_length=150)
    count=models.IntegerField()
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.filename

