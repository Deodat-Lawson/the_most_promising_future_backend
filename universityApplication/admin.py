from django.contrib import admin
from universityApplication.models import personalStatusForm


@admin.register(personalStatusForm)
class personalStatusFormAdmin(admin.ModelAdmin):
  list_display = ['id', 'fullName', 'locationOfResidence', 'citizenship',
                  'currentGradeLevel', 'currentSchoolSystem', 'GPA', 'SAT', 'ACT', 'honorsAndAwards',
                  'fieldsOfInterest', 'geographicPreferences', 'sizeOfUniversity', 'prestigeFactor', 'financialAid',
                  'EA', 'ED', 'RD', 'numberOfSchools']
  search_fields = ['id', 'fullName', 'locationOfResidence', 'citizenship',
                  'currentGradeLevel', 'currentSchoolSystem', 'GPA', 'SAT', 'ACT', 'honorsAndAwards',
                  'fieldsOfInterest', 'geographicPreferences', 'sizeOfUniversity', 'prestigeFactor', 'financialAid',
                  'EA', 'ED', 'RD', 'numberOfSchools']


# Register your models here.
