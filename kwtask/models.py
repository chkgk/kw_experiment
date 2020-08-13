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
import random
import json

author = 'Christian König gen. Kersting'

doc = """
Krupka & Weber (2013) Task.
"""


class Constants(BaseConstants):
    name_in_url = 'kwtask'
    players_per_group = None
    num_rounds = 1

    bonus = c(0.75)
    decision_list = ["10_0", "9_1", "8_2", "7_3", "6_4", "5_5", "4_6", "3_7", "2_8", "1_9", "0_10"]

    economics_expressions = [
        "economist", "economics", "economy", "economic", "econ"
    ]


class Subsession(BaseSubsession):
    modal10_0 = models.StringField()
    modal9_1 = models.StringField()
    modal8_2 = models.StringField()
    modal7_3 = models.StringField()
    modal6_4 = models.StringField()
    modal5_5 = models.StringField()
    modal4_6 = models.StringField()
    modal3_7 = models.StringField()
    modal2_8 = models.StringField()
    modal1_9 = models.StringField()
    modal0_10 = models.StringField()

    def creating_session(self):
        treatment = self.session.config.get('treatment', 'original')
        for player in self.get_players():
            player.randomize_decision_order()
            player.set_treatment(treatment)

    def determine_modal_responses(self):
        players = self.get_players()

        for decision in Constants.decision_list:
            count = {
                'ia': 0,
                'sia': 0,
                'sa': 0,
                'a': 0
            }
            for player in players:
                response = player.get_response(decision)
                count['ia'] += (response == -1)
                count['sia'] += (response == -0.33)
                count['sa'] += (response == 0.33)
                count['a'] += (response == 1)

            modal = max(count, key=count.get)
            self.set_modal_response(decision, modal)


    def set_modal_response(self, decision, modal_response):
        if decision == "10_0":
            self.modal10_0 = modal_response
        elif decision == "9_1":
            self.modal9_1 = modal_response
        elif decision == "8_2":
            self.modal8_2 = modal_response
        elif decision == "7_3":
            self.modal7_3 = modal_response
        elif decision == "6_4":
            self.modal6_4 = modal_response
        elif decision == "5_5":
            self.modal5_5 = modal_response
        elif decision == "4_6":
            self.modal4_6 = modal_response
        elif decision == "3_7":
            self.modal3_7 = modal_response
        elif decision == "2_8":
            self.modal2_8 = modal_response
        elif decision == "1_9":
            self.modal1_9 = modal_response
        elif decision == "0_10":
            self.modal0_10 = modal_response

        self.save()

    def set_payoffs(self):
        for player in self.get_players():
            player.set_payoff()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    original = models.BooleanField(initial=False)
    always_remind = models.BooleanField(initial=False)
    never_remind  = models.BooleanField(initial=False)
    no_incentives = models.BooleanField(initial=False)
    incentives_only = models.BooleanField(initial=False)

    decision_order = models.StringField()

    captcha = models.CharField(blank=True)

    decision10_0 = models.FloatField()
    decision9_1 = models.FloatField()
    decision8_2 = models.FloatField()
    decision7_3 = models.FloatField()
    decision6_4 = models.FloatField()
    decision5_5 = models.FloatField()
    decision4_6 = models.FloatField()
    decision3_7 = models.FloatField()
    decision2_8 = models.FloatField()
    decision1_9 = models.FloatField()
    decision0_10 = models.FloatField()

    selected_decision = models.StringField()

    task_question = models.IntegerField(
        verbose_name="Which of the following two statements about your task is true?",
        widget=widgets.RadioSelect()
    )

    task_incentives = models.IntegerField(
        verbose_name="Which of the following three statements about payments is true?",
        widget=widgets.RadioSelect()
    )

    age = models.IntegerField(verbose_name="How old are you?", max=120, doc="Age.")
    gender = models.StringField(choices=["female", "male", "other", "I prefer not to tell"],
                                label="What is your gender?", doc="Gender.", widget=widgets.RadioSelectHorizontal)
    education = models.IntegerField(
        verbose_name="Which is the highest level of education you have attained?",
        doc="Education level.",
        choices=[
            (1, "some High School"),
            (2, "High School Graduate"),
            (3, "some College, no degree"),
            (4, "Associates degree"),
            (5, "Bachelor’s degree"),
            (6, "Master’s degree"),
            (7, "Doctorate degree")
        ],
        widget=widgets.RadioSelect
        )
    field_of_study = models.StringField(
        label="If you have at least some college education, what is/was your field of study?", blank=True,
        doc="Field of study.")

    # additional variables computed from inputs:
    female = models.BooleanField(doc="True if participant is female.")
    economist = models.BooleanField(doc="True if participant is an economist.")
    understood_task = models.BooleanField()
    understood_incentives = models.BooleanField()

    def task_question_choices(self):
        choices = [
            (0, "I was asked to give appropriateness ratings based on my own, personal beliefs."),
            (1, "I was asked to give appropriateness ratings based on what I thought most people would believe."),
        ]
        random.shuffle(choices)
        return choices

    def task_incentives_choices(self):
        choices = [
            (0, "My total payment for this study is independent of my responses."),
            (1, "My total payment for this study depends on my own, personal beliefs."),
            (2, "My total payment for this study depends on my ability to anticipate what most people believe.")
        ]
        random.shuffle(choices)
        return choices

    def randomize_decision_order(self):
        decision_list = Constants.decision_list.copy()
        random.shuffle(decision_list)
        self.decision_order = json.dumps(decision_list)

    def set_treatment(self, treatment):
        self.treatment = treatment

        if treatment == "original":
            self.original = True
        elif treatment == "always remind":
            self.always_remind = True
        elif treatment == "never remind":
            self.never_remind = True
        elif treatment == "no incentives":
            self.no_incentives = True
        elif treatment == "incentives only":
            self.incentives_only = True

        self.selected_decision = random.choice(Constants.decision_list)

    def get_response(self, decision):
        dec_map = {
            "10_0": self.decision10_0,
            "9_1": self.decision9_1,
            "8_2": self.decision8_2,
            "7_3": self.decision7_3,
            "6_4": self.decision6_4,
            "5_5": self.decision5_5,
            "4_6": self.decision4_6,
            "3_7": self.decision3_7,
            "2_8": self.decision2_8,
            "1_9": self.decision1_9,
            "0_10": self.decision0_10,
        }
        return dec_map[decision]

    def prepare_data_for_analysis(self):
        # female indicator
        if self.gender == "female":
            self.female = True
        else:
            self.female = False

        if self.field_of_study:
            if any(word in self.field_of_study.lower() for word in Constants.economics_expressions):
                self.economist = True
            else:
                self.economist = False
        else:
            self.economist = False

        if self.no_incentives:
            self.understood_task = self.task_question == 0
            self.understood_incentives = self.task_incentives == 0
        else:
            self.understood_task = self.task_question == 1
            self.understood_incentives = self.task_incentives == 2


    def set_payoff(self):
        if self.no_incentives:
            self.payoff = c(0)
            self.save()
            return

        label_to_value = {
            'ia': -1,
            'sia': -0.33,
            'sa': 0.33,
            'a': 1
        }

        dec_map = {
            "10_0": self.decision10_0,
            "9_1": self.decision9_1,
            "8_2": self.decision8_2,
            "7_3": self.decision7_3,
            "6_4": self.decision6_4,
            "5_5": self.decision5_5,
            "4_6": self.decision4_6,
            "3_7": self.decision3_7,
            "2_8": self.decision2_8,
            "1_9": self.decision1_9,
            "0_10": self.decision0_10,
        }

        modal_map = {
            "10_0": self.subsession.modal10_0,
            "9_1": self.subsession.modal9_1,
            "8_2": self.subsession.modal8_2,
            "7_3": self.subsession.modal7_3,
            "6_4": self.subsession.modal6_4,
            "5_5": self.subsession.modal5_5,
            "4_6": self.subsession.modal4_6,
            "3_7": self.subsession.modal3_7,
            "2_8": self.subsession.modal2_8,
            "1_9": self.subsession.modal1_9,
            "0_10": self.subsession.modal0_10,
        }

        if dec_map[self.selected_decision] == label_to_value[modal_map[self.selected_decision]]:
            self.payoff = Constants.bonus
        else:
            self.payoff = c(0)

        self.save()