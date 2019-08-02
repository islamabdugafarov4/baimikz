from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Articles


# Create your views here.
def listing(request):
    project_list = Articles.objects.all().order_by('-date')[:5]  # Срез записей через БД
    paginator = Paginator(project_list, 5)  # Пагинация 5 записей на странице
    page = request.GET.get('page', 1)
    project_list = paginator.page(page)
    return render(request, 'projects/posts.html', {'posts': project_list})

# class ProjectsListView(ListView):
#     projects = Articles.objects.all().order_by('-date')[:20]
#     template_name = 'projects/posts.html'
#     context_object_name = 'projects_list'
#     paginate_by = 20
