from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True, null=True,
        verbose_name="фотография пользователя"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    statistics = models.TextField(
        blank=True,
        verbose_name="Статика"
    )
    achievements = models.TextField(
        blank=True,
        verbose_name="Достижения"
    )

    class Meta:
        verbose_name="Профиль"
        verbose_name_plural="Профили"


