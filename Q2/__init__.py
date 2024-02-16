from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = "Q2"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3

    raw_score = list(range(0, 6))


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q2_1 = models.IntegerField(choices=C.raw_score)
    q2_2 = models.IntegerField(choices=C.raw_score)
    q2_3 = models.IntegerField(choices=C.raw_score)
    q2_4 = models.IntegerField(choices=C.raw_score)

    checked = models.BooleanField(initial=False)


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = [
        "q2_1",
        "q2_2",
        "q2_3",
        "q2_4",
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
        return dict(
            label=player.participant.label,
        )

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.checked:
            return upcoming_apps[-1]


page_sequence = [MyPage, Results]
