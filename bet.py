from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *

name = ''
age = 0
p1 = 0
p2 = 0
p3 = 0

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) 
        btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        txt = Label(text = txt_instruction)
        txt1 = Label(text = 'Возраст')
        v1 = TextInput()
        txt2 = Label(text = 'Введите имя')
        self.v2 = TextInput()
        btn.on_press = self.next
        l1 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height='30sp')
        l1.add_widget(txt1)
        l1.add_widget(v1)
        l2 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height='30sp')
        l2.add_widget(txt2)
        l2.add_widget(self.v2)
        mainL = BoxLayout(orientation='vertical')
        mainL.add_widget(txt)
        mainL.add_widget(l1)
        mainL.add_widget(l2)
        mainL.add_widget(btn)
        self.add_widget(mainL)
    def next(self):
            global name
            name = self.v2.text
            print(name)
            self.manager.transition.direction = 'left'                                    
            self.manager.current = 'second'
        
class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        txt3 = Label(text = txt_test1)
        txt1 = Label(text = 'Введите результат')
        v1 = TextInput()
        btn3 = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        l3 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height='30sp')
        l3.add_widget(txt1)
        l3.add_widget(v1)
        btn3.on_press = self.next2
        mainL2 = BoxLayout(orientation='vertical')
        mainL2.add_widget(txt3)
        mainL2.add_widget(l3)
        mainL2.add_widget(btn3)
        self.add_widget(mainL2)
    def next2(self):
        self.manager.transition.direction = 'left'                                    
        self.manager.current = 'three'


class ThreeScr(Screen):
    def __init__(self, name='three'):
        super().__init__(name=name)
        txt3 = Label(text = txt_test2)
        btn3 = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        l3 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height='30sp')
        btn3.on_press = self.next3
        mainL2 = BoxLayout(orientation='vertical')
        mainL2.add_widget(txt3)
        mainL2.add_widget(l3)
        mainL2.add_widget(btn3)
        self.add_widget(mainL2)
    def next3(self):
        self.manager.transition.direction = 'left'                                    
        self.manager.current = 'four'

class FourScr(Screen):
    def __init__(self, name='four'):
        super().__init__(name=name)
        btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        txt = Label(text = txt_test3)
        txt1 = Label(text = 'Результат:')
        v1 = TextInput()
        txt2 = Label(text = 'Результат после отдыха:')
        v2 = TextInput()
        btn.on_press = self.next
        l1 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height='30sp')
        l1.add_widget(txt1)
        l1.add_widget(v1)
        l2 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height='30sp')
        l2.add_widget(txt2)
        l2.add_widget(v2)
        mainL = BoxLayout(orientation='vertical')
        mainL.add_widget(txt)
        mainL.add_widget(l1)
        mainL.add_widget(l2)
        mainL.add_widget(btn)
        self.add_widget(mainL)
    def next(self):
            self.manager.transition.direction = 'left'                                    
            self.manager.current = 'fife'

class FifeScr(Screen):
    def __init__(self, name='fife'):
        super().__init__(name=name)
        txt = Label(text = 'bla bla bla')
        l1 = BoxLayout(orientation='horizontal', size_hint=(0.8, None), height='30sp')
        l1.add_widget(txt)
        mainL = BoxLayout(orientation='vertical')
        mainL.add_widget(l1)






class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThreeScr())
        sm.add_widget(FourScr())
        sm.add_widget(FifeScr())
        return sm

app = MyApp()
app.run()
