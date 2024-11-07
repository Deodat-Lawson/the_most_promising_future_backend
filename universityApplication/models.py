from django.db import models

# Create your models here.

class personalStatusForm(models.Model):
  fullName = models.CharField(max_length=100)
  currentGradeLevel = models.CharField(max_length=100)
  locationOfResidence = models.CharField(max_length=100)
  citizenship = models.CharField(max_length=100)

  currentSchoolSystem = models.CharField(max_length=100)
  GPA = models.CharField(max_length=10)
  SAT = models.CharField(max_length=10)
  ACT = models.CharField(max_length=10)

  honorsAndAwards = models.CharField(max_length=1000)

  fieldsOfInterest = models.CharField(max_length=100)
  geographicPreferences = models.CharField(max_length=100)
  sizeOfUniversity = models.CharField(max_length=100)
  prestigeFactor = models.FloatField()

  financialAid = models.BooleanField()

  EA = models.BooleanField()
  ED = models.BooleanField()
  RD = models.BooleanField()
  numberOfSchools = models.CharField(max_length=100)


  def __str__(self):
    return self.name

