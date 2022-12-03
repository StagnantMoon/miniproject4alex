from django.db import models


# Create your models here. - Forum Idea

class forums(models.Model):
    name = models.CharField(max_length=200, default="anon")
    topic = models.CharField(max_length=200, null=True)  # Had to add
    description = models.CharField(max_length=1000, black=True)

    def __str__(self):
        return str(self.topic)


# Discussion Model


class discussions(models.Model):
    forums = models.ForeignKey(forums, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forums)
