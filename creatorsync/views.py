from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Campaign, Application, CreatorProfile


# Homepage
def index(request):
    return render(request, "creatorsync/index.html")


# Register
def register_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "creatorsync/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(
                username,
                email,
                password
            )

            user.save()

        except:
            return render(request, "creatorsync/register.html", {
                "message": "Username already taken."
            })

        login(request, user)

        return redirect("index")

    return render(request, "creatorsync/register.html")


# Login
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("index")

        else:

            return render(request, "creatorsync/login.html", {
                "message": "Invalid username or password."
            })

    return render(request, "creatorsync/login.html")


# Logout
def logout_view(request):

    logout(request)

    return redirect("index")


# Campaign List Page
def campaigns_view(request):

    campaigns = Campaign.objects.all()

    return render(request, "creatorsync/campaigns.html", {
        "campaigns": campaigns
    })

def campaign_detail_view(request, campaign_id):

    campaign = Campaign.objects.get(id=campaign_id)

    return render(request, "creatorsync/campaign_detail.html", {
        "campaign": campaign
    })

@login_required
def apply_campaign(request, campaign_id):

    campaign = Campaign.objects.get(id=campaign_id)

    existing_application = Application.objects.filter(
        creator=request.user,
        campaign=campaign
    ).first()

    if existing_application:
        return redirect("campaign_detail", campaign_id=campaign.id)

    Application.objects.create(
        creator=request.user,
        campaign=campaign,
        status="Pending"
    )

    return redirect("campaign_detail", campaign_id=campaign.id)

@login_required
def dashboard(request):

    applications = Application.objects.filter(
        creator=request.user
    )

    application_count = applications.count()

    campaign_count = Campaign.objects.count()

    creator_count = CreatorProfile.objects.count()

    return render(request, "creatorsync/dashboard.html", {
        "applications": applications,
        "application_count": application_count,
        "campaign_count": campaign_count,
        "creator_count": creator_count
    })

@login_required
def profile_view(request):

    profile, created = CreatorProfile.objects.get_or_create(
        user=request.user,
        defaults={
            "instagram": "",
            "tiktok": "",
            "followers": 0
        }
    )

    return render(request, "creatorsync/profile.html", {
        "profile": profile
    })

@login_required
def edit_profile_view(request):

    profile, created = CreatorProfile.objects.get_or_create(
        user=request.user,
        defaults={
            "instagram": "",
            "tiktok": "",
            "followers": 0
        }
    )

    if request.method == "POST":

        profile.instagram = request.POST["instagram"]

        profile.tiktok = request.POST["tiktok"]

        profile.followers = request.POST["followers"]

        profile.save()

        return redirect("profile")

    return render(request, "creatorsync/edit_profile.html", {
        "profile": profile
    })

def creators_view(request):

    creators = CreatorProfile.objects.all()

    return render(request, "creatorsync/creators.html", {
        "creators": creators
    })

@login_required
def applications_view(request):

    applications = Application.objects.all()

    return render(request, "creatorsync/applications.html", {
        "applications": applications
    })