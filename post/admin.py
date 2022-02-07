from django.contrib import admin
from .models import Board, Post


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('', {
            'fields': (
                'board_name',
                'is_display'
            )
        }),
        ('날짜정보', {
            'fields': (
                'created_at',
                'updated_at'
            )
        })
    )


@admin.register((Post))
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title',)
    fieldsets = (
        ('', {
            'fields': (
                'board',
                'user',
                'title',
                'context',
                'view_count',
                'is_display',
            )
        }),
        ('날짜정보', {
            'fields': (
                'created_at',
                'updated_at'
            )
        })
    )