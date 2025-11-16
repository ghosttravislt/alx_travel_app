# listings/management/commands/seed.py
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
import random

User = get_user_model()


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Create a sample host if none exists
        host, created = User.objects.get_or_create(
            username="sample_host",
            defaults={
                "email": "host@example.com",
                "password": "password123",
                "first_name": "Sample",
                "last_name": "Host",
            },
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Created sample host user."))

        sample_data = [
            {
                "title": "Beachfront Villa",
                "description": "A relaxing villa with an ocean view.",
                "location": "Zanzibar",
                "price_per_night": 120.00,
            },
            {
                "title": "Mountain Cabin Retreat",
                "description": "Cozy cabin in the mountains.",
                "location": "Kenya Highlands",
                "price_per_night": 90.00,
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "location": "Accra",
                "price_per_night": 75.00,
            },
        ]

        for data in sample_data:
            Listing.objects.create(
                host=host,
                **data,
            )

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
