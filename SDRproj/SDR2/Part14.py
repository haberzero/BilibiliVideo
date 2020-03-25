#Part13
from manimlib.imports import *

class part14(Scene):
    def construct(self):
        I_Q_circuit = ImageMobject("C:\myself\jpg_png_file\circuit3.png")#一张图片，放在另一个文件夹
        I_Q_circuit.scale(1.5).move_to(UP*1.5)

        line_1 = Line(LEFT*3,RIGHT*3, color = YELLOW)
        line_1.move_to(I_Q_circuit.get_center())

        text_cossin = TextMobject('$cos(\\omega _0)cos(\\omega _h) - sin(\\omega _h)sin(\\omega _0)$').scale(0.8)
        text_cossin.move_to(DOWN*1.0)

        text_1 = TextMobject('$cos(\\omega _0)$', color = WHITE).scale(0.7)
        text_1.move_to(DOWN*2.5+LEFT*2.5)
        text_2 = TextMobject('$jsin(\\omega _0)$').scale(0.7)
        text_2.move_to(DOWN*2.5+LEFT*1)
        text_3 = TextMobject('$cos(\\omega _h)$').scale(0.7)
        text_3.move_to(DOWN*2.5+RIGHT*1)
        text_4 = TextMobject('$jsin(\\omega _h)$').scale(0.7)
        text_4.move_to(DOWN*2.5+RIGHT*2.5)

        text_5 = TextMobject('$e^{j(\\omega _0)}$').scale(0.7)
        text_5.move_to(DOWN*3+LEFT*2)
        text_6 = TextMobject('$e^{j(\\omega _h)}$').scale(0.7)
        text_6.move_to(DOWN*3+RIGHT*2)

        text_sym_1 = TextMobject('$+$').scale(0.7).next_to(text_1,RIGHT*0.1)
        text_sym_2 = TextMobject('$+$').scale(0.7).next_to(text_3,RIGHT*0.1)

        self.play(Write(text_cossin))
        self.wait(7)
        self.play(FadeIn(I_Q_circuit))
        self.wait(9)
        self.play(TransformFromCopy(text_cossin, text_1)\
            , TransformFromCopy(text_cossin, text_2)\
            , TransformFromCopy(text_cossin, text_3)\
            , TransformFromCopy(text_cossin, text_4))
        self.play(Write(text_sym_1), Write(text_sym_2))
        self.wait(5)
        self.play(Write(text_5), Write(text_6))
        self.wait(9)
        self.play(ShowCreationThenFadeOut(line_1))
        self.wait(10)