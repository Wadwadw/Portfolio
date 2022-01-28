from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class MainInfoBlock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    git_link = models.CharField(max_length=255)

    def __str__(self):
        return self.last_name


class SkillsInfoBlock(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)

    def __str__(self):
        return self.description


class LanguagesInfoBlock(models.Model):
    BEG = "Beginner"
    ELEM = "Elementary"
    INTER = "Intermediate"
    UPPER = "Upper intermediate"
    ADVANCED = "Advanced"
    LEVEL_CHOICES = (
        (BEG, "Beginner"),
        (ELEM, "Elementary"),
        (INTER, "Intermediate"),
        (UPPER, "Upper intermediate"),
        (ADVANCED, "Advanced"),
    )

    title = models.CharField(max_length=255)
    level_of_knowledge = models.CharField(
        max_length=255, default="Beginner", choices=LEVEL_CHOICES
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)

    def __str__(self):
        return self.title


class ExperienceInfoBlock(models.Model):
    title = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EducationInfoBlock(models.Model):
    name_of_school = models.CharField(max_length=255)
    name_of_specialities = models.CharField(max_length=255)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_specialities


class CoursesInfoBlock(models.Model):
    teacher = models.CharField(max_length=255)
    name_of_course = models.CharField(max_length=255)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_course
