from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from projects.models import Project


def project_category(request, category):
    all_projects_ = Project.objects.filter(categories__name__contains=category).order_by('-created_on')

    paginator = Paginator(all_projects_, 3)
    page_number = request.GET.get('page')
    try:
        projects = paginator.get_page(page_number)
    except PageNotAnInteger:
        projects = paginator.get_page(page_number)
    except EmptyPage:
        projects = paginator.get_page(page_number)

    context = {
        'projects': projects,
        'category': category
    }
    return render(request, 'projects/project_category.html', context)


def projects_list(request):
    all_projects = Project.objects.all()
    paginator = Paginator(all_projects, 3)
    page_number = request.GET.get('page')
    try:
        projects = paginator.get_page(page_number)
    except PageNotAnInteger:
        projects = paginator.get_page(page_number)
    except EmptyPage:
        projects = paginator.get_page(page_number)
    context = {
        'projects': projects
    }
    return render(request, 'projects/list_projects.html', context)


def project_details(request, id):
    project = Project.objects.get(id=id)

    context = {
        'project': project,
    }

    return render(request, 'projects/project_detail.html', context)
