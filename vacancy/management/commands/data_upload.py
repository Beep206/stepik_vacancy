from django.core.management import BaseCommand
from vacancy.data import jobs, companies, specialties
from vacancy.models import Company, Specialty, Vacancy


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in specialties:
            code = i.get("code")
            title = i.get("title")

            specialty = Specialty(
                code=code,
                title=title,
            )
            specialty.save()

        for i in companies:
            name = i.get("title")
            location = i.get("location")
            description = i.get("description")
            employee_count = i.get("employee_count")
            logo = i.get("logo")

            company = Company(
                name=name,
                location=location,
                description=description,
                employee_count=employee_count,
                logo=logo,
            )

            company.save()

        for i in jobs:
            title = i.get("title")
            skills = i.get("skills")
            description = i.get("description")
            salary_from = i.get("salary_from")
            salary_to = i.get("salary_to")
            posted = i.get("posted")

            vacancy = Vacancy(
                title=title,
                specialty=Specialty.objects.get(code=i['specialty']),
                company=Company.objects.get(id=i['company']),
                skills=skills,
                description=description,
                salary_min=salary_from,
                salary_max=salary_to,
                published_at=posted,
            )

            vacancy.save()
