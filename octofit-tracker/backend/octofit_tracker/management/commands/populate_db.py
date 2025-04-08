from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", age=30)
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", age=25)

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=user1)

        # Create test activities
        Activity.objects.create(user=user1, type="Running", duration=45, date="2025-04-01")
        Activity.objects.create(user=user2, type="Cycling", duration=60, date="2025-04-02")

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, points=150)
        Leaderboard.objects.create(user=user2, points=200)

        # Create test workouts
        Workout.objects.create(name="Morning Yoga", description="A relaxing morning yoga session.")
        Workout.objects.create(name="HIIT Training", description="High-intensity interval training.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))