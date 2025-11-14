from django.db import models


class Culture(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Culture's name"
    )

    class Meta:
        verbose_name = "Culture"
        verbose_name_plural = "Cultures"

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Disease's name"
    )
    type = models.CharField(
        max_length=10,
        default='OTHER',
        verbose_name="Disease's type"
    )
    cultures = models.ManyToManyField(
        Culture,
        related_name="diseases",
        verbose_name="Impressive cultures"
    )

    class Meta:
        verbose_name = "Disease"
        verbose_name_plural = "Diseases"

    def __str__(self):
        return f"{self.name} ({self.type})"


class Drug(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Drug's name"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Price (grn)"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )
    fights_diseases = models.ManyToManyField(
        Disease,
        related_name="drugs",
        verbose_name="Fights diseases"
    )

    class Meta:
        verbose_name = "Drug"
        verbose_name_plural = "Drugs"
        ordering = ["name"]

    def __str__(self):
        return self.name