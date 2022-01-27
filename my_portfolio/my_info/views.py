from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import MainInfoBlock, SkillsInfoBlock, LanguagesInfoBlock, ExperienceInfoBlock,\
    EducationInfoBlock, CoursesInfoBlock, User
from .forms import MainInfoForm, SkillInfoForm, LanguageInfoForm, ExperienceInfoForm,\
    EducationInfoForm, CourseInfoForm


def main(request, pk):
    user = User.objects.get(pk=pk)
    main = MainInfoBlock.objects.filter(user=user)
    skills = SkillsInfoBlock.objects.filter(user=user)
    language = LanguagesInfoBlock.objects.filter(user=user)
    exp = ExperienceInfoBlock.objects.filter(user=user)
    educa = EducationInfoBlock.objects.filter(user=user)
    course = CoursesInfoBlock.objects.filter(user=user)

    context = {
        'main': main,
        'skills': skills,
        'languages': language,
        'exps': exp,
        'educas': educa,
        'course': course
    }

    return render(request, 'my_info/main_info.html', context=context)


class MainInfoUpdate(generic.UpdateView):
    template_name = 'my_info/main_update.html'
    form_class = MainInfoForm

    def get_queryset(self):
        return MainInfoBlock.objects.all()

    def get_success_url(self):
        return reverse('my_info:main', args=str(self.request.user.pk))


class SkillsInfoUpdate(generic.UpdateView):
    template_name = 'my_info/skills_update.html'
    form_class = SkillInfoForm
    context_object_name = 'skills_forms'

    def get_queryset(self):
        skills = SkillsInfoBlock.objects.all()
        return skills

    def get_success_url(self):
        return reverse('my_info:main', args=str(self.request.user.pk))


class LanguageInfoUpdate(generic.UpdateView):
    template_name = 'my_info/language_update.html'
    form_class = LanguageInfoForm
    context_object_name = 'language_form'

    def get_queryset(self):
        language = LanguagesInfoBlock.objects.all()
        return language

    def get_success_url(self):
        return reverse('my_info:main', args=str(self.request.user.pk))


class ExperienceInfoUpdate(generic.UpdateView):
    template_name = 'my_info/exp_update.html'
    form_class = ExperienceInfoForm

    def get_queryset(self):
        language = ExperienceInfoBlock.objects.all()
        return language

    def get_success_url(self):
        return reverse('my_info:main', args=str(self.request.user.pk))


class EducationInfoUpdate(generic.UpdateView):
    template_name = 'my_info/education_update.html'
    form_class = EducationInfoForm

    def get_queryset(self):
        language = EducationInfoBlock.objects.all()
        return language

    def get_success_url(self):
        return reverse('my_info:main', args=str(self.request.user.pk))


class CoursesInfoUpdate(generic.UpdateView):
    template_name = 'my_info/courses_update.html'
    form_class = CourseInfoForm

    def get_queryset(self):
        language = CoursesInfoBlock.objects.all()
        return language

    def get_success_url(self):
        return reverse('my_info:main', args=str(self.request.user.pk))
