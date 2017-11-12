import factory
from .models import Tweet
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = 'secret'
    email = factory.Faker('email')


class TweetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tweet

    user = factory.SubFactory(UserFactory)
    body = factory.Faker('text', max_nb_chars=140)
