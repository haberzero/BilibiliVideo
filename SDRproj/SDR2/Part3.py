#Part3
from manimlib.imports import *

class part3(Scene):
    def construct(self):
        axis_config={
            "stroke_color": YELLOW, #坐标轴颜色
            "stroke_width": 0,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLUE},
        }
        background_line_style={
            "stroke_width": 0,
        }

        #过程中所用变量
        d_theta = TAU/30    #仅在30帧状况下是正确的，可以让箭头每秒旋转一圈
        freq_value = DecimalNumber(0, num_decimal_places=2, color=BLUE)

        #建立主坐标轴
        cp_scale = 2.
        cp = ComplexPlane(axis_config=axis_config,\
            background_line_style=background_line_style)\
            .scale(cp_scale)

        #放到后面去进行添加，需要配合视频内容显示出主坐标轴，目前暂且隐藏
        #cp.add_coordinates(0, 1, 2, 3, 4, -1, -2, -3, -4)
        #cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)
        #cp.set_stroke(stroke_width = 2)

        #此部分在创建一个独立的小坐标轴，刚创建时位置在原点附近
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
        #小坐标轴创建完毕
        #添加小坐标轴右侧的相关文字与参数
        freq_text = TextMobject('频率=', color=WHITE).scale(0.7).next_to(w_axes, DOWN * 0.7)
        freq_value = freq_value     #无意义，仅作提示用，定义在最上方
        freq_value.next_to(freq_text, RIGHT * 0.5).scale(0.7)
        hz_text = TextMobject('Hz').next_to(freq_value, RIGHT * 0.7).scale(0.7)
        #小坐标轴文字参数添加完毕

        arr_f = Arrow(cp.n2p(0), cp.n2p(0.5j), buff=0, color=YELLOW)#表征频域单位冲激的箭头
        arr_f.shift(cp.n2p(1.2j)+cp.n2p(2.))#放到小坐标轴原点

        freq_value.add_updater(lambda v: v.set_value(5*(cp.p2n(arr_f.get_center() ).real - 2.0) ) )    #坐标等效换算

        arr1 = Arrow(cp.n2p(0), cp.n2p(1), buff=0, color=BLUE_D)    #创建围绕原点旋转的箭头
        arr1.add_updater(lambda a, dt: a.rotate(d_theta * freq_value.get_value(), about_point=ORIGIN))   #目前仅知此写法是以帧时间为单位刷新，所以d_theta需要视情况更改
        ###同时标注说明一下：updater的传入函数中，第一个参数是实例化对象本身，这里就是 a 
        ###第二个参数dt如果添加，updater会随时间被调用，实时更新，实现图像自行转动。
        ###如果不加入第二个dt，updater被调用的方式就不是实时更新，而是跟随其它动态方法一起更新

        self.add(cp)#添加主坐标轴
        self.play(FadeIn(w_axes), FadeIn(freq_text), FadeIn(freq_value), FadeIn(hz_text) )#添加小坐标轴，以及小坐标轴相关的内容参数
        self.play(FadeInFromPoint(arr1, ORIGIN) )#添加旋转箭头
        self.play(FadeInFromDown(arr_f))#添加频域冲激箭头
        self.wait(1)

        self.play(arr_f.shift, cp.n2p(1)/5, run_time = 2)
        self.wait(8)
        self.play(arr_f.shift, cp.n2p(1.5)/5, run_time = 2)
        self.wait(2)
        self.play(arr_f.shift, cp.n2p(2.5)/5, run_time = 2)
        self.wait(1)
        self.play(arr_f.shift, cp.n2p(-6)/5, run_time = 2)
        self.wait(0.5)
        self.play(arr_f.shift, cp.n2p(-1.5)/5, run_time = 2)
        self.wait(4)
        #最后用达芬奇添加淡出关键帧，这里不再做效果