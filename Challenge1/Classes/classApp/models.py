from django.db import models

class UniversityClasses(models.Model):
    title = models.CharField(max_length=100)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=100)
    duration = models.FloatField()

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "University Classes"

    def __str__(self):
        return f"{self.title} - {self.instructor_name}"


# Create your models here.
