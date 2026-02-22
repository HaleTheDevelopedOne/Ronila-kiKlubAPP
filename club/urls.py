from django.urls import path
from . import views

urlpatterns = [
    # Home/dashboard (kasnije ćemo to uljepšati)
    path("", views.HomeView.as_view(), name="home"),

    # Member CRUD
    path("members/", views.MemberListView.as_view(), name="member_list"),
    path("members/<int:pk>/", views.MemberDetailView.as_view(), name="member_detail"),
    path("members/create/", views.MemberCreateView.as_view(), name="member_create"),
    path("members/<int:pk>/update/", views.MemberUpdateView.as_view(), name="member_update"),
    path("members/<int:pk>/delete/", views.MemberDeleteView.as_view(), name="member_delete"),

    # Dive CRUD
    path("dives/", views.DiveListView.as_view(), name="dive_list"),
    path("dives/<int:pk>/", views.DiveDetailView.as_view(), name="dive_detail"),
    path("dives/create/", views.DiveCreateView.as_view(), name="dive_create"),
    path("dives/<int:pk>/update/", views.DiveUpdateView.as_view(), name="dive_update"),
    path("dives/<int:pk>/delete/", views.DiveDeleteView.as_view(), name="dive_delete"),

    # Equipment CRUD
    path("equipment/", views.EquipmentListView.as_view(), name="equipment_list"),
    path("equipment/<int:pk>/", views.EquipmentDetailView.as_view(), name="equipment_detail"),
    path("equipment/create/", views.EquipmentCreateView.as_view(), name="equipment_create"),
    path("equipment/<int:pk>/update/", views.EquipmentUpdateView.as_view(), name="equipment_update"),
    path("equipment/<int:pk>/delete/", views.EquipmentDeleteView.as_view(), name="equipment_delete"),
]