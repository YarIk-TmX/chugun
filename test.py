from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (720, 400)
heo_class = ''
class two_slide(App):
    def build(self):
        main_l = BoxLayout(orientation='vertical')
        box1 = BoxLayout(orientation='horizontal')
        box2 = BoxLayout(orientation='horizontal')
        self.mainbutton = Button(
            text='class:', size_hint=(None, None),
            size=(250, 75), pos_hint={'center_x': .10, 'top': 1}
        )
        
        box1.add_widget(self.mainbutton)
        self.dropdown = DropDown()
        btn = Button(text='mag', size_hint_y=None, height=40)
        btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
        self.dropdown.add_widget(btn)
        btn1 = Button(text='druid', size_hint_y=None, height=40)
        btn1.bind(on_release=lambda btn1: self.dropdown.select(btn1.text))
        self.dropdown.add_widget(btn1)
        
        self.mainbutton.add_widget(self.dropdown)
        self.mainbutton.bind(on_release=self.dropdown.open)

#------------------------------------------------------2----------------------------------------------

        self.mainbutton3 = Button(
            text='class:', size_hint=(None, None),
            size=(250, 75), pos_hint={'center_x': .10, 'top': 1}
        )
        
        box2.add_widget(self.mainbutton3)
        self.dropdown = DropDown()
        

        
        self.mainbutton3.add_widget(self.dropdown)
        self.mainbutton3.bind(on_release=self.dropdown.open)

#-----------------------------------------------------------------------------------------------------
        self.mainbutton2 = Button(
            text='additional weapon', size_hint=(None, None),
            size=(250, 75), pos_hint={'center_x': .10, 'top': 1}
        )
        
        box2.add_widget(self.mainbutton2)
        self.dropdown = DropDown()
        btn2 = Button(text='shield', size_hint_y=None, height=40)
        btn2.bind(on_release=lambda btn2: self.dropdown.select(btn2.text))
        self.dropdown.add_widget(btn2)
        
        self.mainbutton2.add_widget(self.dropdown)
        self.mainbutton2.bind(on_release=self.dropdown.open)

#-----------------------------------------------------------------------------------------------------

        self.mainbutton1 = Button(
            text='armor:', size_hint=(None, None),
            size=(250, 75), pos_hint={'center_x': .10, 'top': 1}
        )
        
        box1.add_widget(self.mainbutton1)
        self.dropdown = DropDown()
        btn1 = Button(text='iron armor', size_hint_y=None, height=40)
        btn1.bind(on_release=lambda btn1: self.dropdown.select(btn1.text))
        self.dropdown.add_widget(btn1)
        
        self.mainbutton1.add_widget(self.dropdown)
        self.mainbutton1.bind(on_release=self.dropdown.open)

#-----------------------------------------------------------------------------------------------------

        self.dropdown.bind(on_select=self.test)
        main_l.add_widget(box1)
        main_l.add_widget(box2)
        return main_l

    def test(self, instnce, x):
        setattr(self.mainbutton,'text', x)
        test = x
        print(test)
        # if heo_class == 'mag':
        #     btn3 = Button(text='rabot', size_hint_y=None, height=40)
        #     btn3.bind(on_release=lambda btn3: self.dropdown.select(btn3.text))
        #     self.dropdown.add_widget(btn3)
        # else:
        #     btn3 = Button(text='mag', size_hint_y=None, height=40)
        #     btn3.bind(on_release=lambda btn3: self.dropdown.select(btn3.text))
        #     self.dropdown.add_widget(btn3)

class MyApp(App):
    def build(self):
        sm = two_slide()
        return sm

app = two_slide()
app.run()
