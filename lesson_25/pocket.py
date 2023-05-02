class Pocket:
    def __init__(self):
        self.stick = 0
        self.ball = 0

    def add_stick(self, count):
        self.stick += count

    def add_ball(self, count):
        self.ball += count

    def rasskazi_o_sebe(self):
        print(f"Во мне палочек : {self.stick} шт., шариков: {self.ball} шт.")