from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

Window.size= (350,600)
Window.clearcolor = (247/255, 232/255, 222/255)


Builder.load_string("""
<StartScreen>:
    FloatLayout:
        size: 350,650

        Image:
            source: 'start_scr.png'
            pos:0,0

        Button:
            size_hint: 0.5, 0.1
            pos: 88,100
            on_press: root.manager.current = 'menu'

        Image:
            source: 'start.png'
            size_hint: 0.5, 0.1
            pos: 88,100


<MenuScreen>:
    FloatLayout:
        size: 350,650

        Image:
            source: 'menu.png'
            size_hint:1, None
            pos:0,500

        Button:
            text: "Рычаг"
            font_size: 25
            pos: 10,425
            size_hint:0.937,0.1
			background_color: (143/255, 185/255, 227/255, 1)
            background_normal: '000000'
            color: 0,0,0,1
            on_press: root.manager.current = 'teo'

        Image:
            source: 'arm.png'
            size_hint:0.937, None
            pos:10,405

        Button:
            text: 'Блок'
            font_size: 25
            pos: 10,350
            size_hint:0.937,0.1
			background_color: (143/255, 185/255, 227/255, 1)
            background_normal: '000000'
            color: 0,0,0,1

        Image:
            source: 'block.png'
            size_hint:0.937, None
            pos:10,330

        Button:
            text: 'Ворот'
            font_size: 25
            pos: 10,275
            size_hint:0.937,0.1
			background_color: (143/255, 185/255, 227/255, 1)
            background_normal: '000000'
            color: 0,0,0,1

        Image:
            source: 'vorot.png'
            size_hint:0.937, None
            pos:10,255

        Button:
            text: 'Клин'
            font_size: 25
            pos: 10,200
            size_hint:0.937,0.1
			background_color: (143/255, 185/255, 227/255, 1)
            background_normal: '000000'
            color: 0,0,0,1

        Image:
            source: 'klin.png'
            size_hint: 0.937, None
            pos:10, 180

        Button:
            text: 'Наклонная плоскость'
            font_size: 25
            pos: 10,125
            size_hint:0.937,0.1
			background_color: (143/255, 185/255, 227/255, 1)
            background_normal: '000000'
            color: 0,0,0,1

        Image:
            source: 'nakl.png'
            size_hint:0.937, None
            pos:10,105

        Button:
            text: 'Винт'
            font_size: 25
            pos: 10,50
            size_hint:0.937,0.1
			background_color: (143/255, 185/255, 227/255, 1)
            background_normal: '000000'
            color: 0,0,0,1

        Image:
            source: 'vint.png'
            size_hint:0.937, None
            pos:10,30

<InputScreen>:
    one: one
    one_sol:one_sol
    two:two
    two_sol:two_sol

    ScrollView:
        size_hint:1, None
        size: 350,600

    	FloatLayout:
            size: 350,1200
            size_hint:1, None

            FloatLayout:
                size: 350,600
                size_hint:1, None

        		Label:
        			canvas.before:
        				Color:
        					rgba: 143/255, 185/255, 227/255, 1
        				Rectangle:
        					pos: 0,1120
        					size: 350,80

        		Button:
        			font_size: 32
        			markup: True
        			text: '[b]Решение[/b]'
                    color: 0, 0, 0, 1
        			size_hint: (.3, 0.1)
        			pos: 220, 1120
                    background_normal: '000000'
                    background_down : '000000'
        			background_color: (143/255, 185/255, 227/255, 1)


        		Button:
        			font_size: 32
        			text: 'Теория'
        			color: 0, 0, 0, 1
        			size_hint: (.3, 0.1)
        			pos: 85, 1120
        			background_normal: '000000'
                    background_down : '000000'
        			background_color: (143/255, 185/255, 227/255, 1)

        			on_press: root.manager.current = 'teo'

                Button:
                    font_size: 20
        			text: 'Меню'
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 0, 1120
        			background_normal: '000000'
                    background_down : '000000'
        			background_color: (123/255, 145/255, 207/255, 1)

        			on_press: root.manager.current = 'menu'

                Image:
                    source: 'resh.png'
                    size_hint:1, None
                    pos:0,1110

        		Button:
        			font_size: 25
        			text: 'Рассчитать'
        			color: 0, 0, 0, 1
        			size_hint: (.5, 0.09)
        			pos: 90, 450
        			background_normal: '000000'
        			background_color: (143/255, 185/255, 227/255, 1)

        			on_press:
                        root.inp()

                Image:
                    source: 'rass.png'
                    size_hint:0.5, None
                    pos:90,427

                Image:
                    source: 'mfl.jpg'
                    size: self.texture_size
                    pos:0,700


        		Label:                   		    		 #ЛАБЕЛИ НАЧАЛО
                    text: 'Введите данные'
        			color: 0, 0, 0, 1
        			size_hint: (.5, 0.1)
        			pos: 40,830
        			font_size: 30

        		Label:
                    text: 'Программа посчитает недостающие данные'
        			color: 0, 0, 0, 1
        			size_hint: (.5, 0.1)
        			pos: 85,800
        			font_size: 15

        		Label:
        			markup: True
        			bold: True
                    text: 'F[size=15]1[/size]'
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 0, 770
        			font_size: 30

        		Label:
                    markup: True
        			bold: True
                    text: 'F[size=15]2[/size]'
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 0, 720
        			font_size: 30

        		Label:
                    markup: True
        			bold: True
                    text: 'l[size=15]1[/size]'
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 0, 670
        			font_size: 30

        		Label:
                    markup: True
        			bold: True
                    text: 'l[size=15]2[/size]'
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 0, 620
        			font_size: 30

        		Label:
                    markup: True
        			bold: True
                    text: 'M[size=15]1[/size]'
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 0, 570
        			font_size: 30

        		Label:
                    markup: True
        			bold: True
                    text: 'M[size=15]2[/size]'
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 0, 520
        			font_size: 30

        		Label:
                    markup: True
        			text:"="
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 45, 770
        			font_size: 30

        		Label:
                    markup: True
        			text:"="
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 45, 720
        			font_size: 30

        		Label:
                    markup: True
        			text:"="
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 45, 670
        			font_size: 30

        		Label:
                    markup: True
        			text:"="
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 45, 620
        			font_size: 30

        		Label:
                    markup: True
        			text:"="
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 45, 570
        			font_size: 30

        		Label:
                    markup: True
        			text:"="
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 45, 520
        			font_size: 30

        		Label:
                    markup: True
        			text:"Н"
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 195,770
        			font_size: 30

        		Label:
                    markup: True
        			text:"Н"
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 195, 720
        			font_size: 30

        		Label:
                    markup: True
        			text:"м"
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 195, 670
        			font_size: 30

        		Label:
                    markup: True
        			text:"м"
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 195, 620
        			font_size: 30

        		Label:
                    markup: True
        			text:"Н•м"
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 210, 570
        			font_size: 30

        		Label:
                    markup: True
        			text:"Н•м"
        			color: 0, 0, 0, 1
        			size_hint: (.2, 0.1)
        			pos: 210, 520
        			font_size: 30							#КОНЕЦ ЛАБЕЛЕЙ

        		TextInput:
                    id: F1							# INPUT
        			multiline: False
        			size_hint: (.22, None)
        			pos: 120, 780
        			height: 35
        			font_size: 19

        		TextInput:
                    id:F2
        			multiline: False
        			size_hint: (.22, None)
        			pos: 120, 730
        			height: 35
        			font_size: 19

        		TextInput:
                    id:l1
        			multiline: False
        			size_hint: (.22, None)
        			pos: 120, 680
        			height: 35
        			font_size: 19

        		TextInput:
                    id:l2
        			multiline: False
        			size_hint: (.22, None)
        			pos: 120, 630
        			height: 35
        			font_size: 19

        		TextInput:
                    id: M1
        			multiline: False
        			size_hint: (.22, None)
        			pos: 120, 580
        			height: 35
        			font_size: 19

        		TextInput:
                    id: M2
        			multiline: False
        			size_hint: (.22, None)
        			pos: 120, 530
        			height: 35
        			font_size: 19						#INPUT END


            FloatLayout:
                size:350,600
                size_hint:1, None
                Label:                                  #SOLUTION
                    markup:True
                    color: 0,0,0,1
                    font_size:30
                    pos: 0,350
                    size_hint:1, 0.05
                    text: "[b][i]Решение:[/i][/b]"

                Label:
                    id:one
                    markup:True
                    font_size: 25
                    text_size: 300,None
                    color: 0,0,0,1
                    pos: 10,230
                    size_hint:1, 0.1
                    text: "[b]1) [/b]"

                Label:
                    id: one_sol
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,250-self.height
                    size_hint:1, 0.1
                    text: ""

                Label:
                    id: two
                    markup:True
                    font_size: 25
                    text_size: 300,None
                    color: 0,0,0,1
                    pos: 10,110
                    size_hint:1, 0.1
                    text: "[b]2) [/b]"

                Label:
                    id: two_sol
                    font_size: 20
                    text_size: 300,None
                    color: 0,0,0,1
                    pos: 10,130-self.height
                    size_hint:1, 0.1
                    text: ""


<TheoryScreen>:
    ScrollView:
        size_hint:1, None
        size: 350,600

        FloatLayout:
            size_hint_y:None
            size: 350, 3600

            FloatLayout:
                size: 350,100
                size_hint_y:None

                Label:
                    canvas.before:
        				Color:
    				        rgba: 143/255, 185/255, 227/255, 1
        				Rectangle:
    				        pos: 0, 3520
    				        size: 350,80

                Button:
        			font_size: 32
                    markup: True
        			text: '[b]Теория[/b]'
        			color: 0, 0, 0, 1
        			size_hint: (.3, 0.6)
        			pos: 85, 3520
            		background_normal: '000000'
                    background_down : '000000'
        			background_color: (143/255, 185/255, 227/255, 1)

                Button:
                    font_size: 32
                    text: 'Решение'
                    color: 0, 0, 0, 1
                    size_hint: (.3, 0.6)
                    pos: 220, 3520
                    background_normal: '000000'
                    background_down : '000000'
                    background_color: (143/255, 185/255, 227/255, 1)

                    on_press: root.manager.current = 'inp'

                Button:
                    font_size: 20
            		text: 'Меню'
            		color: 0, 0, 0, 1
        			size_hint: (.2, 0.6)
        			pos: 0, 3520
        			background_normal: '000000'
                    background_down : '000000'
        			background_color: (123/255, 145/255, 207/255, 1)

        			on_press: root.manager.current = 'menu'

                Image:
                    source: 'teo.png'
                    size_hint:1, None
                    pos:0,3510

            FloatLayout:
                size_hint_y:None
                size: 350, 600

                Label:
                    markup: True
                    text:
                        "   [b]Простые механизмы[/b] – это устройства, с помощью которых работа совершается только за счет механической энергии."
                    text_size: 300, None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,3410
                    size_hint:1,0.1

                Label:
                    markup: True
                    text:
                        "   [b]Pычaг[/b] представляет собой балку, которая вращается вокруг точки опоры. Плечо рычага – это расстояние от точки опоры или подвеса рычага до точки приложения силы. Силы будем прикладывать перпендикулярно рычагу."
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,3230
                    size_hint:1,0.1

                Image:
                    source: 'opr.jpg'
                    size: self.texture_size
                    pos:0,2720

                Label:
                    markup: True
                    text:
                        "   [b]Правило равновесия рычага.[/b] Рычаг находится в равновесии тогда, когда силы, действующие на него, обратно пропорциональны плечам этих сил."
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,2765
                    size_hint:1,0.1

                Image:
                    source: 'ravn.jpg'
                    size: self.texture_size
                    pos:0,2290

                Label:
                    markup: True
                    text:
                        "   [b]Момент силы[/b] - произведение силы на плечо. Для определения физического смысла можно сказать, что момент - вращательное действие. M=F*l"
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,2330
                    size_hint:1,0.1

                Image:
                    source: 'mom.jpg'
                    size: self.texture_size
                    pos:0,1860

                Label:
                    markup: True
                    text:
                        "   [b]Как используют рычаг?[/b]"
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,1960
                    size_hint:1,0.1

                Label:
                    text:
                        "   Рычаг используется для получения большего усилия на коротком плече с помощью меньшего усилия на длинном плече (или для получения большего перемещения на длинном плече с помощью меньшего перемещения на коротком плече). Сделав плечо рычага достаточно длинным, теоретически, можно развить любое усилие."
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,1800
                    size_hint:1,0.1

                Image:
                    source: 'anim.gif'
                    size: self.texture_size
                    pos:0,1255


                Label:
                    markup: True
                    text:
                        "   [b]Типы рычагов[/b]"
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,1350
                    size_hint:1,0.1

                Label:
                    markup: True
                    text:
                        "   В рычагах [b]первого рода[/b] точка опоры расположена между точками приложения усилия и нагрузки. Например, ножницы или детские качели (перекладина)."
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,1265
                    size_hint:1,0.1

                Image:
                    source: 'kach.jpg'
                    size: self.texture_size
                    pos:0,800

                Label:
                    markup: True
                    text:
                        "   В рычагах [b]второго рода[/b] точка опоры и точка приложения усилия находятся на противоположных концах, а точка приложения нагрузки расположена между ними. Можно привести в пример тачку, где колесо является точкой опоры."
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,800
                    size_hint:1,0.1

                Image:
                    source: 'tach.jpg'
                    size: self.texture_size
                    pos:0,300

                Label:
                    markup: True
                    text:
                        "   В рычагах [b]третьего рода[/b] точка опоры и точка приложения нагрузки находятся на противоположных концах, а точка приложения усилия – между ними. Допустим, пинцет."
                    text_size: 300,None
                    color: 0,0,0,1
                    font_size:20
                    pos: 10,310
                    size_hint:1,0.1

                Image:
                    source: 'pin.jpg'
                    size: self.texture_size
                    pos:0,-185
""")

class StartScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class TheoryScreen(Screen):
    pass

class InputScreen(Screen):
    one=ObjectProperty()
    one_sol=ObjectProperty()
    two=ObjectProperty()
    two_sol=ObjectProperty()
    def inp(self):
        F1=self.ids['F1'].text
        F2=self.ids['F2'].text
        l1=self.ids['l1'].text
        l2=self.ids['l2'].text
        M1=self.ids['M1'].text
        M2=self.ids['M2'].text

        try:
            if len(F1)>0:
                F1=int(F1)
            else:
                F1=0

            if len(l1)>0:
                l1=int(l1)
            else:
                l1=0

            if len(M1)>0:
                M1=int(M1)
            else:
                M1=0
        except ValueError:
            self.one.text="[b]1) [/b]Введено некорректное значение"
            self.one_sol.text=""
        else:
            self.F1=F1
            self.l1=l1
            self.M1=M1
            self.one_text()

        try:
            if len(F2)>0:
                F2=int(F2)
            else:
                F2=0

            if len(l2)>0:
                l2=int(l2)
            else:
                l2=0

            if len(M2)>0:
                M2=int(M2)
            else:
                M2=0

        except ValueError:
            self.two.text="[b]2) [/b]Введено некорректное значение"
            self.two_sol.text=""
        else:
            self.F2=F2
            self.l2=l2
            self.M2=M2
            self.two_text()

    def mfl(self, F, l):
        M=F*l
        M=str(M)
        F=str(F)
        l=str(l)
        text_1="M = F*l"
        text_2="M = " + F + " * " + l + " = " + M + " Н•м"
        return (text_1, text_2)

    def fml(self, M, l):
        F=M/l
        M=str(M)
        F=str(F)
        l=str(l)
        text_1="[b]1) [/b]F = M/l"
        text_2="F = " + M + " / " + l + " = " + F + " H"
        return (text_1, text_2)

    def lmf(self, M, F):
        l=M/F
        M=str(M)
        F=str(F)
        l=str(l)
        text_1="[b]1) [/b]l = M/F"
        text_2="l = " + M + " / " + F + " = " + l + " м"
        return (text_1, text_2)

    def solution_1(self):
        if self.F1==0:
            if self.l1!=0 and self.M1!=0:
                self.sol_1=self.fml(self.M1, self.l1)
            else:
                self.sol_1=0

        elif self.l1==0:
            if self.F1!=0 and self.M1!=0:
                self.sol_1=self.lmf(self.M1, self.F1)
            else:
                self.sol_1=0
        elif self.M1==0:
            if self.l1!=0 and self.F1!=0:
                self.sol_1=self.mfl(self.F1, self.l1)
            else:
                self.sol_1=0

        elif self.F1!=0 and self.M1!=0 and self.l1!=0:
            self.sol_1=2

        return self.sol_1


    def solution_2(self):
        if self.F2==0:
            if self.l2!=0 and self.M2!=0:
                self.sol_2=self.fml(self.M2, self.l2)
            else:
                self.sol_2=0

        elif self.l2==0:
            if self.F2!=0 and self.M2!=0:
                self.sol_2=self.lmf(self.M2, self.F2)
            else:
                self.sol_2=0


        elif self.M2==0:
            if self.l2!=0 and self.F2!=0:
                self.sol_2=self.mfl(self.F2, self.l2)
            else:
                self.sol_2=0

        elif self.F2!=0 and self.M2!=0 and self.l2!=0:
            self.sol_2=2


        return self.sol_2

    def one_text(self):
        sol_1=self.solution_1()
        if sol_1==0:
            self.one.text="[b]1) [/b]Недостаточно данных"
            self.one_sol.text=""

        elif sol_1==2:
            self.one.text="[b]1) [/b]Все данные известны"
            self.one_sol.text=""

        else:
            self.one.text="[b]1) [/b]" + sol_1[0]
            self.one_sol.text=sol_1[1]

    def two_text(self):
        sol_2=self.solution_2()
        if sol_2==0:
            self.two.text="[b]2) [/b]Недостаточно данных"
            self.two_sol.text=""

        elif sol_2==2:
            self.two.text="[b]2) [/b]Все данные известны"
            self.two_sol.text=""

        else:
            self.two.text="[b]2) [/b]" + sol_2[0]
            self.two_sol.text=sol_2[1]

class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(InputScreen(name='inp'))
        sm.add_widget(TheoryScreen(name='teo'))

        return sm

if __name__ == '__main__':
    TestApp().run()