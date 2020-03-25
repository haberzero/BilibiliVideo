#Part8_1（上一个场景的内容过多所以添加一个
from manimlib.imports import *

class part8_1(GraphScene):
#######引入图像坐标轴，并且通过颜色设置将其隐藏
    CONFIG = {
        "x_min": -1,
        "x_max": 1,
        "x_axis_width": 1.6,
        "x_labeled_nums" :None,
        "x_axis_label": None,
        "y_min" : 0,
        "y_max" : 2,
        "y_axis_height": 2.4,
        "y_labeled_nums" :None,
        "y_axis_label": None,
        "graph_origin" : ORIGIN,
        "function1" : lambda x :np.cos(x),
        "axes_color": BLACK,
    }

#construct
    def construct(self):
#######CP坐标轴的参数设置与实例化
        axis_config={
            "stroke_color": WHITE, #坐标轴颜色
            "stroke_width": 2,  #正式显示出坐标轴所以将宽度设置为2
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLUE},
        }
        background_line_style={
            "stroke_width": 1,
            "stroke_opacity": 0.7,
        }

        cp_scale = 2.
        cp = ComplexPlane(axis_config=axis_config,\
            background_line_style=background_line_style)\
            .scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

#######过程中所用变量
        d_theta = TAU/30    #仅在30帧状况下是正确的，可以让箭头每秒旋转一圈

########小坐标轴创建与移动
        ###方便起见小坐标轴的创建直接借用了很大一部分群主Cigar666的代码，此处特别标注，表示感谢。
        c_line = Line(cp.n2p(-1.), cp.n2p(1.), stroke_width=4.5, stroke_color=WHITE)
        w_tick = VGroup()
        for i in range(1, 4):
            tick = Line(ORIGIN, UP * 0.12, color=WHITE, stroke_width=2.5).next_to(c_line, UP * 0.01).shift((i-2)*cp.n2p(1.))
            w_tick.add(tick)
        w_label_02 = TexMobject('-5', color=WHITE).scale(0.6).next_to(w_tick[0], DOWN * 0.4)
        w_label_03 = TexMobject('0', color=WHITE).scale(0.6).next_to(w_tick[1], DOWN * 0.4)
        w_label_04 = TexMobject('5', color=WHITE).scale(0.6).next_to(w_tick[2], DOWN * 0.4)
        w_label = VGroup(w_label_02, w_label_03, w_label_04)
        w_axes = VGroup(w_tick, w_label, c_line)    #把创建好的浮标line和创建好的Label文字绑定
        w_axes.shift(cp.n2p(1.2j)+cp.n2p(2.))#移动小坐标轴到右上方

