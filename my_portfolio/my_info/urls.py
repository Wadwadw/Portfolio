from django.urls import path
from .views import main, MainInfoUpdate, SkillsInfoUpdate, LanguageInfoUpdate,\
    EducationInfoUpdate, ExperienceInfoUpdate, CoursesInfoUpdate



app_name = 'my_info'


urlpatterns = [
    path('<int:pk>/', main, name='main'),
    path('update_main/<int:pk>/', MainInfoUpdate.as_view(), name='update_main'),
    path('update_skills/<int:pk>/', SkillsInfoUpdate.as_view(), name='update_skills'),
    path('update_language/<int:pk>/', LanguageInfoUpdate.as_view(), name='update_language'),
    path('update_exp/<int:pk>/', ExperienceInfoUpdate.as_view(), name='update_exp'),
    path('update_education/<int:pk>/', EducationInfoUpdate.as_view(), name='update_education'),
    path('update_courses/<int:pk>/', CoursesInfoUpdate.as_view(), name='update_courses'),

]