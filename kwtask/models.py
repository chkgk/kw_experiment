from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Christian König gen. Kersting'

doc = """
Krupka & Weber (2013) Task.
"""


class Constants(BaseConstants):
    name_in_url = 'kwtask'
    players_per_group = None
    num_rounds = 1

    bonus = c(0.5)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
