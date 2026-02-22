from django.contrib import admin
from .models import Member, Dive, Equipment


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    """
    Admin konfiguracija za model Member.
    Ovdje definiramo kako se članovi prikazuju u adminu:
    - list_display: koje kolone vidimo u listi
    - search_fields: po kojim poljima možemo pretraživati
    - list_filter: filteri u desnoj strani admina
    """
    list_display = ("first_name", "last_name", "email", "certification", "date_joined")
    search_fields = ("first_name", "last_name", "email", "certification")
    list_filter = ("certification", "date_joined")


@admin.register(Dive)
class DiveAdmin(admin.ModelAdmin):
    """
    Admin konfiguracija za model Dive.
    U listi zarona želimo odmah vidjeti:
    - člana (member)
    - lokaciju, datum, dubinu i trajanje
    Također omogućimo filtriranje po datumu i lokaciji.
    """
    list_display = ("member", "location", "date", "depth", "duration")
    search_fields = ("location", "member__first_name", "member__last_name", "member__email")
    list_filter = ("date", "location")


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """
    Admin konfiguracija za opremu.
    Prikazujemo tip, ispravnost i (ako postoji) kojem članu je dodijeljena.
    """
    list_display = ("name", "equipment_type", "is_functional", "member")
    search_fields = ("name",)
    list_filter = ("equipment_type", "is_functional")