#####旋转矢量与频谱冲激
        #freq_value.add_updater(lambda v: v.set_value(5*(cp.p2n(arr_f.get_center() ).real - 2.0) ) )

        arr_f0 = Arrow(cp.n2p(0), cp.n2p(0.7j), buff=0, color=YELLOW)#表征频域单位冲激的箭头
        arr_f0.shift(cp.n2p(1.2j)+cp.n2p(2.))#放到小坐标轴原点
        arr_f0.shift(cp.n2p(0.3)/5)

        arr_f1 = Arrow(cp.n2p(0), cp.n2p(0.5j), buff=0, color=YELLOW)
        arr_f1.shift(cp.n2p(1.2j)+cp.n2p(2.))
        arr_f1.shift(cp.n2p(0.9)/5)

        arr_f2 = Arrow(cp.n2p(0), cp.n2p(0.4j), buff=0, color=YELLOW)
        arr_f2.shift(cp.n2p(1.2j)+cp.n2p(2.))
        arr_f2.shift(cp.n2p(1.4)/5)

        arr_f3 = Arrow(cp.n2p(0), cp.n2p(0.2j), buff=0, color=YELLOW)
        arr_f3.shift(cp.n2p(1.2j)+cp.n2p(2.))
        arr_f3.shift(cp.n2p(2)/5)

        arr0 = Arrow(cp.n2p(0), cp.n2p(0.7), buff=0, color=BLUE_D)    #创建围绕原点旋转的箭头
        arr0.add_updater(lambda a, dt: a.rotate(d_theta * 0.3, about_point=ORIGIN))

        arr1 = Arrow(cp.n2p(0), cp.n2p(0.5), buff=0, color=BLUE_D)
        arr1.add_updater(lambda a, dt: a.rotate(d_theta * 0.9, about_point=ORIGIN))

        arr2 = Arrow(cp.n2p(0), cp.n2p(0.4), buff=0, color=BLUE_D)
        arr2.add_updater(lambda a, dt: a.rotate(d_theta * 1.4, about_point=ORIGIN))

        arr3 = Arrow(cp.n2p(0), cp.n2p(0.2), buff=0, color=BLUE_D)
        arr3.add_updater(lambda a, dt: a.rotate(d_theta * 2, about_point=ORIGIN))

        a_group = Group(arr0, arr1, arr2, arr3)
        af_group = Group(arr_f0, arr_f1, arr_f2, arr_f3)

        ##旋转方向相反的箭头和相应的冲激表达
        arr_f0_r = Arrow(cp.n2p(0), cp.n2p(0.7j), buff=0, color=RED_D)#表征频域单位冲激的箭头
        arr_f0_r.shift(cp.n2p(1.2j)+cp.n2p(2.))#放到小坐标轴原点
        arr_f0_r.shift(cp.n2p(-0.3)/5)

        arr_f1_r = Arrow(cp.n2p(0), cp.n2p(0.5j), buff=0, color=RED_D)
        arr_f1_r.shift(cp.n2p(1.2j)+cp.n2p(2.))
        arr_f1_r.shift(cp.n2p(-0.9)/5)

        arr_f2_r = Arrow(cp.n2p(0), cp.n2p(0.4j), buff=0, color=RED_D)
        arr_f2_r.shift(cp.n2p(1.2j)+cp.n2p(2.))
        arr_f2_r.shift(cp.n2p(-1.4)/5)

        arr_f3_r = Arrow(cp.n2p(0), cp.n2p(0.2j), buff=0, color=RED_D)
        arr_f3_r.shift(cp.n2p(1.2j)+cp.n2p(2.))
        arr_f3_r.shift(cp.n2p(-2)/5)

        arr0_r = Arrow(cp.n2p(0), cp.n2p(0.7), buff=0, color=TEAL_E)    #创建围绕原点旋转的箭头
        arr0_r.add_updater(lambda a, dt: a.rotate(-d_theta * 0.3, about_point=ORIGIN))

        arr1_r = Arrow(cp.n2p(0), cp.n2p(0.5), buff=0, color=TEAL_E)
        arr1_r.add_updater(lambda a, dt: a.rotate(-d_theta * 0.9, about_point=ORIGIN))

        arr2_r = Arrow(cp.n2p(0), cp.n2p(0.4), buff=0, color=TEAL_E)
        arr2_r.add_updater(lambda a, dt: a.rotate(-d_theta * 1.4, about_point=ORIGIN))

        arr3_r = Arrow(cp.n2p(0), cp.n2p(0.2), buff=0, color=TEAL_E)
        arr3_r.add_updater(lambda a, dt: a.rotate(-d_theta * 2, about_point=ORIGIN))

        a_group_r = Group(arr0_r, arr1_r, arr2_r, arr3_r)
        af_group_r = Group(arr_f0_r, arr_f1_r, arr_f2_r, arr_f3_r)

        ###标记：可能是由于写法错误或者个人理解有误等问题，如果使用list保存并创建这些箭头，
        ###就会出现所有箭头的转速都会变成最后一个箭头的转速的状况，不得已只能使用这种糟糕的方法来创建箭头
        ###目前在交流群内讨论结果是，估计是由于updater的实现原理，导致内部所有变量都会被记录，包括i
        ###于是最后的动画中，箭头的转速就同时还与 i 有关，这也能解释为何是在play方法生效前才会有转速变化

