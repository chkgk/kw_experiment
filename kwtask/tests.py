from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        likert_choices = [-1, -0.33, 0.33, 1]

        valid_questionnaire = {
            'age': random.randint(18, 60),
            'gender': random.choice(['male', 'female', 'other', 'I prefer not to tell']),
            'education': random.randint(1, 7),
            'field_of_study': random.choice(['economics', 'business', 'law', 'other']),
        }

        yield pages.Instructions1
        yield pages.ExampleSituation
        yield pages.ExampleSituationCont
        yield pages.FinalInstructions

        yield pages.Decisions, {
            "decision10_0": random.choice(likert_choices),
            "decision9_1": random.choice(likert_choices),
            "decision8_2": random.choice(likert_choices),
            "decision7_3": random.choice(likert_choices),
            "decision6_4": random.choice(likert_choices),
            "decision5_5": random.choice(likert_choices),
            "decision4_6": random.choice(likert_choices),
            "decision3_7": random.choice(likert_choices),
            "decision2_8": random.choice(likert_choices),
            "decision1_9": random.choice(likert_choices),
            "decision0_10": random.choice(likert_choices)
        }
        yield pages.Questionnaire, valid_questionnaire
        yield pages.LastPage