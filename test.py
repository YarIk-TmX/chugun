from kivy.app import App
import sys
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (1300, 510)
heo_class = ''


class LinkedDropdowns(BoxLayout):
    def __init__(self, data: dict[str, list[str]], **kwargs):
        super().__init__(**kwargs)


        self.data = data

        layout = BoxLayout(orientation='vertical')
        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(orientation='horizontal')
        layout3 = BoxLayout(orientation='horizontal')
        layout4 = BoxLayout(orientation='horizontal')
        layout5 = BoxLayout(orientation='vertical')

        self.main_button_1 = Button(text='класс', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))
        self.main_button_2 = Button(text='оружие', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))

        self.main_button_3 = Button(text='скилл1', size_hint=(None, None), size=(250, 50))
        self.main_button_4 = Button(text='скилл2', size_hint=(None, None), size=(250, 50))
        self.main_button_5 = Button(text='скилл3', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))
        self.main_button_6 = Button(text='скилл', size_hint=(None, None), pos_hint={'top': 1}, size=(250, 50))


        
        self.add_widget(self.main_button_1)
        self.add_widget(self.main_button_2)
        layout1.add_widget(self.main_button_5)

        layout5.add_widget(self.main_button_3)
        layout4.add_widget(self.main_button_4)
        layout5.add_widget(self.main_button_6)
    

        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        layout1.add_widget(layout4)
        layout4.add_widget(layout5)

        
        self.add_widget(layout)
        self.add_widget(layout1)
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
#-------------------------------------------------------2----------------------------------------------------------------
class LinkedDropdowns2(BoxLayout):
    def __init__(self, data: dict[str, list[str]], **kwargs):
        super().__init__(**kwargs)


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
class two_slide(App):
    def build(self):

        data = {
            "маг": ["посох", "волшебная палочка", "магические перчатки"],
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

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(links)
        layout.add_widget(links2)

        return layout
        

app = two_slide()
app.run()
