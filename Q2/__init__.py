from otree.api import *
import json


class C(BaseConstants):
    NAME_IN_URL = "Q2"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    report1_1 = models.IntegerField(
        label="レポート1（要件の充足）",
        choices=[
            [18, "言う事無し18"],
            [17, "根拠未提示17"],
            [15, "分量不足15"],
            [14, "分量不足かつ根拠未提示14"],
            [0, "不適切0"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    report1_2 = models.IntegerField(
        label="レポート1（社会への応用例の記述）",
        choices=[
            [2, "言う事無し2"],
            [1, "説明不足1"],
            [0, "不適切0"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    report1_3 = models.BooleanField(
        label="レポート1（早期提出）",
        widget=widgets.CheckboxInput,
        blank=True,
        initial=False,
    )
    report1_4 = models.BooleanField(
        label="レポート1（遅延提出）",
        widget=widgets.CheckboxInput,
        blank=True,
        initial=False,
    )

    report2_1 = models.IntegerField(
        label="レポート2（要件の充足）",
        choices=[
            [18, "言う事無し18"],
            [17, "根拠未提示17"],
            [15, "分量不足15"],
            [14, "分量不足かつ根拠未提示14"],
            [0, "不適切0"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    report2_2 = models.IntegerField(
        label="レポート2（社会への応用例の記述）",
        choices=[
            [2, "言う事無し2"],
            [1, "説明不足1"],
            [0, "不適切0"],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    checked = models.BooleanField(widget=widgets.RadioSelectHorizontal)


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = [
        "report1_1",
        "report1_2",
        "report1_3",
        "report1_4",
        "report2_1",
        "report2_2",
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
                {k: alldata[k] for k in sorted(alldata) if k.startswith("report")},
                indent=4,
            ),
        )

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.checked:
            return upcoming_apps[0]


page_sequence = [MyPage, Results]
