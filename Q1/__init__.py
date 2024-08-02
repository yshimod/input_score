from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = "Q1"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3

    # raw_score = list(range(0, 6))


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # q1_1 = models.IntegerField(choices=C.raw_score)
    # q1_2 = models.IntegerField(choices=C.raw_score)
    # q1_3 = models.IntegerField(choices=C.raw_score)
    # q1_4 = models.IntegerField(choices=C.raw_score)

    q1_1_1 = models.BooleanField(initial=False)
    q1_1_2 = models.BooleanField(initial=False)
    q1_1_3 = models.BooleanField(initial=False)
    q1_2_1 = models.BooleanField(initial=False)
    q1_2_2 = models.BooleanField(initial=False)
    q1_2_3 = models.BooleanField(initial=False)

    q2_1 = models.BooleanField(initial=False)
    q2_2 = models.BooleanField(initial=False)
    q2_3_ab = models.BooleanField(initial=False)
    q2_3_c = models.BooleanField(initial=False)
    q2_4 = models.BooleanField(initial=False)
    q2_5 = models.BooleanField(initial=False)

    q3_1 = models.BooleanField(initial=False)
    q3_2 = models.BooleanField(initial=False)
    q3_3 = models.BooleanField(initial=False)
    q3_4 = models.BooleanField(initial=False)

    checked = models.BooleanField(initial=False)


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = [
        "q1_1_1",
        "q1_1_2",
        "q1_1_3",
        "q1_2_1",
        "q1_2_2",
        "q1_2_3",
        "q2_1",
        "q2_2",
        "q2_3_ab",
        "q2_3_c",
        "q2_4",
        "q2_5",
        "q3_1",
        "q3_2",
        "q3_3",
        "q3_4",
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
