from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Postpage(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    category = models.CharField(max_length=20)
    sub = models.CharField(max_length=20)
    title = models.CharField(max_length=80)
    price = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(9_999_999)],
    )
    district = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=Status.choices)
    seller = models.CharField(max_length=20)
    description = models.CharField(max_length=4000)
    views = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99_999)],
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(price__isnull=True)
                | models.Q(price__gte=0, price__lte=9_999_999),
                name="postpage_price_in_range",
            ),
            models.CheckConstraint(
                condition=models.Q(views__gte=0, views__lte=99_999),
                name="postpage_views_in_range",
            ),
            models.CheckConstraint(
                condition=models.Q(status__in=["active", "inactive"]),
                name="postpage_status_valid",
            ),
        ]

    def __str__(self):
        return self.title