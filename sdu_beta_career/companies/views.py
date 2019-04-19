from django.shortcuts import render, get_object_or_404
from .models import Company


def company_list(request):
    companies = Company.objects.filter()
    return render(request, 'company_list.html', {'companies': companies})
