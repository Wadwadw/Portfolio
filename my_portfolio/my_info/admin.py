from django.contrib import admin
from .models import (
    MainInfoBlock,
    SkillsInfoBlock,
    LanguagesInfoBlock,
    ExperienceInfoBlock,
    EducationInfoBlock,
    CoursesInfoBlock,
)


admin.site.register(MainInfoBlock)
admin.site.register(SkillsInfoBlock)
admin.site.register(LanguagesInfoBlock)
admin.site.register(EducationInfoBlock)
admin.site.register(ExperienceInfoBlock)
admin.site.register(CoursesInfoBlock)
