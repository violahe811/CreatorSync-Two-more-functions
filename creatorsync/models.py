from django.db import models
from django.contrib.auth.models import User


# Creator profile information
class CreatorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    niche = models.CharField(max_length=100)
    follower_count = models.IntegerField()
    social_link = models.URLField()

    def __str__(self):
        return self.user.username


# Brand collaboration campaigns
class Campaign(models.Model):
    brand = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Creator applications to campaigns
class Application(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Pending")
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.creator.username} - {self.campaign.title}"


# Shipment tracking information
class Shipment(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=50)
    shipped_date = models.DateField()

    def __str__(self):
        return self.tracking_number

class CreatorProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField()

    tiktok = models.CharField(
        max_length=100
    )

    instagram = models.CharField(
        max_length=100
    )

    followers = models.IntegerField()

    niche = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.user.username
