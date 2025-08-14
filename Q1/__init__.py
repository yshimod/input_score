from otree.api import *
import json


class C(BaseConstants):
    NAME_IN_URL = "Q1"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.StringField()
    q2 = models.StringField()
    q3 = models.StringField()
    q4 = models.StringField()
    q5 = models.StringField()
    q6 = models.StringField()
    q7 = models.StringField()
    q8 = models.StringField()
    q9 = models.StringField()
    q10 = models.StringField()

    checked = models.BooleanField(widget=widgets.RadioSelectHorizontal)


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = [
        "q1",
        "q2",
        "q3",
        "q4",
        "q5",
        "q6",
        "q7",
        "q8",
        "q9",
        "q10",
    ]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            label=player.participant.label,
        )


class Results(Page):
    form_model = "player"
    form_fields = ["checked"]

    @staticmethod
    def vars_for_template(player: Player):
        alldata = dict(vars(player))
        return dict(
            label=player.participant.label,
            alldata=alldata,
            data=json.dumps(
                {k: alldata[k] for k in sorted(alldata) if k.startswith("q")}, indent=4
            ),
        )

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.checked:
            return upcoming_apps[0]


page_sequence = [MyPage, Results]
