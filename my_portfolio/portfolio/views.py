from django.shortcuts import render
from .models import Intro, Project, Links, Resume, Contacts

def index(request):
    intros = Intro.objects.all()
    projects = Project.objects.all()
    links = Links.objects.all()
    resumes = Resume.objects.all()
    contacts = Contacts.objects.all()

    context = {'intros': intros, 'projects': projects, 'links': links, 'resumes': resumes, 'contacts': contacts}
    
    return render(request, 'index.html', context)

