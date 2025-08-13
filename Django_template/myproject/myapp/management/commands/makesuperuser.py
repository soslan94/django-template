from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from django.conf import settings

class Command(BaseCommand):
    help = ('Создать суперпользователя с данными, указанными в файле настроек settings.py. '
            'При этом необходимо убедиться, что соответствующая информация указана в переменных окружения.')

    def handle(self, *args, **options):
        username = settings.SUPERUSER_USERNAME
        email = settings.SUPERUSER_EMAIL
        password = settings.SUPERUSER_PASSWORD
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS((f'Создан суперпользователь "{username}". Email: "{email}". Пароль: "{password}"')))
        else:
            self.stdout.write(self.style.WARNING(f'Суперпользователь "{username}" уже существует в базе данных.'))