from django.contrib import admin

from .models import Post, User, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_filter = ('author', 'categories')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('id',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'created_at',
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_content',
        'post',
        'author',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'content',
        'post__title',
        'author__username',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'author',
    )
    ordering = ('-created_at',)

    @admin.display(description='Content')
    def short_content(self, obj):
        return obj.content[:50]