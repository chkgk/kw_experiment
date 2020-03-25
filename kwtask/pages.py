from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions1(Page):
    pass


class ExampleSituation(Page):
    pass


class ExampleSituationCont(Page):
    pass


class FinalInstructions(Page):
    def vars_for_template(self) -> dict:
        return {
            'participation_fee': self.session.config['participation_fee']
        }


class LastPage(Page):
    def vars_for_template(self) -> dict:
        return {
            'participation_fee': self.session.config['participation_fee']
        }


page_sequence = [
    Instructions1,
    ExampleSituation,
    ExampleSituationCont,
    FinalInstructions,
    LastPage
]
