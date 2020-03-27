from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from otree.models import Session
from django.shortcuts import render
import json
from captcha.fields import ReCaptchaField
from django.conf import settings

class Instructions1(Page):
    form_model = 'player'
    form_fields = ['captcha']

    def get_form(self, data=None, files=None, **kwargs):
        frm = super().get_form(data, files, **kwargs)
        if not settings.DEBUG:
            frm.fields['captcha'] = ReCaptchaField(label='')
        return frm

    def vars_for_template(self) -> dict:
        return {
            'debug': settings.DEBUG
        }


class ExampleSituation(Page):
    pass


class ExampleSituationCont(Page):
    pass


class FinalInstructions(Page):
    def vars_for_template(self) -> dict:
        return {
            'participation_fee': self.session.config['participation_fee']
        }


class Decisions(Page):
    form_model = "player"
    form_fields = [
        "decision10_0",
        "decision9_1",
        "decision8_2",
        "decision7_3",
        "decision6_4",
        "decision5_5",
        "decision4_6",
        "decision3_7",
        "decision2_8",
        "decision1_9",
        "decision0_10"
    ]

    def js_vars(self):
        return {
            'decision_order': json.loads(self.player.decision_order),
            'treatment': self.player.treatment
        }


class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'field_of_study']

    def error_message(self, input_values):
        if input_values['education'] >= 3 and not input_values['field_of_study']:
            return "Please provide your field of study."

    def before_next_page(self):
        self.player.prepare_data_for_analysis()


class LastPage(Page):
    def vars_for_template(self) -> dict:
        return {
            'participation_fee': self.session.config['participation_fee']
        }

    def before_next_page(self):
        if self.participant._is_bot and self.player.id_in_group == len(self.subsession.get_players()):
            self.subsession.determine_modal_responses()
            self.subsession.set_payoffs()


# custom payment processing
# don't include these in page_sequence
def payments_link(request):
    return render(request, 'kwtask/PaymentProcessing.html')


def process_payments(request, session_code):
    # get the current session by session_code
    sessions = Session.objects.filter(code=session_code)

    subsessions = sessions[0].get_subsessions()
    subsessions[0].determine_modal_responses()
    subsessions[0].set_payoffs()

    return render(request, 'kwtask/PaymentComplete.html')


page_sequence = [
    Instructions1,
    ExampleSituation,
    ExampleSituationCont,
    FinalInstructions,
    Decisions,
    Questionnaire,
    LastPage
]
