from django.core.management.base import BaseCommand
from club.models import Member, Dive, Equipment
from random import choice, randint
from datetime import date, timedelta


class Command(BaseCommand):
    """
    Custom Django management command za generiranje testnih podataka.
    Pokreće se s: python manage.py seed
    """

    help = "Generira testne podatke za ronilački klub"

    def handle(self, *args, **options):
        # Prvo brišemo postojeće podatke da ne dupliramo zapise
        Dive.objects.all().delete()
        Equipment.objects.all().delete()
        Member.objects.all().delete()

        self.stdout.write(self.style.WARNING("Postojeći podaci obrisani."))

        # --- ČLANOVI ---
        certifications = ["Open Water", "Advanced", "Rescue Diver"]

        members = []
        for i in range(10):
            member = Member.objects.create(
                first_name=f"Clan{i}",
                last_name=f"Prezime{i}",
                email=f"clan{i}@klub.hr",
                certification=choice(certifications)
            )
            members.append(member)

        self.stdout.write(self.style.SUCCESS("Generirano 10 članova."))

        # --- ZARONI ---
        for _ in range(30):
            Dive.objects.create(
                member=choice(members),
                location=choice(["Jadransko more", "Plitvice", "Crveno more"]),
                date=date.today() - timedelta(days=randint(1, 365)),
                depth=randint(10, 40),
                duration=randint(20, 90)
            )

        self.stdout.write(self.style.SUCCESS("Generirano 30 zarona."))

        # --- OPREMA ---
        equipment_types = ["tank", "fins", "suit", "mask"]

        for i in range(15):
            Equipment.objects.create(
                name=f"Oprema {i}",
                equipment_type=choice(equipment_types),
                is_functional=choice([True, False]),
                member=choice(members + [None])  # neka oprema nema vlasnika
            )

        self.stdout.write(self.style.SUCCESS("Generirano 15 komada opreme."))

        self.stdout.write(self.style.SUCCESS("Seedanje baze završeno ✅"))