from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from .models import Member, Dive, Equipment


class HomeView(TemplateView):
    """
    Najjednostavniji Home ekran.
    TemplateView samo rendera template bez posebne logike.
    """
    template_name = "home.html"


# -------------------------
# MEMBER VIEWS
# -------------------------

class MemberListView(ListView):
    """
    ListView prikazuje listu objekata iz baze.
    Ovdje dodajemo i jednostavnu pretragu preko GET parametra ?q=...
    """
    model = Member
    template_name = "members/member_list.html"
    context_object_name = "members"
    paginate_by = 10  # ispitno + praktično (straničenje)

    def get_queryset(self):
        """
        Vraća queryset koji se prikazuje u listi.
        Ako postoji q, filtriramo po imenu/prezimenu/emailu/certifikatu.
        """
        qs = super().get_queryset().order_by("last_name", "first_name")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q) |
                Q(email__icontains=q) |
                Q(certification__icontains=q)
            )
        return qs


class MemberDetailView(DetailView):
    """
    DetailView prikazuje jedan objekt (po pk).
    """
    model = Member
    template_name = "members/member_detail.html"
    context_object_name = "member"


class MemberCreateView(CreateView):
    """
    CreateView automatski kreira formu iz modela.
    fields definiraju koja polja su u formi.
    """
    model = Member
    fields = ["first_name", "last_name", "email", "certification"]
    template_name = "members/member_form.html"

    def get_success_url(self):
        """
        Nakon uspješnog unosa preusmjeri na detalje tog člana.
        """
        return reverse_lazy("member_detail", kwargs={"pk": self.object.pk})


class MemberUpdateView(UpdateView):
    """
    UpdateView radi isto kao CreateView, ali uređuje postojeći objekt.
    """
    model = Member
    fields = ["first_name", "last_name", "email", "certification"]
    template_name = "members/member_form.html"

    def get_success_url(self):
        return reverse_lazy("member_detail", kwargs={"pk": self.object.pk})


class MemberDeleteView(DeleteView):
    """
    DeleteView traži potvrdu brisanja, a zatim briše objekt.
    """
    model = Member
    template_name = "members/member_confirm_delete.html"
    success_url = reverse_lazy("member_list")  # nakon brisanja vrati na listu


# -------------------------
# DIVE VIEWS
# -------------------------

class DiveListView(ListView):
    model = Dive
    template_name = "dives/dive_list.html"
    context_object_name = "dives"
    paginate_by = 10

    def get_queryset(self):
        """
        Pretraga po lokaciji i članu (ime/prezime/email).
        """
        qs = super().get_queryset().select_related("member").order_by("-date")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(location__icontains=q) |
                Q(member__first_name__icontains=q) |
                Q(member__last_name__icontains=q) |
                Q(member__email__icontains=q)
            )
        return qs


class DiveDetailView(DetailView):
    model = Dive
    template_name = "dives/dive_detail.html"
    context_object_name = "dive"


class DiveCreateView(CreateView):
    model = Dive
    fields = ["member", "location", "date", "depth", "duration"]
    template_name = "dives/dive_form.html"

    def get_success_url(self):
        return reverse_lazy("dive_detail", kwargs={"pk": self.object.pk})


class DiveUpdateView(UpdateView):
    model = Dive
    fields = ["member", "location", "date", "depth", "duration"]
    template_name = "dives/dive_form.html"

    def get_success_url(self):
        return reverse_lazy("dive_detail", kwargs={"pk": self.object.pk})


class DiveDeleteView(DeleteView):
    model = Dive
    template_name = "dives/dive_confirm_delete.html"
    success_url = reverse_lazy("dive_list")


# -------------------------
# EQUIPMENT VIEWS
# -------------------------

class EquipmentListView(ListView):
    model = Equipment
    template_name = "equipment/equipment_list.html"
    context_object_name = "equipment"
    paginate_by = 10

    def get_queryset(self):
        """
        Pretraga po nazivu + filtriranje po tipu kroz GET parametar ?type=tank
        """
        qs = super().get_queryset().select_related("member").order_by("name")
        q = self.request.GET.get("q")
        eq_type = self.request.GET.get("type")

        if q:
            qs = qs.filter(name__icontains=q)

        if eq_type:
            qs = qs.filter(equipment_type=eq_type)

        return qs


class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = "equipment/equipment_detail.html"
    context_object_name = "item"


class EquipmentCreateView(CreateView):
    model = Equipment
    fields = ["name", "equipment_type", "is_functional", "member"]
    template_name = "equipment/equipment_form.html"

    def get_success_url(self):
        return reverse_lazy("equipment_detail", kwargs={"pk": self.object.pk})


class EquipmentUpdateView(UpdateView):
    model = Equipment
    fields = ["name", "equipment_type", "is_functional", "member"]
    template_name = "equipment/equipment_form.html"

    def get_success_url(self):
        return reverse_lazy("equipment_detail", kwargs={"pk": self.object.pk})


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = "equipment/equipment_confirm_delete.html"
    success_url = reverse_lazy("equipment_list")