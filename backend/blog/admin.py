from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost
from .models import Post, Comment

class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'category', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )

admin.site.register(BlogPost, BlogPostAdmin)

class PostAdmin(admin.ModelAdmin):
	search_fields = ('title', )

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)