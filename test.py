
from kivy.app import App
import sys
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (1300, 510)
heo_class = ''


class LinkedDropdowns(BoxLayout):
    def __init__(self, data: dict[str, list[str]], **kwargs):
        super().__init__(**kwargs)


        self.data = data


        self.orientation = 'horizontal'
        self.spacing = 100
        self.pos_hint = {'center_y': 1}

        self.grid1 = GridLayout()
        self.grid2 = GridLayout()

        self.grid1.rows = 2
        self.grid1.cols = 2

        self.grid2.rows = 2
        self.grid2.cols = 2

        self.grid1.spacing = [50, 100]
        self.grid2.spacing = [50, 100]
        self.grid1.size_hint = (0.5, 0.5)
        self.grid2.size_hint = (0.5, 0.5)


        self.main_button_1 = Button(text='класс', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))
        self.main_button_2 = Button(text='оружие', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))
        self.main_button_3 = Button(text='скиллы', size_hint=(None, None), size=(250, 50))
        self.main_button_4 = Button(text='скилл2', size_hint=(None, None), size=(250, 50))
        self.main_button_5 = Button(text='скилл3', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))
        self.main_button_6 = Button(text='скилл', size_hint=(None, None), size=(250, 50))

        self.grid1.add_widget(self.main_button_1)

        self.grid1.add_widget(self.main_button_2)
        self.grid2.add_widget(self.main_button_5)

        self.grid2.add_widget(self.main_button_3)
        self.grid2.add_widget(self.main_button_4)
        self.grid2.add_widget(self.main_button_6)
        
        self.add_widget(self.grid1)
        self.add_widget(self.grid2)


        self.dropdown_1 = DropDown()
        self.dropdown_2 = DropDown()
        self.dropdown_3 = DropDown()
        self.dropdown_4 = DropDown()
        self.dropdown_5 = DropDown()
        self.dropdown_6 = DropDown()



        for category in self.data:
            btn = Button(text=category, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_category(btn.text))
            self.dropdown_1.add_widget(btn)


        self.main_button_1.bind(on_release=self.dropdown_1.open)
        self.main_button_2.bind(on_release=self.open_second_dropdown)
        self.main_button_3.bind(on_release=self.open_third_dropdown)
        self.main_button_4.bind(on_release=self.open_four_dropdown)
        self.main_button_5.bind(on_release=self.open_fife_dropdown)
        self.main_button_6.bind(on_release=self.open_six_dropdown)

        
    
        
    def select_category(self, category):
        self.main_button_1.text = category
        self.dropdown_1.dismiss()
        self.populate_second_dropdown(self.data[category]['weapons'])
        self.populate_third_dropdown(self.data[category]['skills'])
        self.populate_four_dropdown(self.data[category]['skills'])
        self.populate_fife_dropdown(self.data[category]['skills'])
        self.populate_six_dropdown(self.data[category]['skills'])

#-----------------------------------------------------------------------------------------------------------------

    def populate_second_dropdown(self, options):
        self.dropdown_2.clear_widgets()
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_option(btn.text))
            self.dropdown_2.add_widget(btn)

    def populate_third_dropdown(self, options):
        self.dropdown_3.clear_widgets()
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_option3(btn.text))
            self.dropdown_3.add_widget(btn)

    def populate_four_dropdown(self, options):
        self.dropdown_4.clear_widgets()
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_option4(btn.text))
            self.dropdown_4.add_widget(btn)

    def populate_fife_dropdown(self, options):
        self.dropdown_5.clear_widgets()
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_option5(btn.text))
            self.dropdown_5.add_widget(btn)

    def populate_six_dropdown(self, options):
        self.dropdown_6.clear_widgets()
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_option6(btn.text))
            self.dropdown_6.add_widget(btn)

#-------------------------------------------------------------------------------------------------------------------

    def select_option(self, option):
        self.main_button_2.text = option
        self.dropdown_2.dismiss()
        
    def select_option3(self, option):
        self.main_button_3.text = option
        self.dropdown_3.dismiss()

    def select_option4(self, option):
        self.main_button_4.text = option
        self.dropdown_4.dismiss()

    def select_option5(self, option):
        self.main_button_5.text = option
        self.dropdown_5.dismiss()

    def select_option6(self, option):
        self.main_button_6.text = option
        self.dropdown_6.dismiss()    

