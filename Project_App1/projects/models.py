from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # overriting the default id with uuid
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    vote_total = models.IntegerField(default=0,blank=True,null=True)
    vote_ratio = models.IntegerField(default=0,blank=True,null=True)

    # creating M to M 
    tags = models.ManyToManyField('Tag',blank=True)
    '''
    we can also create this using, tags = models.ManyToManyField(Tag) but we need to move Tag before 
    this code

    '''

    def __str__(self):
        return self.title

class Review(models.Model):
    vote_type = (
        ('up','up vote'),
        ('down','down vote'),
    )

    # foreign key : establishes 1 to Many
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=200, choices=vote_type)
    
    
    def __str__(self):
        return self.project.title +'  Vote : '+self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Contactus(models.Model):
    name = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)
    project_details = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name + ' Project: ' + self.project_name