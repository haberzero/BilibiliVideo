#Part9
from manimlib.imports import *

class part9(GraphScene):
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
        self.setup_axes(animate=True)

        text_1 = TextMobject('$cos(\\omega _h t)$').scale(0.7)
        text_2 = TextMobject('$(e^{j\\omega _h t} + e^{-j\\omega _h t})$').scale(0.7)#用来演示高频正弦载波
        text_3 = TextMobject('$\\sum {cos(\\omega _n t)}$').scale(0.7)
        text_4 = TextMobject('$\\sum {e^{j\\omega _n t}}$').scale(0.7)#用来演示基带信号

        text_5 = TextMobject('$\\sum_n {e^{j(\\omega _n -\\omega _h) t}} + \\sum_n {e^{j(\\omega _n +\\omega _h) t}}$').scale(0.7)

        text_sym_1 = TextMobject('$*$').scale(0.7)
        text_sym_2 = TextMobject('$*$').scale(0.7)

        text_1.move_to(DOWN*2+LEFT)
        text_sym_1.next_to(text_1, RIGHT*0.5)
        text_3.next_to(text_sym_1, RIGHT*0.5)
        text_group_1 = Group(text_1, text_sym_1, text_3)#cos * cos

        text_2.move_to(DOWN*2+LEFT*0.5)
        text_sym_2.next_to(text_2, RIGHT*0.5)
        text_4.next_to(text_sym_2, RIGHT*0.5)#cos * cos
        text_group_2 = Group(text_2, text_sym_2, text_4)#ejwt * ejwt

        text_5.move_to(DOWN*2)

        curve_1 = lambda x : 1-x**2
        graph_cur_1 = self.get_graph(curve_1, x_min=-1, x_max=1, color=BLUE)

        curve_2 = lambda x : 1-x**2
        graph_cur_2 = self.get_graph(curve_2, x_min=-1, x_max=1, color=BLUE)

        arr1 = Arrow(LEFT*2.5, LEFT*2.5+UP, color = BLUE_D).scale(2).shift(DOWN)
        arr2 = Arrow(RIGHT*2.5, RIGHT*2.5+UP, color = BLUE_D).scale(2).shift(DOWN)

        text_w1 = TextMobject('$-\\omega _h$', color = BLUE_A).scale(0.8).next_to(arr1,DOWN*0.6)
        text_w2 = TextMobject('$\\omega _h$', color = BLUE_A).scale(0.8).next_to(arr2,DOWN*0.6)

        line1 = Line(LEFT*2.5, LEFT*2.5+UP, color = YELLOW_C).scale(2).shift(DOWN)
        line2 = Line(RIGHT*2.5, RIGHT*2.5+UP, color = YELLOW_C).scale(2).shift(DOWN)


        self.play(Write(text_1), FadeInFromDown(arr1), FadeInFromDown(arr2))
        self.play(FadeInFromDown(text_w1), FadeInFromDown(text_w2))
        self.play(Write(text_sym_1))
        self.play(Write(text_3), ShowCreation(graph_cur_1), ShowCreation(graph_cur_2))
        self.wait(2)

        self.play(Transform(text_group_1, text_group_2))
        self.wait(2)

        self.play(Transform(text_group_1, text_5))
        self.play(graph_cur_1.shift, LEFT*2.5, graph_cur_2.shift, RIGHT*2.5)
        self.play(FadeOut(arr1), FadeOut(arr2))
        self.wait(8)

        self.play(ShowCreationThenFadeOut(line1), ShowCreationThenFadeOut(line2))
        self.wait()
        self.play(ShowCreationThenFadeOut(line1), ShowCreationThenFadeOut(line2))
        self.wait(2)
        self.play(FadeOut(graph_cur_1), FadeOut(graph_cur_2))