#--------------------------------------------------------------------------------------------------------

    def open_second_dropdown(self, instance):
        if len(self.dropdown_2.children) > 0:
            self.dropdown_2.open(self.main_button_2)

    def open_third_dropdown(self, instance):
        if len(self.dropdown_3.children) > 0:
            self.dropdown_3.open(self.main_button_3)

    def open_four_dropdown(self, instance):
        if len(self.dropdown_4.children) > 0:
            self.dropdown_4.open(self.main_button_4)

    def open_fife_dropdown(self, instance):
        if len(self.dropdown_5.children) > 0:
            self.dropdown_5.open(self.main_button_5)

    def open_six_dropdown(self, instance):
        if len(self.dropdown_6.children) > 0:
            self.dropdown_6.open(self.main_button_6)

#_____________________________________________________________________________________________________________________

    def get_selection(self):
        return self.main_button_1.text, self.main_button_2.text
#-------------------------------------------------------2----------------------------------------------------------------
class LinkedDropdowns2(BoxLayout):
    def __init__(self, data: dict[str, list[str]], **kwargs):
        super().__init__(**kwargs)
        
        self.spacing = 50
        self.data = data


        self.main_button_1 = Button(text='упор на', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))
        self.main_button_2 = Button(text='инвентарь', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))


        self.add_widget(self.main_button_1)
        self.add_widget(self.main_button_2)


        self.dropdown_1 = DropDown()
        self.dropdown_2 = DropDown()


        for category in self.data:
            btn = Button(text=category, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_category(btn.text))
            self.dropdown_1.add_widget(btn)


        self.main_button_1.bind(on_release=self.dropdown_1.open)
        self.main_button_2.bind(on_release=self.open_second_dropdown)


    def select_category(self, category):
        self.main_button_1.text = category
        self.dropdown_1.dismiss()
        self.populate_second_dropdown(self.data[category])


    def populate_second_dropdown(self, options):
        self.dropdown_2.clear_widgets()
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.select_option(btn.text))
            self.dropdown_2.add_widget(btn)


    def select_option(self, option):
        self.main_button_2.text = option
        self.dropdown_2.dismiss()


    def open_second_dropdown(self, instance):
        if len(self.dropdown_2.children) > 0:
            self.dropdown_2.open(self.main_button_2)


    def get_selection(self):
        return self.main_button_1.text, self.main_button_2.text
#--------------------------------------------------------------------------------------------------------------------

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        data = {
            "маг": {
                'weapons': ["посох", "волшебная палочка", "магические перчатки"],
                'skills': ['yhrr', 'qwe', 'asd', 'zxc']
            },
            "друид":["посох","магический шар","ничего"],
            "паладин":["меч","двуручный меч","копье","алебарда","моргенштерн"],
            "некромант":["боевая коса"," отравленный кенжал","скытые клинки"],
            "варвар":["парные топоры","молот","двуручный топор", "кастеты"],
            "бард":["гитара","балалайка","укулеле","гусли"]
        }
        data2 = {
            "защита": ["железные поножи", "железный нагрудник", "ботинки на скорость", "железный шлем",],
            "поддержка":["зелье хила","зелье стамины","бинты х 10","зелье ярости"],
            "атака":["точильный станок","улучшеная рукоять","дополнительный клинок","утонщенное лезвие","утолщенное лезвие"],
        }

        links = LinkedDropdowns(data)
        links2 = LinkedDropdowns2(data2)

        self.btn = Button(text='дальше', size_hint=(None, None), size=(250, 50))
        self.btn.on_press = self.next2

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(links)
        layout.add_widget(links2)
        layout.add_widget(self.btn)

        self.add_widget(layout)

    def next2(self):
        self.manager.transition.direction = 'left'                                    
        self.manager.current = 'two'





class SecondScr(Screen):
    def __init__(self, name='two'):
        super().__init__(name=name)
        
        self.txt = Label(text='1')
        self.txt1 = Label(text='2')
        self.txt2 = Label(text='3')
        self.txt3 = Label(text='4')

        layout1 = BoxLayout(orientation='horizontal')
        layout1.add_widget(self.txt)
        layout1.add_widget(self.txt1)
        layout1.add_widget(self.txt2)
        layout1.add_widget(self.txt3)
        self.add_widget(layout1)





class two_slide(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        return sm
        


app = two_slide()
app.run()
