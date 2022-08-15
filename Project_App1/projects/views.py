from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProjectForm, ContactusForm

from .models import Project, Contactus


# Create your views here.

# return all projects
def projects(request):
    project_dic = Project.objects.all()
    return render(request,'projects/all-project.html',{'project':project_dic})

# return all projects with details
def allprojects(request):
    project_dic = Project.objects.all()
    return render(request,'projects/all-projects.html',{'project':project_dic})


# default homepage
def homepage(request):
    return render(request,'projects/homepage.html')

# return details of all projects
def projectbyid(request,uid):
    project_dic = Project.objects.get(id=uid)
    #tags = project_dic.tags.all()
    return render(request,'projects/single-project.html',{'pdic':project_dic})

def contactus(request):
    form = ContactusForm()

    if request.method=='POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form':form}
    return render(request,'projects/contact-form.html',context)


# view to create a new project entry
def project_create_form(request):
    form = ProjectForm()

    if request.method=='POST':
        #print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_projects_details')

    context = {'form':form}
    return render(request,'projects/project_form.html',context)


# view to update/modify a old project entry present into the database
def project_update_form(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method=='POST':
        #print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('all_projects_details')

    context = {'form':form}
    return render(request,'projects/project_form.html',context)


# view to delete the old project from the db

def delete_project(request,pk):
    project = Project.objects.get(id=pk)

    if request.method=='POST':
        project.delete()
        return redirect('all_projects_details')
        
    context = {'obj':project}
    return render(request, 'projects/delete_template.html',context)



