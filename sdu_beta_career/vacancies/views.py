from django.shortcuts import render, get_object_or_404
from .models import Vacancy


def vacancy_list(request):
    vacancies = Vacancy.objects.filter()

    return render(request, 'vacancy_list.html', {'vacancies': vacancies})


def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})
