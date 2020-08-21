from otree.api import Submission
from . import pages
from ._builtin import Bot
import random

class PlayerBot(Bot):
    def play_round(self):
        # likert_choices = [-3, -2, -1, 1, 2, 3]
        weighted_choices = ['-3'] * 10 + ['-2'] * 15 + ['-1'] * 25 + 25 * ['1'] + 15 * ['2'] + 10 * ['3']

        valid_questionnaire = {
            'age': random.randint(18, 60),
            'gender': random.choice(['male', 'female', 'other', 'I prefer not to tell']),
            'education': random.randint(1, 7),
            'field_of_study': random.choice(['economics', 'business', 'law', 'other']),
        }

        valid_assessment = {
            'task_question': random.randint(0, 1),
            'task_incentives': random.randint(0, 2)
        }

        valid_comprehension = {
            'task': {
                'comprehension_task': 1 if self.player.no_conflict or self.player.second else 0
            },
            'incentives': {
                'comprehension_incentives': 0 if self.player.first or self.player.second else 2
            }
        }

        yield Submission(pages.Instructions1, {'captcha': 'a'}, check_html=False)
        yield pages.ExampleSituation, valid_comprehension['task']
        yield pages.ExampleSituationCont
        yield pages.FinalInstructions, valid_comprehension['incentives']

        yield pages.Decisions, {
            "decision10_0": random.choice(weighted_choices),
            "decision9_1": random.choice(weighted_choices),
            "decision8_2": random.choice(weighted_choices),
            "decision7_3": random.choice(weighted_choices),
            "decision6_4": random.choice(weighted_choices),
            "decision5_5": random.choice(weighted_choices),
            "decision4_6": random.choice(weighted_choices),
            "decision3_7": random.choice(weighted_choices),
            "decision2_8": random.choice(weighted_choices),
            "decision1_9": random.choice(weighted_choices),
            "decision0_10": random.choice(weighted_choices)
        }
        yield pages.Assessment, valid_assessment
        yield pages.Questionnaire, valid_questionnaire
        yield pages.LastPage
