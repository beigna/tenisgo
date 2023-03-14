from django.core.exceptions import ValidationError
from django.db import models


class Match(models.Model):
    player_a = models.ForeignKey('players.Player',
                                 related_name='nosense_a',
                                 on_delete=models.CASCADE)
    player_b = models.ForeignKey('players.Player',
                                 related_name='nosense_b',
                                 on_delete=models.CASCADE)

    played_at = models.DateField()
    winner = models.ForeignKey('players.Player',
                               related_name='matches_won',
                               on_delete=models.CASCADE,
                               blank=True, null=True)
    loser = models.ForeignKey('players.Player',
                              related_name='matches_lost',
                              on_delete=models.CASCADE,
                              blank=True, null=True)

    def clean(self):
        if self.winner and self.looser:
            if self.winner == self.looser:
                raise ValidationError(
                    'No puede ganar y perder el mismo ñato al mismo tiempo'
                )

            if self.winner not in (self.player_a, self.player_b):
                raise ValidationError('El ganador debe ser del partido')

            if self.loser not in (self.player_a, self.player_b):
                raise ValidationError('El perdedor debe ser del partido')


class Set(models.Model):
    match = models.ForeignKey('matches.Match', on_delete=models.CASCADE)
    order = models.SmalIntegerField(default=0)

    is_tie_break = models.BooleanField(default=False)
    score_a = models.SmalIntegerField(default=0)
    score_b = models.SmalIntegerField(default=0)
