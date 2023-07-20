from dino_runner.utils.constants import PARTYHAT, PARTYHAT_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Partyhat(PowerUp):
    def __init__(self):
        self.image = PARTYHAT
        self.type = PARTYHAT_TYPE
        super().__init__(self.image, self.type)
