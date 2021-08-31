from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Category'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='projects')
    github_link = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Project'
        verbose_name_plural = 'Project'

    def __str__(self):
        return self.title