#########公式文本创建
        text_n1 = list()
        text_n2 = list()
        text_n3 = list()

        text_sym_1 = list()
        text_sym_2 = list()
        text_sym_3 = list()

        text_sym_4 = TextMobject('...')
        text_sym_5 = TextMobject('...')
        text_sym_6 = TextMobject('...')

        text_n1.append(TextMobject('$e^{j\\omega _{1}t}$').scale(0.7).shift(RIGHT+DOWN*1.5))
        text_n2.append(TextMobject('$e^{-j\\omega _{1}t}$').scale(0.7).shift(RIGHT+DOWN*2))
        text_n3.append(TextMobject('$cos(\\omega _{1}t)$').scale(0.5).shift(RIGHT*1.1+DOWN*2.5))

        text_sym_1.append(TextMobject('$+$').scale(0.7))
        text_sym_2.append(TextMobject('$+$').scale(0.7))
        text_sym_3.append(TextMobject('$+$').scale(0.7))

        text_sum3 = TextMobject('$\\sum {cos(\\omega t)}$').scale(0.8)
        text_sum3.shift(RIGHT*2+DOWN*1.5)

        for i in range(2,5):    #主要是为了下标
            text_n1.append(TextMobject('$e^{j\\omega _{%d}t}$'%i).scale(0.7))
            text_n2.append(TextMobject('$e^{-j\\omega _{%d}t}$'%i).scale(0.7))
            text_n3.append(TextMobject('$cos(\\omega_{%d} t)$'%i).scale(0.5))

            text_sym_1.append(TextMobject('$+$').scale(0.7))
            text_sym_2.append(TextMobject('$+$').scale(0.7))
            text_sym_3.append(TextMobject('$+$').scale(0.7))

        for i in range(1,4):
            text_sym_1[i-1].next_to(text_n1[i-1], RIGHT*0.4)
            text_sym_2[i-1].next_to(text_n2[i-1], RIGHT*0.4)
            text_sym_3[i-1].next_to(text_n3[i-1], RIGHT*0.4)

            text_n1[i].next_to(text_sym_1[i-1])
            text_n2[i].next_to(text_sym_2[i-1])
            text_n3[i].next_to(text_sym_3[i-1])
        ##最终效果大概是't1 + t2 + t3 + t4'
        text_sym_4.next_to(text_n1[3], RIGHT*0.5)
        text_sym_5.next_to(text_n2[3], RIGHT*0.5)
        text_sym_6.next_to(text_n3[3], RIGHT*0.5)
        ##三个省略号跟随在四个式子之后

        t_group1 = Group(text_n1[0], text_n1[1], text_n1[2], text_n1[3], text_sym_1[0], text_sym_1[1], text_sym_1[2], text_sym_1[3])
        t_group2 = Group(text_n2[0], text_n2[1], text_n2[2], text_n2[3], text_sym_2[0], text_sym_2[1], text_sym_2[2], text_sym_2[3])
        t_group3 = Group(text_n3[0], text_n3[1], text_n3[2], text_n3[3], text_sym_3[0], text_sym_3[1], text_sym_3[2], text_sym_3[3])

        t_group_tmp = Group(t_group1, t_group2)

        af_group_tmp = Group(af_group, af_group_r)

######建立GraphScene坐标轴并创建曲线
        self.setup_axes(animate=False)
        curve_1 = lambda x : 1-x**2
        graph_cur_1 = self.get_graph(curve_1)
        graph_cur_1.shift(cp.n2p(1.2j)+cp.n2p(2.))

#####################动画播放部分#########################
        self.add(cp)
        self.add(w_axes)

        self.play(FadeInFromPoint(a_group, ORIGIN, run_time = 2), FadeInFromDown(a_group_r, run_time = 2))
        self.play(FadeIn(af_group), FadeIn(af_group_r))
        self.play(FadeIn(t_group1), FadeIn(t_group2))
        self.wait(2)

        self.play(Transform(t_group_tmp, t_group3))
        self.wait(2)
        self.play(Transform(t_group_tmp, text_sum3), Transform(af_group_tmp, graph_cur_1))
        #self.play(FadeIn(graph_cur_1))
        self.wait(10)
        