from django.shortcuts import render, get_object_or_404
from sdu_beta_career.resumes.models import Resume


def resume_detail(request, pk):
    resume_details = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume.html', {'resume': resume_details})




