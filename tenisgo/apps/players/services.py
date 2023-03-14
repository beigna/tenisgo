from django.contrib.auth.models import User

from .models import Player


def player_create(
        email,
        first_name,
        last_name,
        birthdate,
        nationality,
        club) -> Player:

    user = User.objects.create_user(
        username=email,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )

    player = Player.objects.create(
        user=user,
        birthdate=birthdate,
        nationality=nationality,
        club=club,
    )

    return player
