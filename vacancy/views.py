from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from vacancy.models import Specialty, Company, Vacancy


class MainView(View):

    def get(self, request, *args, **kwargs):
        specialty = Specialty.objects.all()
        specialty_count = Specialty.objects.annotate(vacancy_count=Count("vacancies"))
        company = Company.objects.all()
        vacancy_count_company = Company.objects.annotate(vacancy_count=Count("vacancies"))

        return render(
            request,
            "vacancy/index.html",
            {
                "specialty": specialty,
                "specialty_count": specialty_count,
                "company": company,
                "vacancy_count_company": vacancy_count_company,
            }
        )


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancies.html'


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = 'vacancy/company_specialty.html'
    slug_field = "code"
    slug_url_kwarg = "code"

    def get_context_data(self, **kwargs):
        context = super(SpecialtyDetailView, self).get_context_data(**kwargs)
        context["vacancy_list"] = Vacancy.objects.filter(specialty_id=self.object.id)

        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'vacancy/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context["vacancy_list"] = Vacancy.objects.filter(company__id=self.object.id)

        return context


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy/vacancy.html'


def custom_handler404(request, exception):
    return HttpResponseNotFound("404 Страница не найдена")


def custom_handler500(request):
    return HttpResponseServerError("500 Server Error")
