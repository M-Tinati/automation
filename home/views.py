from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Message, SavedDocument


class HomeView(LoginRequiredMixin, View):
    template_name = 'home/dashboard.html'

    def get(self, request):
        # لیست کاربران برای منوی کشویی گیرنده (به جز خود کاربر)
        users = User.objects.exclude(id=request.user.id).order_by('username')

        # پیام‌های دریافتی کاربر فعلی
        received_messages = Message.objects.filter(receiver=request.user).order_by('-created_at')

        # پیام‌های ارسالی کاربر فعلی
        sent_messages = Message.objects.filter(sender=request.user).order_by('-created_at')

        # اسناد ذخیره‌شده کاربر فعلی
        saved_documents = SavedDocument.objects.filter(user=request.user).order_by('-uploaded_at')

        context = {
            'users': users,
            'received_messages': received_messages,
            'sent_messages': sent_messages,
            'saved_documents': saved_documents,
        }
        print(f"کاربر: {request.user.username}")
        print(f"پیام‌های ارسالی: {sent_messages.count()}")
        print(f"پیام‌های دریافتی: {received_messages.count()}")
        return render(request, self.template_name, context)


class SendMessageView(LoginRequiredMixin, View):
    def post(self, request):
        receiver_id = request.POST.get('receiver')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        # اعتبارسنجی ورودی‌ها
        if not receiver_id or not subject or not body:
            messages.error(request, 'همه فیلدها (گیرنده، موضوع و متن پیام) الزامی هستند.')
            return redirect('home:home')

        try:
            receiver = User.objects.get(id=receiver_id)

            # ذخیره واقعی پیام در دیتابیس
            Message.objects.create(
                sender=request.user,
                receiver=receiver,
                subject=subject.strip(),
                body=body.strip()
            )

            receiver_name = receiver.get_full_name() or receiver.username
            messages.success(request, f'پیام با موفقیت به {receiver_name} ارسال شد.')

        except User.DoesNotExist:
            messages.error(request, 'کاربر گیرنده یافت نشد. دوباره تلاش کنید.')
        except Exception as e:
            messages.error(request, 'خطایی در ارسال پیام رخ داد. لطفاً دوباره تلاش کنید.')
            print("خطا در SendMessageView:", e)  # برای دیباگ در کنسول

        return redirect('home:home')


class SaveDocumentView(LoginRequiredMixin, View):
    def post(self, request):
        files = request.FILES.getlist('files')  # پشتیبانی از چند فایل همزمان
        title = request.POST.get('title', '').strip()

        if not files:
            messages.error(request, 'حداقل یک فایل برای ذخیره انتخاب کنید.')
            return redirect('home:home')

        created_count = 0
        for file in files:
            SavedDocument.objects.create(
                user=request.user,
                title=title if title else None,
                file=file
            )
            created_count += 1

        if created_count == 1:
            messages.success(request, 'سند با موفقیت ذخیره شد.')
        else:
            messages.success(request, f'{created_count} سند با موفقیت ذخیره شد.')

        return redirect('home:home')