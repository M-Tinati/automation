# home/admin.py
from django.contrib import admin
from .models import Message, SavedDocument

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'receiver', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('subject', 'sender__username', 'receiver__username')

@admin.register(SavedDocument)
class SavedDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'uploaded_at', 'file')
    list_filter = ('uploaded_at',)
    search_fields = ('title', 'user__username')