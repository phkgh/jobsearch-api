from django.core.management.base import BaseCommand
from jobs.models import JobPost
from faker import Faker
import random


class Command(BaseCommand):
    help = "Generate fake job listings for testing"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int,
                            help='Number of fake job posts to create')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()
        created = 0

        for _ in range(total):
            JobPost.objects.create(
                title=fake.job(),
                company=fake.company(),
                location=fake.city(),
                salary=random.randint(30000, 250000),
                description=fake.text(max_nb_chars=200)
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {created} fake job posts.'))
