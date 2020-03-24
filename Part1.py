#Part1
from manimlib.imports import *

class part1(Scene):
    def construct(self):
        topic = TextMobject("带你走进SDR的世界",Color = WHITE).scale(1.8)
        topic.shift(UP*2)

        subtitle1 = TextMobject("Chapter – 2.1",Color = WHITE).scale(0.8)
        subtitle1.shift(DOWN*0.5)

        subtitle2 = TextMobject("用高中数学理解正交解调",Color = WHITE).scale(0.9)
        subtitle2.shift(DOWN*2)

        self.play(Write(topic,run_time = 2))
        self.wait(1)
        self.play(Write(subtitle1,run_time = 2),Write(subtitle2,run_time = 2))
        self.wait(4)
        self.play(FadeOut(topic),FadeOut(subtitle1),FadeOut(subtitle2))