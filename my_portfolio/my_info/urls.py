from django.urls import path
from .views import (
    main,
    MainInfoUpdate,
    SkillsInfoUpdate,
    LanguageInfoUpdate,
    EducationInfoUpdate,
    ExperienceInfoUpdate,
    CoursesInfoUpdate,
    UserListView,
    MainInfoCreate,
    SkillsInfoCreate,
    SkillInfoDelete,
    LanguageInfoCreate,
    LanguageInfoDelete,
    EducationInfoCreate,
    EducationInfoDelete,
    ExperienceInfoCreate,
    ExperienceInfoDelete,
    CourseInfoCreate,
    CourseInfoDelete,
)


app_name = "my_info"


urlpatterns = [
    path("<int:pk>/", main, name="main"),
    path("update_main/<int:pk>/", MainInfoUpdate.as_view(), name="update_main"),
    path("update_skills/<int:pk>/", SkillsInfoUpdate.as_view(), name="update_skills"),
    path(
        "update_language/<int:pk>/",
        LanguageInfoUpdate.as_view(),
        name="update_language",
    ),
    path("update_exp/<int:pk>/", ExperienceInfoUpdate.as_view(), name="update_exp"),
    path(
        "update_education/<int:pk>/",
        EducationInfoUpdate.as_view(),
        name="update_education",
    ),
    path(
        "update_courses/<int:pk>/", CoursesInfoUpdate.as_view(), name="update_courses"
    ),
    path("portfolio_list/", UserListView.as_view(), name="portfolio_list"),
    path("main_create/<int:pk>/", MainInfoCreate.as_view(), name="main_create"),
    path("skills_create/<int:pk>", SkillsInfoCreate.as_view(), name="skills_create"),
    path("skills_delete/<int:pk>", SkillInfoDelete.as_view(), name="skills_delete"),
    path(
        "language_create/<int:pk>", LanguageInfoCreate.as_view(), name="language_create"
    ),
    path(
        "language_delete/<int:pk>", LanguageInfoDelete.as_view(), name="language_delete"
    ),
    path(
        "education_create/<int:pk>",
        EducationInfoCreate.as_view(),
        name="education_create",
    ),
    path(
        "education_delete/<int:pk>",
        EducationInfoDelete.as_view(),
        name="education_delete",
    ),
    path(
        "experience_create/<int:pk>",
        ExperienceInfoCreate.as_view(),
        name="experience_create",
    ),
    path(
        "experience_delete/<int:pk>",
        ExperienceInfoDelete.as_view(),
        name="experience_delete",
    ),
    path("course_create/<int:pk>", CourseInfoCreate.as_view(), name="course_create"),
    path("course_delete/<int:pk>", CourseInfoDelete.as_view(), name="course_delete"),
]
