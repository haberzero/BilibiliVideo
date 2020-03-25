#Part7
from manimlib.imports import *

class part7(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "x_labeled_nums" :None,
        "x_axis_label": "频率",
        "y_min" : 0,
        "y_max" : 2,
        "y_axis_height": 2,
        "y_axis_label": "信号幅度",
        "axes_color": GREY,
        #"y_labeled_nums" :range(-4,6,2),
        "graph_origin" : ORIGIN
    }

    def construct(self):
        self.setup_axes(animate=True)
        
        arr1 = Arrow(LEFT, LEFT+UP, color = BLUE_D).scale(2)
        arr2 = Arrow(RIGHT, RIGHT+UP, color = BLUE_D).scale(2)

        text_f1 = TextMobject('$-f$', color = BLUE_A).scale(0.8).next_to(arr1,DOWN*0.5)
        text_f2 = TextMobject('$f$', color = BLUE_A).scale(0.8).next_to(arr2,DOWN*0.5)

        text_cos = TextMobject('$Acos(2\\pi ft)$').scale(0.7).move_to(LEFT*3+UP*2)

        self.play(Write(text_cos))
        self.play(FadeInFromDown(arr1), FadeInFromDown(arr2), FadeInFromDown(text_f1), FadeInFromDown(text_f2))
        self.wait(6)
