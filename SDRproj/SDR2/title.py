#title
from manimlib.imports import *

class title(Scene):
    def construct(self):
        text_1 = TextMobject('用高中数学知识', color = WHITE).scale(1.5)
        text_1.move_to(UP)
        text_2 = TextMobject('理解正交调制').scale(1.5)
        text_2.move_to(DOWN*0.5)

        self.add(text_1)
        self.add(text_2)