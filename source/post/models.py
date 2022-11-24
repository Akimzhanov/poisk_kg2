from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string
from slugify import slugify
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from .utils import get_time

class UserManager(BaseUserManager):
    def _create(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('Поле Username обязательно должно быть заполнено')
        if not email:
            raise ValueError('Поле Email обязательно должно быть заполнено ')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self._create(username, email, password, **extra_fields)



class Post(models.Model):
    CATEGORY_CHOICES = (
        ('documents', 'Документ'),
        ('keys', 'Ключи'),
        ('technique', 'Техника'),
        ('wallets', 'Кошельки'),
        ('animals', 'Животные'),
        ('decorations', 'Украшения'),
        ('bags', 'Сумки'),
        ('other', 'Другое')
    )

    STATUS_CHOICES = [
        ('treatment', 'В обработке'),
        ('open', 'Открыто'),
        ('closed', 'Закрыто')
    ]
    # ADDRESS_CHOICES = (
    #     ('XXXXXX', 'xxxxxx'),
    #     ('YYYYYY', 'yyyyyy')
    # )
    STORAGE_CHOICES = (
        ('lost', 'Потерял'),
        ('find', 'Нашел')
    )
    storage = models.CharField(
        max_length=20,
        choices=STORAGE_CHOICES
    )
    title = models.CharField(verbose_name='Что вы нашли?', max_length=200)
    slug = models.SlugField(max_length=200, primary_key=True, blank=True)
    image = models.ImageField(upload_to='images')
    blur_image = models.ImageField(upload_to='blur_images')

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES, 
        default=STATUS_CHOICES[0][0]
    )
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )
    address = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=13)
    telegram = models.CharField(max_length=100)
    date = models.DateField(verbose_name='Дата находки')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def create_slug(self):
        # slug_post = get_random_string(length=8)
        # if Post.objects.filter(slug=slug_post):
        #     self.create_slug()
        # self.slug = slug_post 
        # # self.slug.save()

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        slug_post = get_random_string(length=14)
        if not self.slug:
            self.slug = slugify(slug_post)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ('created_at',)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})