from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """ Менеджер пользователей """

    def _create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает нового пользователя, используя адрес электронной почты"""
        if not email:  # проверить наличие пустой электронной почты
            raise AttributeError("User must set an email address")
        else:  # normalizes the provided email
            email = self.normalize_email(email)

        # Создать пользователя
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # хеширует/шифрует пароль
        user.save(using=self._db)  # безопасно для нескольких баз данных
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Создает и возвращает нового пользователя, используя адрес электронной почты"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password=None, **extra_fields):
        """Создает и возвращает нового штатного пользователя, используя адрес электронной почты"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Создает и возвращает нового суперпользователя, используя адрес электронной почты"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Пользовательская модель пользователя """

    email = models.EmailField(
        _("Email Address"),
        max_length=255,
        unique=True,
        help_text="Ex: example@example.com",
    )
    is_staff = models.BooleanField(_("Staff status"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
