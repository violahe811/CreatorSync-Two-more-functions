from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),

    path("campaigns", views.campaigns_view, name="campaigns"),

    path(
        "campaign/<int:campaign_id>",
        views.campaign_detail_view,
        name="campaign_detail"
    ),

    path(
        "campaign/<int:campaign_id>/apply",
        views.apply_campaign,
        name="apply_campaign"
    ),

    path("dashboard", views.dashboard, name="dashboard"),

    path("profile", views.profile_view, name="profile"),

    path(
        "profile/edit",
        views.edit_profile_view,
        name="edit_profile"
    ),

    path("creators", views.creators_view, name="creators"),
    path("applications", views.applications_view, name="applications"),
]