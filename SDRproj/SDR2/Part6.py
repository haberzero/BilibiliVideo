#Part6
from manimlib.imports import *

class part6(Scene):
    def construct(self):
        text1 = TextMobject('$Acos(2\\pi ft)$').scale(1.5)
        text2 = TextMobject('A表示电压幅度').scale(0.8)
        text3 = TextMobject('f表示信号频率').scale(0.8)

        text1.shift(UP*0.5)
        text2.next_to(text1, DOWN*1.5)
        text3.next_to(text2, DOWN*0.7)

        self.play(Write(text1))
        self.wait(1)
        self.play(FadeInFromDown(text2), FadeInFromDown(text3))
        self.wait(4)