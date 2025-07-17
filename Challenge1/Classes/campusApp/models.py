from django.db import models

# UniversityCampus model represents a college campus
class UniversityCampus(models.Model):
    # Name of the campus (e.g., Main Campus)
    campus_name = models.CharField(max_length=100)

    # Two-letter state abbreviation (e.g., NY, CA)
    state = models.CharField(max_length=2)

    # Unique campus ID number
    campus_id = models.IntegerField()

    # Default model manager
    objects = models.Manager()

    # Meta class allows customization of model display
    class Meta:
        verbose_name_plural = "University Campus"

    # String representation in the admin interface
    def __str__(self):
        return f"{self.campus_name} ({self.state})"
