from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from check import check_and_install_modules as cim
from pages import Start1Page, Start2Page, Start3Page, Start4Page

class MainPage(Screen):
    def __init__(self,**kwargs):
        super(MainPage, self).__init__(**kwargs)
        out = BoxLayout(orientation = "vertical")
        top1 = BoxLayout(size_hint = (1.0, 0.1))
        top2 = BoxLayout(size_hint = (1.0, 0.1))
        top3 = BoxLayout(size_hint = (1.0, 0.1))

        tools_btn = Button(text = "Tools", on_press = self.tools, size_hint = (0.3, 1.0))
        blank = Label(text = "____", size_hint = (0.3, 1.0))
        logo_label = Label(text = "#place for logo")
        top1.add_widget(tools_btn)
        top1.add_widget(blank)
        top1.add_widget(logo_label)

        hostel_btn = ToggleButton(text = "Hostel", on_press = self.hostel_func)
        flat_btn = ToggleButton(text = "Flat", on_press = self.flat_func)
        roommate_btn = ToggleButton(text = "Room Mate", on_press = self.roommate_func)
        top2.add_widget(hostel_btn)
        top2.add_widget(flat_btn)
        top2.add_widget(roommate_btn)

        textinput = TextInput(hint_text = "search")
        search_btn = Button(text = "search", on_press = self.search, size_hint = (0.1, 1.0))
        top3.add_widget(textinput)
        top3.add_widget(search_btn)

        scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        grid = GridLayout(cols = 1, size_hint_y = None)
        grid.bind(minimum_height = grid.setter('height'))
        for i in range(50):
            btn = Button(text = f"Button {i+1}",size_hint_y = None, height = 150)
            grid.add_widget(btn)
        scroll.add_widget(grid)

        out.add_widget(top1)
        out.add_widget(top2)
        out.add_widget(top3)
        out.add_widget(scroll)
        self.add_widget(out)

    def hostel_func(self, instance):
        pass
    def flat_func(self, instance):
        pass
    def roommate_func(self, instance):
        pass

    def search(self, instance):
        pass

    def tools(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "push")
        self.manager.current = "toolpage"

class ToolPage(Screen):
    def __init__(self,**kwargs):
        super(ToolPage,self).__init__(**kwargs)
        button = Button(text = "Welcome to tools page\nOops, you are a bit early!\nWork under progress", on_press = self.start)
        self.add_widget(button)

    def start(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "pop")
        self.manager.current = "mainpage"

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
        
        screen_manager.add_widget(Start1Page(name = "start1page"))
        screen_manager.add_widget(Start2Page(name = "start2page"))
        screen_manager.add_widget(Start3Page(name = "start3page"))
        screen_manager.add_widget(Start4Page(name = "start4page"))
        screen_manager.add_widget(MainPage(name = "mainpage"))
        screen_manager.add_widget(ToolPage(name = "toolpage"))
        screen_manager.add_widget(MessagePage(name = "messagepage"))
        screen_manager.add_widget(ProfilePage(name = "profilepage"))
        screen_manager.add_widget(EditProfPage(name = "editprofpage"))
        

        return screen_manager
    
if __name__ == "__main__":
    cim()
    MyApp().run()