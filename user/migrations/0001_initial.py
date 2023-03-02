# Generated by Django 4.1.7 on 2023-02-28 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True, max_length=254, null=True, unique=True
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("state_id", models.PositiveIntegerField()),
                ("state_code", models.CharField(max_length=255)),
                ("country_id", models.PositiveIntegerField()),
                ("country_code", models.CharField(max_length=2)),
                ("latitude", models.DecimalField(decimal_places=8, max_digits=10)),
                ("longitude", models.DecimalField(decimal_places=8, max_digits=11)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("flag", models.BooleanField(default=True)),
                ("wikiDataId", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("iso3", models.CharField(blank=True, max_length=3, null=True)),
                (
                    "numericCode",
                    models.CharField(
                        blank=True, db_column="numeric_code", max_length=3, null=True
                    ),
                ),
                ("iso2", models.CharField(blank=True, max_length=2, null=True)),
                (
                    "phoneCode",
                    models.CharField(
                        blank=True, db_column="phonecode", max_length=255, null=True
                    ),
                ),
                ("capital", models.CharField(blank=True, max_length=255, null=True)),
                ("currency", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "currencyName",
                    models.CharField(
                        blank=True, db_column="currency_name", max_length=255, null=True
                    ),
                ),
                (
                    "currency_symbol",
                    models.CharField(
                        blank=True,
                        db_column="currency_symbol",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("tld", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "_native",
                    models.CharField(
                        blank=True, db_column="native", max_length=255, null=True
                    ),
                ),
                ("region", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "subRegion",
                    models.CharField(
                        blank=True, db_column="subregion", max_length=255, null=True
                    ),
                ),
                ("timezones", models.TextField(blank=True, null=True)),
                ("translations", models.TextField(blank=True, null=True)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=10, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=11, null=True
                    ),
                ),
                ("emoji", models.CharField(blank=True, max_length=191, null=True)),
                ("emojiU", models.CharField(blank=True, max_length=191, null=True)),
                (
                    "createdAt",
                    models.DateTimeField(
                        auto_now_add=True, db_column="created_at", null=True
                    ),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(auto_now=True, db_column="updated_at"),
                ),
                ("flag", models.BooleanField(default=True)),
                (
                    "wikiDataId",
                    models.CharField(
                        blank=True,
                        db_column="wikiDataId",
                        max_length=255,
                        null=True,
                        verbose_name="Rapid API GeoDB Cities",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="State",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("country_id", models.IntegerField()),
                ("country_code", models.CharField(max_length=2)),
                ("fips_code", models.CharField(blank=True, max_length=255, null=True)),
                ("iso2", models.CharField(blank=True, max_length=255, null=True)),
                ("type", models.CharField(blank=True, max_length=191, null=True)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=10, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=11, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("flag", models.BooleanField(default=True)),
                (
                    "wikiDataId",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Rapid API GeoDB Cities",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="user_profile",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=255, null=True)),
                ("is_verified", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("address2", models.CharField(max_length=255)),
                ("zipcode", models.PositiveIntegerField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("description", models.TextField()),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.city"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.country"
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.state"
                    ),
                ),
            ],
        ),
    ]