from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)  # Название
    location = models.CharField(max_length=128)  # Город
    logo = models.URLField(default='https://place-hold.it/100x60')  # Логотипчик
    description = models.TextField()  # Информация о компании
    employee_count = models.IntegerField()  # Количество сотрудников


class Specialty(models.Model):
    code = models.CharField(max_length=128)  # Код например, testing, gamedev
    title = models.CharField(max_length=128)  # Название
    picture = models.URLField(default='https://place-hold.it/100x60')  # Картинка


class Vacancy(models.Model):
    title = models.CharField(max_length=128)  # Название вакансии
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")  # Специализация
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")  # Компания
    skills = models.CharField(max_length=128)  # Навыки
    description = models.TextField()  # Текст
    salary_min = models.IntegerField()  # Зарплата от
    salary_max = models.IntegerField()  # Зарплата до
    published_at = models.DateField()  # Опубликовано

    def __str__(self):
        return self.title
