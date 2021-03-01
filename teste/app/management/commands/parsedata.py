from django.core.management.base import BaseCommand
from django.apps import apps
from app.models.customers_model import Customers
import csv
import requests

cache = {}

class Command(BaseCommand):
    help = 'Creating model objects according the file path specified'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")
        parser.add_argument('--gkey', type=str, help="google maps key")

    def handle(self, *args, **options):
        file_path = options['path']
        key = options['gkey']

        def position_stack(address):
            if address in cache.keys():
                return cache[address]

            params = f"forward?access_key={key}&query={address}&country=US"

            req = requests.get(f"http://api.positionstack.com/v1/{params}")

            try:
                latitude_req = req.json()["data"][0]["latitude"]
                longitude_req = req.json()["data"][0]["longitude"]
                cache[address] = latitude_req, longitude_req
            except TypeError:
                cache[address] = (0, 0)

            return cache[address]

        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    continue

                print(i, row[6])

                latitude, longitude = position_stack(row[6])

                Customers.objects.update_or_create(
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    gender=row[4],
                    company=row[5],
                    city=row[6],
                    title=row[7],
                    longitude=longitude,
                    latitude=latitude,
                )

            # TODO : recebendo aleatoriamente lista vazia, descobrir o motivo
