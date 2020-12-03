from django.core.management.base import BaseCommand

from workshop.tests import quick_test


class Command(BaseCommand):
    help = 'Django quick test'

    def handle(self, *args, **options):
        try:
            self.stdout.write('Running quick test ...')
            quick_test()

            self.stdout.write(self.style.SUCCESS('Successfully done'))

        except:
            self.stdout.write('*** Quick test died ***')

