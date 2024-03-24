from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.pagelayout import PageLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class MainPage(Screen):
    def __init__(self,**kwargs):
        super(MainPage, self).__init__(**kwargs)
        button = Button(text = "hit me", on_press = self.next)
        self.add_widget(button)

    def next(self,instance):
        self.manager.current = "toolpage"

class StartPage(Screen):
    def __init__(self,**kwargs):
        super(StartPage,self).__init__(**kwargs)

        page = PageLayout()
        pg1 = BoxLayout(orientation = "vertical")
        pg2 = BoxLayout(orientation = "vertical")
        pg3 = BoxLayout(orientation = "vertical")
        pg4 = BoxLayout(orientation = "vertical")


        top1_label = Label(text = "Welcome to", size_hint = (1.0, 0.25), font_size = 50 ,color=(1, 1, 1, 1))
        logo1_label = Label(text = "#Place holder for project logo",size_hint = (1.0, 0.25))
        text1_label = Label(text = "Before we begin, lets see \nall the features you \ncould get your hands on",size_hint = (1.0, 0.25), font_size = 20)
        blank1_label = Label(text = "(Slide left to continue)", size_hint = (1.0, 0.25))
        pg1.add_widget(top1_label)
        pg1.add_widget(logo1_label)
        pg1.add_widget(text1_label)
        pg1.add_widget(blank1_label)

        logo2_label = Label(text = "#Placeholder for project logo", size_hint = (1.0, 0.2))
        my_text1 = "In CRoom, you can: \n-Find 1k+ hostels and flats in you area \n-Search for hostel/flat in 20+ areas \n-Save your favourite room for later \n-be a landlord \n-And more..."
        text2_label = Label(text = my_text1)
        pg2.add_widget(logo2_label)
        pg2.add_widget(text2_label)

        logo3_label = Label(text = "#Placeholder for project logo", size_hint = (1.0, 0.2))
        my_text2 = "We also provide:\n  Zer0 paper work,\n  Zer0 brokerage,\n  Zer0 Installment,\n  Reasonable price for call and subscription!"
        text3_label = Label(text = my_text2)
        pg3.add_widget(logo3_label)
        pg3.add_widget(text3_label)

        logo4_label = Label(text = "#Placeholder for project logo", size_hint = (1.0, 0.2))
        text4_label = Label(text = "So what are you \nwaiting for?", size_hint = (1.0,0.2))
        text4_1_label = Label(text = "Put on your shoes\nand lets get\nstarted", size_hint = (1.0,0.2))
        text4_2_label = Label(text = "#Placeholder for image")
        button = Button(text = "Start", size_hint = (0.3,0.2), pos_hint = {"right" : 1})
        pg4.add_widget(logo4_label)
        pg4.add_widget(text4_label)
        pg4.add_widget(text4_1_label)
        pg4.add_widget(text4_2_label)
        pg4.add_widget(button)


        page.add_widget(pg1)
        page.add_widget(pg2)
        page.add_widget(pg3)
        page.add_widget(pg4)

        self.add_widget(page)

        
    def gotomain(self,instance):
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class ToolPage(Screen):
    def __init__(self,**kwargs):
        super(ToolPage,self).__init__(**kwargs)
        #add layouts
    def next(self,instance):
        pass

class MessagePage(Screen):
    def __init__(self,**kwargs):
        super(MessagePage,self).__init__(**kwargs)
        #add layouts
    def next(self,instance):
        pass

class ProfilePage(Screen):
    def __init__(self,**kwargs):
        super(ProfilePage,self).__init__(**kwargs)
        #add layouts
    def next(self,instance):
        pass

class EditProfPage(Screen):
    def __init__(self,**kwargs):
        super(EditProfPage,self).__init__(**kwargs)
        #add layouts
    def next(self,instance):
        pass

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        
        screen_manager.add_widget(StartPage(name = "startpage"))
        screen_manager.add_widget(MainPage(name = "mainpage"))
        screen_manager.add_widget(ToolPage(name = "toolpage"))
        screen_manager.add_widget(MessagePage(name = "messagepage"))
        screen_manager.add_widget(ProfilePage(name = "profilepage"))
        screen_manager.add_widget(EditProfPage(name = "editprofpage"))
        

        return screen_manager
    
if __name__ == "__main__":
    MyApp().run()