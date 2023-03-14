import pytest
from datetime import datetime
from django.utils import timezone

from freezegun import freeze_time

from players.models import Player, User
from players.services import player_create


@pytest.mark.django_db
@freeze_time('2023-03-13')
def test_player_create_success():
    bday = datetime(1984, 9, 28)

    new_player = player_create(
        email='test@test.com',
        first_name='Juan',
        last_name='Romero',
        birthdate=bday.date(),
        nationality='Argentina',
        club='CAFA',
    )

    assert isinstance(new_player, Player)
    assert isinstance(new_player.user, User)

    created_player = Player.objects.first()
    assert created_player.user.email == 'test@test.com'
    assert created_player.birthdate == bday.date()
    assert created_player.nationality == 'Argentina'
    assert created_player.club == 'CAFA'


    assert created_player.full_name == 'Juan Romero'
    assert created_player.age == 38
