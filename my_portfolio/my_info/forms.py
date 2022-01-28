from .models import (
    MainInfoBlock,
    SkillsInfoBlock,
    LanguagesInfoBlock,
    ExperienceInfoBlock,
    EducationInfoBlock,
    CoursesInfoBlock,
)
from django import forms


class MainInfoForm(forms.ModelForm):
    class Meta:
        model = MainInfoBlock
        fields = (
            "name",
            "last_name",
            "age",
            "position",
            "location",
            "git_link",
            "email",
            "user",
        )


class SkillInfoForm(forms.ModelForm):
    class Meta:
        model = SkillsInfoBlock
        fields = ("description",)


class LanguageInfoForm(forms.ModelForm):
    class Meta:
        model = LanguagesInfoBlock
        fields = ("title", "level_of_knowledge")


class ExperienceInfoForm(forms.ModelForm):
    class Meta:
        model = ExperienceInfoBlock
        fields = ("title", "date_from", "date_to", "responsibilities")


class EducationInfoForm(forms.ModelForm):
    class Meta:
        model = EducationInfoBlock
        fields = ("name_of_school", "name_of_specialities", "date_from", "date_to")


class CourseInfoForm(forms.ModelForm):
    class Meta:
        model = CoursesInfoBlock
        fields = ("teacher", "name_of_course", "date")
