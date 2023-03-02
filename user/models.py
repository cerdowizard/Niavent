from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils import timezone


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None  # remove username field, we will use email as unique identifier
    email = models.EmailField(unique=True, null=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_profile")
    phone = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


class Country(models.Model):
    name = models.CharField(max_length=100)
    iso3 = models.CharField(max_length=3, null=True, blank=True)
    numericCode = models.CharField(max_length=3, null=True, blank=True, db_column='numeric_code')
    iso2 = models.CharField(max_length=2, null=True, blank=True)
    phoneCode = models.CharField(max_length=255, null=True, blank=True, db_column='phonecode')
    capital = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)
    currencyName = models.CharField(max_length=255, null=True, blank=True, db_column='currency_name')
    currency_symbol = models.CharField(max_length=255, null=True, blank=True, db_column='currency_symbol')
    tld = models.CharField(max_length=255, null=True, blank=True)
    _native = models.CharField(max_length=255, null=True, blank=True, db_column='native')
    region = models.CharField(max_length=255, null=True, blank=True)
    subRegion = models.CharField(max_length=255, null=True, blank=True, db_column='subregion')
    timezones = models.TextField(null=True, blank=True)
    translations = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    emoji = models.CharField(max_length=191, null=True, blank=True)
    emojiU = models.CharField(max_length=191, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, db_column='created_at')
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')
    flag = models.BooleanField(default=True)
    wikiDataId = models.CharField(max_length=255, null=True, blank=True, db_column='wikiDataId',
                                  verbose_name='Rapid API GeoDB Cities')


    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    state_id = models.PositiveIntegerField()
    state_code = models.CharField(max_length=255)
    country_id = models.PositiveIntegerField()
    country_code = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)
    wikiDataId = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
        return self.name


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country_id = models.IntegerField()
    country_code = models.CharField(max_length=2)
    fips_code = models.CharField(max_length=255, null=True, blank=True)
    iso2 = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=191, null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    flag = models.BooleanField(default=True)
    wikiDataId = models.CharField(max_length=255, null=True, blank=True, verbose_name="Rapid API GeoDB Cities")



    def __str__(self):
        return self.name


class Location(models.Model):
    tag = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    zipcode = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()


    def __str__(self):
        return self.description
