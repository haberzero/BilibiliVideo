#Part12
from manimlib.imports import *

class part12(GraphScene):
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

        text_1 = TextMobject('$e^{j\\omega t} = cos(\\omega t) + jsin(\\omega t)$').scale(0.7)
        text_1.move_to(LEFT*2.5+UP*1.5)

        text_2 = TextMobject('$(e^{j\\omega _h t}$').scale(0.7)#用来演示高频复信号
        text_3 = TextMobject('$\\sum {e^{j\\omega _n t}}$').scale(0.7)#用来演示基带信号

        text_sym_1 = TextMobject('$*$').scale(0.7)

        rectan = Rectangle(height = 0.5, width = 1.5)
        rectan.move_to(LEFT*1.1+UP*1.5)

        curve_1 = lambda x : abs(1 + 2*x - 1*(x**2) - 2*(x**3))
        graph_cur_1 = self.get_graph(curve_1, x_min=-1, x_max=1, color=BLUE)
        graph_cur_2 = self.get_graph(curve_1, x_min=-1, x_max=1, color=BLUE).flip()#翻转
        graph_cur_2.shift(LEFT*2.5)

        arr1 = Arrow(LEFT*2.5, LEFT*2.5+UP, color = BLUE_D).scale(2).shift(DOWN)
        arr2 = Arrow(RIGHT*2.5, RIGHT*2.5+UP, color = BLUE_D).scale(2).shift(DOWN)

        text_w1 = TextMobject('$-\\omega _h$', color = BLUE_A).scale(0.8).next_to(arr1,DOWN*0.6)
        text_w2 = TextMobject('$\\omega _h$', color = BLUE_A).scale(0.8).next_to(arr2,DOWN*0.6)

        self.add(text_1)#衔接
        self.add(text_w1, text_w2)

        self.play(ShowCreation(graph_cur_1))
        self.wait(5)
        self.play(FadeInFromDown(arr2))
        self.wait(3)
        self.play(graph_cur_1.shift, RIGHT*2.5, FadeOut(arr2))
        self.wait(10)
        self.play(TransformFromCopy(graph_cur_1, graph_cur_2))
        self.wait(8)
        self.play(ShowCreationThenFadeOut(rectan))
        self.wait(8)
        self.play(FadeOut(graph_cur_2),FadeOut(graph_cur_1))
        self.wait(4)

        #还没有渲染，之后处理
