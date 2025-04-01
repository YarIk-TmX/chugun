from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (720, 400)
test = ''
class two_slide(App):
    def build(self):
        box = BoxLayout(orientation='horizontal')

        self.mainbutton = Button(
            text='Drop Down Button', size_hint=(None, None),
            size=(250, 75), pos_hint={'center_x': .10, 'top': 1}
        )
        
        box.add_widget(self.mainbutton)
        dropdown = DropDown()
        for index in range(1, 11):    
            btn = Button(text='Button ' + str(index),
            size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        #box.add_widget(dropdown)
        
        self.mainbutton.add_widget(dropdown)
        self.mainbutton.bind(on_release=dropdown.open)
#-----------------------------------------------------------------------------------------------------

        self.mainbutton1 = Button(
            text='Drop Down Button', size_hint=(None, None),
            size=(250, 75), pos_hint={'center_x': .5, 'top': 1}
        )
        
        box.add_widget(self.mainbutton1)
        dropdown = DropDown()
        for index in range(1, 11):    
            btn = Button(text='Button ' + str(index),
            size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        #box.add_widget(dropdown)
        
        self.mainbutton1.add_widget(dropdown)
        self.mainbutton1.bind(on_release=dropdown.open)


        dropdown.bind(on_select=self.test)
        return box

    def test(self, instnce, x):
       setattr(self.mainbutton,'text', x)
       test = x
       print(test)
