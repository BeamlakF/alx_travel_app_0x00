from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Cozy Apartment in Addis Ababa",
                "description": "2-bedroom apartment close to Bole airport.",
                "price_per_night": 50.00,
                "location": "Addis Ababa, Ethiopia"
            },
            {
                "title": "Beachfront Villa in Zanzibar",
                "description": "Luxurious villa with private pool and ocean view.",
                "price_per_night": 200.00,
                "location": "Zanzibar, Tanzania"
            },
            {
                "title": "Safari Lodge in Serengeti",
                "description": "Experience the wild in a beautiful safari lodge.",
                "price_per_night": 150.00,
                "location": "Serengeti, Tanzania"
            },
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings!"))
