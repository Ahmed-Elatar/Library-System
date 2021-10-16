from django.db import models

# Create your models here.

class books(models.Model):
    title = models.CharField(max_length=20)
    image = models.CharField(max_length=1000)
    description = models.CharField(max_length=200)
    cat = models.CharField(max_length=20)
    # whoborrowed=models.CharField(max_length=20, null=True,default='')
    bookuser=models.CharField(max_length=20)
    status = models.CharField(
        max_length=10,
        choices=[
            ('Available','available'),
            ('Borrowed','borrowed')

        ]



    )

    def __str__(self):
        return self.title

