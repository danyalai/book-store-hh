from django.db import models
from django.contrib.auth.models import AbstractUser

# برای اینکه در آینده بتوانیم جدول user را تغییر بدهیم قبل از migration این مدل ایجاد میکنیم AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    # ایحاد یک customuser شخصی برای ایجاد قابلیت شخصی سازی user ما & تفاوت null  و blank در درس 126
