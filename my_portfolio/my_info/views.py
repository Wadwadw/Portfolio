from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import (
    MainInfoBlock,
    SkillsInfoBlock,
    LanguagesInfoBlock,
    ExperienceInfoBlock,
    EducationInfoBlock,
    CoursesInfoBlock,
    User,
)
from .forms import (
    MainInfoForm,
    SkillInfoForm,
    LanguageInfoForm,
    ExperienceInfoForm,
    EducationInfoForm,
    CourseInfoForm,
)


def main(request, pk):
    user = User.objects.get(pk=pk)
    main = MainInfoBlock.objects.filter(user=user)
    skills = SkillsInfoBlock.objects.filter(user=user)
    language = LanguagesInfoBlock.objects.filter(user=user)
    exp = ExperienceInfoBlock.objects.filter(user=user)
    educa = EducationInfoBlock.objects.filter(user=user)
    course = CoursesInfoBlock.objects.filter(user=user)

    context = {
        "main": main,
        "skills": skills,
        "languages": language,
        "exps": exp,
        "educas": educa,
        "course": course,
    }

    return render(request, "my_info/main_info.html", context=context)


class UserListView(generic.ListView):
    template_name = "my_info/portfolio_list.html"
    context_object_name = "portfolios"

    def get_queryset(self):
        return MainInfoBlock.objects.all()

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))


class MainInfoCreate(generic.CreateView):
    template_name = "my_info/main_create.html"
    form_class = MainInfoForm

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))


class MainInfoUpdate(generic.UpdateView):
    template_name = "my_info/main_update.html"
    form_class = MainInfoForm

    def get_queryset(self):
        return MainInfoBlock.objects.all()

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))


class MainInfoDelete(generic.DeleteView):
    template_name = "my_info/main_delete.html"

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def get_queryset(self):
        return MainInfoBlock.objects.all()


class SkillsInfoUpdate(generic.UpdateView):
    template_name = "my_info/skills_update.html"
    form_class = SkillInfoForm
    context_object_name = "skills_forms"

    def get_queryset(self):
        skills = SkillsInfoBlock.objects.all()
        return skills

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))


class SkillsInfoCreate(generic.CreateView):
    template_name = "my_info/skills_create.html"
    form_class = SkillInfoForm

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def form_valid(self, form):
        skill = form.save(commit=False)
        skill.user = self.request.user
        skill.save()
        return super(SkillsInfoCreate, self).form_valid(form)


class SkillInfoDelete(generic.DeleteView):
    template_name = "my_info/skills_delete.html"

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def get_queryset(self):
        return SkillsInfoBlock.objects.all()


class LanguageInfoUpdate(generic.UpdateView):
    template_name = "my_info/language_update.html"
    form_class = LanguageInfoForm
    context_object_name = "language_form"

    def get_queryset(self):
        language = LanguagesInfoBlock.objects.all()
        return language

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))


class LanguageInfoCreate(generic.CreateView):
    template_name = "my_info/language_create.html"
    form_class = LanguageInfoForm

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def form_valid(self, form):
        language = form.save(commit=False)
        language.user = self.request.user
        language.save()
        return super(LanguageInfoCreate, self).form_valid(form)


class LanguageInfoDelete(generic.DeleteView):
    template_name = "my_info/language_delete.html"

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def get_queryset(self):
        return LanguagesInfoBlock.objects.all()


class ExperienceInfoUpdate(generic.UpdateView):
    template_name = "my_info/exp_update.html"
    form_class = ExperienceInfoForm

    def get_queryset(self):
        language = ExperienceInfoBlock.objects.all()
        return language

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))


class ExperienceInfoCreate(generic.CreateView):
    template_name = "my_info/exp_create.html"
    form_class = ExperienceInfoForm

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def form_valid(self, form):
        exp = form.save(commit=False)
        exp.user = self.request.user
        exp.save()
        return super(ExperienceInfoCreate, self).form_valid(form)


class ExperienceInfoDelete(generic.DeleteView):
    template_name = "my_info/exp_delete.html"

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def get_queryset(self):
        return SkillsInfoBlock.objects.all()


class EducationInfoUpdate(generic.UpdateView):
    template_name = "my_info/education_update.html"
    form_class = EducationInfoForm

    def get_queryset(self):
        language = EducationInfoBlock.objects.all()
        return language

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))


class EducationInfoCreate(generic.CreateView):
    template_name = "my_info/education_create.html"
    form_class = EducationInfoForm

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def form_valid(self, form):
        ed = form.save(commit=False)
        ed.user = self.request.user
        ed.save()
        return super(EducationInfoCreate, self).form_valid(form)


class EducationInfoDelete(generic.DeleteView):
    template_name = "my_info/education_delete.html"

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def get_queryset(self):
        return EducationInfoBlock.objects.all()


class CoursesInfoUpdate(generic.UpdateView):
    template_name = "my_info/courses_update.html"
    form_class = CourseInfoForm

    def get_queryset(self):
        language = CoursesInfoBlock.objects.all()
        return language

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))


class CourseInfoCreate(generic.CreateView):
    template_name = "my_info/course_create.html"
    form_class = CourseInfoForm

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def form_valid(self, form):
        course = form.save(commit=False)
        course.user = self.request.user
        course.save()
        return super(CourseInfoCreate, self).form_valid(form)


class CourseInfoDelete(generic.DeleteView):
    template_name = "my_info/course_delete.html"

    def get_success_url(self):
        return reverse("my_info:main", args=str(self.request.user.pk))

    def get_queryset(self):
        return CoursesInfoBlock.objects.all()
