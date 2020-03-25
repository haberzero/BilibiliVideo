#Part8
from manimlib.imports import *

class part8(Scene):
    def construct(self):
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

#过程中所用变量
        d_theta = TAU/30    #仅在30帧状况下是正确的，可以让箭头每秒旋转一圈

#实例化主坐标轴对象
        cp_scale = 2.
        cp = ComplexPlane(axis_config=axis_config,\
            background_line_style=background_line_style)\
            .scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

#小坐标轴创建与移动
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
        #freq_value.add_updater(lambda v: v.set_value(5*(cp.p2n(arr_f.get_center() ).real - 2.0) ) )

#旋转矢量与频域冲激信号
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

        ##旋转方向相反的矢量和相应的冲激表达
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

#公式文本创建
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

        text_sum1 = TextMobject('$\\sum {e^{jw_{n}t}}$').scale(1)
        text_sum1.shift(RIGHT+DOWN*1.5)

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
        ##最终效果't1 + t2 + t3 + t4'
        text_sym_4.next_to(text_n1[3], RIGHT*0.5)
        text_sym_5.next_to(text_n2[3], RIGHT*0.5)
        text_sym_6.next_to(text_n3[3], RIGHT*0.5)
        ##三个省略号

        t_group1 = Group(text_n1[0], text_n1[1], text_n1[2], text_n1[3], text_sym_1[0], text_sym_1[1], text_sym_1[2], text_sym_1[3], text_sym_4)
        t_group2 = Group(text_n2[0], text_n2[1], text_n2[2], text_n2[3], text_sym_2[0], text_sym_2[1], text_sym_2[2], text_sym_2[3])
        t_group3 = Group(text_n3[0], text_n3[1], text_n3[2], text_n3[3], text_sym_3[0], text_sym_3[1], text_sym_3[2], text_sym_3[3])

        t_group_tmp = Group(t_group1, t_group2)

#动画播放
        self.play(ShowCreation(cp,run_time = 4))#添加主坐标轴
        self.play(FadeIn(w_axes))#添加小坐标轴，以及小坐标轴相关的内容参数
        self.wait(0.5)

        self.play(FadeIn(arr_f0), FadeIn(arr0), )
        self.play(FadeIn(text_n1[0]))
        self.wait(0.2)

        self.play(FadeIn(arr_f1), FadeIn(arr1))
        self.play(FadeIn(text_n1[1]), FadeIn(text_sym_1[0]))
        self.wait(0.2)

        self.play(FadeIn(arr_f2), FadeIn(arr2))
        self.play(FadeIn(text_n1[2]), FadeIn(text_sym_1[1]))
        self.wait(0.2)

        self.play(FadeIn(arr_f3), FadeIn(arr3))
        self.play(FadeIn(text_n1[3]), FadeIn(text_sym_1[2]))
        self.wait(0.2)
        self.play(FadeIn(text_sym_4))

        #self.play(FadeIn(t_group2), FadeIn(arr0_r), FadeIn(arr1_r), FadeIn(arr2_r), FadeIn(arr3_r))
        #self.play(Transform(t_group_tmp, t_group3))
        self.wait(1)

        self.play(Transform(t_group1, text_sum1))

        self.wait(2)

        self.play(FadeOut(a_group), FadeOut(af_group), FadeOut(t_group1))
        #这里需要注意，虽然经过了transform方法，但是实例化的对象还是其本身，只是样式改变了，所以需要使用原本名命
        self.wait(3)