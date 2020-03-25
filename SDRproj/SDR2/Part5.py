#Part5
from manimlib.imports import *

class part5(Scene):
    def construct(self):
        axis_config={
            "stroke_color": WHITE, #坐标轴颜色
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
        freq_value = DecimalNumber(0, num_decimal_places=2, color=BLUE)
        omega_value = DecimalNumber(0, num_decimal_places=2, color=BLUE)

        #实例化主坐标轴对象
        cp_scale = 2.
        cp = ComplexPlane(axis_config=axis_config,\
            background_line_style=background_line_style)\
            .scale(cp_scale)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5)
        cp.add_coordinates(1j, 2j, 3j, -1j, -2j, -3j)

        #小坐标轴创建与移动
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

        arr_f = Arrow(cp.n2p(0), cp.n2p(0.5j), buff=0, color=YELLOW)#表征频域单位冲激的箭头
        arr_f.shift(cp.n2p(1.2j)+cp.n2p(2.))#放到小坐标轴原点

        #添加小坐标轴右侧的相关文字与参数
        freq_text = TextMobject('频率=', color=WHITE).scale(0.7).next_to(w_axes, DOWN * 0.7)
        freq_value = freq_value     #无意义，仅作提示用，定义在最上方
        freq_value.next_to(freq_text, RIGHT * 0.5).scale(0.7)
        hz_text = TextMobject('Hz').next_to(freq_value, RIGHT * 0.7).scale(0.7)
        #小坐标轴文字参数添加完毕
        freq_value.add_updater(lambda v: v.set_value(5*(cp.p2n(arr_f.get_center() ).real - 2.0) ) )#坐标等效换算

        text1 = TextMobject('幅度')
        text1.scale(0.7)
        text1.move_to(cp.n2p(0.25+1.5j))

        text2 = TextMobject('评论区会有关于频谱的补充说明\\\\建议观众在视频结束后进行查看', color = BLUE_B)
        text2.scale(0.5)
        text2.move_to(cp.n2p(-0.5j))

        arr_a = Arrow(cp.n2p(-0.12j), cp.n2p(1.5j), color = WHITE, stroke_width = 2)

        #添加衔接动画，后期达芬奇剪辑所用
        arr_f.shift(cp.n2p(1)/5) #移动到上一幕结束的位置
        self.add(w_axes, freq_text, freq_value, hz_text)#添加小坐标轴，以及小坐标轴相关的内容参数
        self.add(arr_f)#添加频域冲激箭头
        self.wait(3)
        self.play(FadeOut(freq_text), FadeOut(freq_value), FadeOut(hz_text))


        self.play(w_axes.shift, cp.n2p(-2-1.2j), arr_f.shift, cp.n2p(-2-1.2j))
        self.play(FadeInFromDown(arr_a))
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(10)