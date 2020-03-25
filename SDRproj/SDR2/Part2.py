#Part2
from manimlib.imports import *

class part2(Scene):
    def construct(self):
        text1 = TextMobject("前置知识要求:").scale(1)
        text2 = TextMobject("三角函数知识").scale(0.7)
        text3 = TextMobject("幂指数乘法").scale(0.7)
        text4 = TextMobject("死记硬背的能力").scale(0.7)

        #squa.surround(text1)
        text2.shift(UP)
        text3.next_to(text2, DOWN)
        text4.next_to(text3, DOWN)

        recta = Rectangle()

        self.play(ShowCreationThenFadeOut(recta), Write(text1))
        self.wait(0.5)
        self.play(text1.scale, 0.9, text1.move_to, UP*2)
        self.play(Write(text2), Write(text3), Write(text4))

        self.wait(1)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3), FadeOut(text4))