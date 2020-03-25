#Part13
from manimlib.imports import *

class part13(GraphScene):
    CONFIG = {
        "x_min": -4,
        "x_max": 4,
        "x_axis_width": 8,
        "x_labeled_nums" :None,
        "x_axis_label": "$f$",
        "y_min" : 0,
        "y_max" : 4,
        "y_axis_height": 4,
        "y_labeled_nums" :None,
        "y_axis_label": "$A$",
        "graph_origin" : ORIGIN + DOWN,
        "axes_color": WHITE,
    }

    def construct(self):
        self.setup_axes(animate=False)

        # text_1 = TextMobject('$e^{j\\omega t} = cos(\\omega t) + jsin(\\omega t)$').scale(0.7)
        # text_1.move_to(LEFT*2.5+UP*1.5)

        # text_2 = TextMobject('$(e^{j\\omega _h t}$').scale(0.7)
        # text_3 = TextMobject('$\\sum {e^{j\\omega _n t}}$').scale(0.7)

        # text_sym_1 = TextMobject('$*$').scale(0.7)

        arr1 = Arrow(LEFT*3, LEFT*3+UP, color = YELLOW).scale(2).shift(DOWN)#表征左侧基带正弦信号
        arr2 = Arrow(RIGHT*0.5, RIGHT*0.5+UP, color = YELLOW).scale(2).shift(DOWN)#表征基带正弦信号

        arr3 = Arrow(LEFT*2.5, LEFT*2.5+UP, color = BLUE_D).scale(2).shift(DOWN)#保留着给text_w1文本定位用
        arr4 = Arrow(RIGHT*2.5, RIGHT*2.5+UP, color = BLUE_D).scale(2).shift(DOWN)

        text_1 = TextMobject('$e^{j\\omega _0 t}$').scale(0.7)
        text_2 = TextMobject('$e^{j\\omega _h t}$').scale(0.7)
        text_sym_1 = TextMobject('$*$').scale(0.7)

        text_1.move_to(DOWN*2+LEFT)
        text_sym_1.next_to(text_1, RIGHT*0.5)
        text_2.next_to(text_sym_1, RIGHT*0.5)
        text_group_1 = Group(text_1, text_sym_1, text_2)

        text_3 = TextMobject('$e^{j-\\omega _0 t}$').scale(0.7)
        text_4 = TextMobject('$e^{j-\\omega _h t}$').scale(0.7)
        text_sym_2 = TextMobject('$*$').scale(0.7)

        text_3.move_to(DOWN*2.5+LEFT)
        text_sym_2.next_to(text_3, RIGHT*0.5)
        text_4.next_to(text_sym_2, RIGHT*0.5)
        text_group_2 = Group(text_3, text_sym_2, text_4)

        text_5 = TextMobject('$e^{j(\\omega _0 + \\omega _h)t}$').scale(0.7).move_to(DOWN*2)
        text_6 = TextMobject('$e^{j-(\\omega _0 + \\omega _h)t}$').scale(0.7).move_to(DOWN*2.5)

        text_group_tmp = Group(text_group_1, text_group_2)

        text_cos = TextMobject('$cos(\\omega _0 + \\omega _h)$').scale(0.7)
        text_cos.move_to(DOWN*2.25)

        text_cossin = TextMobject('$cos(\\omega _0)cos(\\omega _h) - sin(\\omega _h)sin(\\omega _0)$')
        text_cossin.scale(0.7).move_to(DOWN*2.25)

        text_w1 = TextMobject('$-\\omega _h$', color = BLUE_A).scale(0.8).next_to(arr3,DOWN*0.6)
        text_w2 = TextMobject('$\\omega _h$', color = BLUE_A).scale(0.8).next_to(arr4,DOWN*0.6)

        self.add(text_1)#衔接
        self.add(text_w1, text_w2)

        self.play(ShowCreation(arr2), FadeIn(text_1))
        self.wait(1)
        self.play(Write(text_sym_1))
        self.wait(1)
        self.play(FadeInFromDown(arr4), FadeIn(text_2))#复信号部分显示完毕
        self.wait(2)
        self.play(Transform(text_group_1, text_5), arr2.shift, RIGHT*2.5, FadeOut(arr4))#移动并显示高频信号表达式
        self.wait(2)
        self.play(TransformFromCopy(arr2, arr1),  FadeIn(text_group_2))
        self.wait(1)
        self.play(Transform(text_group_2, text_6))
        self.wait(2)
        self.play(Transform(text_group_tmp, text_cos))
        self.wait(8)
        self.play(Transform(text_group_tmp, text_cossin))#Transform以后对象名并未改变
        self.wait(4)
