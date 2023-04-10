import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from faker import Faker
from first_app.models import Topic, Webpage, AccessRecord, User

fakegen = Faker()
topics = ['Games', 'Search', 'Marketplace', 'Social', 'News', 'TEST FROM actual WEBPAGE']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # create the fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_first_name = fakegen.name().split()[0]
        fake_last_name = fakegen.name().split()[1]
        fake_email = fakegen.email()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Populating script")
