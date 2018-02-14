from django.db import models
from django.utils import timezone


class Student(models.Model):
    
    title = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    fathers_name = models.CharField(max_length=40, null=True)
    mothers_name = models.CharField(max_length=40, null=True)
    nationality = models.CharField(max_length=40, null=True)
    email_address = models.CharField(max_length=40, null=True)
    emip_marks = models.BigIntegerField(default=None)
    emip_grade = models.CharField(max_length=3, null=True)
    emwe_marks = models.BigIntegerField(default=None, null=True)
    emwe_grade = models.CharField(max_length=3, null=True)
    esas_marks = models.BigIntegerField(default=None)
    esas_grade = models.CharField(max_length=3, null=True)
    eict_marks = models.BigIntegerField(default=None)
    eict_grade = models.CharField(max_length=3, null=True)
    eemp_marks = models.IntegerField(default=0)
    eemp_grade = models.CharField(max_length=3, null=True)
    emmp_marks = models.IntegerField(default=0)
    emmp_grade = models.CharField(max_length=3, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:index3',kwargs-{'pk': self.pk})

    def __str__(self):
        return self.title
