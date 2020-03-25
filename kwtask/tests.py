from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Instructions1
        yield pages.ExampleSituation
        yield pages.ExampleSituationCont
        yield pages.FinalInstructions
        yield pages.LastPage
