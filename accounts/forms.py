from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:  # برای اینکه اطلاعات اضافه به فرممون بدیم از متا استفاده میکنیم
        model = CustomUser
        fields = ('username', 'age', 'email', 'first_name', 'last_name', )


class CustomUserChangeForm(UserChangeForm):  # 127-6
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email', 'first_name', 'last_name', )
