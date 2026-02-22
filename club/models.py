from django.db import models


class Member(models.Model):
    """
    Model koji predstavlja člana ronilačkog kluba.
    Svaki član može imati više zarona i može imati dodijeljenu opremu.
    """

    first_name = models.CharField(
        max_length=100,
        help_text="Ime člana"
    )

    last_name = models.CharField(
        max_length=100,
        help_text="Prezime člana"
    )

    email = models.EmailField(
        unique=True,
        help_text="Email adresa člana (mora biti jedinstvena)"
    )

    date_joined = models.DateField(
        auto_now_add=True,
        help_text="Datum kada se član učlanio u klub"
    )

    certification = models.CharField(
        max_length=100,
        help_text="Razina ronilačkog certifikata (npr. Open Water, Advanced)"
    )

    def __str__(self):
        # Ovo definira kako će se objekt prikazivati u admin sučelju i listama
        return f"{self.first_name} {self.last_name}"


class Dive(models.Model):
    """
    Model koji predstavlja jedan zaron.
    Svaki zaron je povezan s jednim članom.
    """

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="dives",
        help_text="Član koji je obavio ovaj zaron"
    )

    location = models.CharField(
        max_length=200,
        help_text="Lokacija zarona"
    )

    date = models.DateField(
        help_text="Datum kada je zaron obavljen"
    )

    depth = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Maksimalna dubina zarona u metrima"
    )

    duration = models.PositiveIntegerField(
        help_text="Trajanje zarona u minutama"
    )

    def __str__(self):
        return f"{self.location} - {self.date}"


class Equipment(models.Model):
    """
    Model koji predstavlja ronilačku opremu.
    Oprema može biti dodijeljena jednom članu ili nijednom.
    """

    EQUIPMENT_TYPES = [
        ("tank", "Boca"),
        ("fins", "Peraje"),
        ("suit", "Odijelo"),
        ("mask", "Maska"),
    ]

    name = models.CharField(
        max_length=100,
        help_text="Naziv opreme"
    )

    equipment_type = models.CharField(
        max_length=50,
        choices=EQUIPMENT_TYPES,
        help_text="Tip ronilačke opreme"
    )

    is_functional = models.BooleanField(
        default=True,
        help_text="Označava je li oprema ispravna"
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="equipment",
        help_text="Član kojem je oprema dodijeljena (nije obavezno)"
    )

    def __str__(self):
        return self.name