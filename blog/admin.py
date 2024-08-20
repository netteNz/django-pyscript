from django.contrib import admin
from blog.models import Post, Category, Comment, Project

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Optional: Display these fields in the list view
    search_fields = ('title', 'description')  # Optional: Add a search bar for title and description

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Project, ProjectAdmin)  # Register the Project model with the ProjectAdmin class
