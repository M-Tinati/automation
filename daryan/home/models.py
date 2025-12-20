from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} - از {self.sender} به {self.receiver}"
    
    
class SavedDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_documents')
    title = models.CharField(max_length=200, blank=True, null=True)  # عنوان/یادداشت اختیاری
    file = models.FileField(upload_to='saved_documents/%Y/%m/%d/')  # مسیر ذخیره فایل‌ها
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"سند بدون عنوان - {self.uploaded_at.strftime('%Y-%m-%d')}"