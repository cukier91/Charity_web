from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Type(models.TextChoices):
    foundation = "Fundacja", "Fundacja"
    non_gov_organization = "Organizacja pozarządowa", "Organizacja pozarządowa"
    local_donation = "Zbiórka lokalna", "Zbiórka lokalna"


class CategoryModel(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class InstitutionModel(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50, choices=Type.choices, default=Type.foundation)
    category = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.name


class DonationModel(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(CategoryModel)
    institution = models.ForeignKey(InstitutionModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=20)
    city = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=20)
    pick_up_date = models.DateField(null=False)
    pick_up_time = models.TimeField(null=False)
    pick_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

