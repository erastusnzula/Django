from django.contrib import admin

from projects.models import Project, Category


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class ProjectCategory(admin.ModelAdmin):
    pass