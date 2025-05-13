
from kivy.app import App
import sys
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
import random

Window.size = (1300, 680)
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
#------------------------------------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------1-------------------------------------------------

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        data = {
            "маг": {
                'weapons': ["посох", "волшебная палочка", "магические перчатки"],
                'skills': ['огненный шар', 'ледяной шар', 'кислотное облако', 'мини торнадо','молния','невидимость','ослепление','левитация','телекинез']
            },
            "друид": {
                'weapons': ["посох","магический шар","ничего"],
                'skills': ['шипы из земли','презыв животных','каменная брона','водяной вихрь','острые лианы','воскрешение','создание предметов'],
            },
            "паладин": {
                'weapons': ["меч","двуручный меч","копье","алебарда","моргенштерн"],
                'skills': ['священный клинок','удар по земле','пронзающий удар','отравленные кинжалы','благословение солнца'],
            },
            "некромант": {
                'weapons': ["боевая коса"," отравленный кенжал","скытые клинки"],
                'skills': ['воскрешение','армия скелетов','армия зомби','костяная стрела','костяная броня','вампиризм','вызов призраков']
            },
            "варвар": {
                'weapons': ["парные топоры","молот","двуручный топор", "кастеты"],
                'skills': ['ярость','вихрь топоров','метание топоров','удар по земле','оглушающий удар','адреналин','сопротивление магии']

            },
            "бард":{
                'weapons': ["гитара","балалайка","укулеле","гусли"],
                'skills': ['зелье хила','оглушающее пение','зелье ярости','острые ноты','ослепляющая музыка','зелье отравления']
            }, 
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

#-------------------------------------------------------------------------2-----------------------------------------------------------

class SecondScr(Screen):
    def __init__(self, name='two'):
        super().__init__(name=name)
        
        self.txt = Label(text='xp:')
        self.txt1 = Label(text='броня:')
        self.txt2 = Label(text='стамина:')
        self.txt3 = Label(text='ловкость:')
        self.btn10 = Button(text='сгенерировать', size_hint=(None, None), size=(250, 50))
        self.btn10.on_press = self.rand
        self.btn11 = Button(text='продолжить', size_hint=(None, None), size=(250, 50))
        self.btn11.on_press = self.next3
            

        layout2 = BoxLayout(orientation='vertical')
        layout1 = BoxLayout(orientation='horizontal')
        layout1.add_widget(self.txt)
        layout1.add_widget(self.txt1)
        layout1.add_widget(self.txt2)
        layout1.add_widget(self.txt3)
        layout1.add_widget(self.btn10)
        layout1.add_widget(self.btn11)
        layout2.add_widget(layout1)

        self.add_widget(layout2)
    
    def rand(self):
        number = random.randint(10, 20)
        number1 = random.randint(10, 20)
        number2 = random.randint(10, 20)
        number3 = random.randint(10, 20)
        self.txt.text = 'xp: ' + str(number)
        self.txt1.text = 'броня: ' + str(number1)
        self.txt2.text = 'стамина: ' + str(number2)
        self.txt3.text = 'ловкость: ' + str(number3)
        print(number)
    def next3(self):
        self.manager.transition.direction = 'left'                                    
        self.manager.current = 'three'



class ThreeScr(Screen):
    def __init__(self, name='three'):
        super().__init__(name=name)




class osnova_slide(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThreeScr())
        return sm
        


app = osnova_slide()
app.run()
