from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.slider import Slider
from kivy.graphics import Color, Line
from check import check_and_install_modules as cim
from pages import *
import webbrowser
import random


class MainPage(Screen):
    def __init__(self,**kwargs):
        super(MainPage, self).__init__(**kwargs)
        out = BoxLayout(orientation = "vertical")
        top1 = BoxLayout(size_hint = (1.0, 0.1))
        top2 = BoxLayout(size_hint = (1.0, 0.1))
        top3 = BoxLayout(size_hint = (1.0, 0.1))

        tools_btn = Button(text = "Tools", on_press = self.tools, size_hint = (0.3, 1.0))
        blank = BLabel(text = "____", size_hint = (0.3, 1.0))
        logo_label = BLabel(text = "#place for logo")
        top1.add_widget(tools_btn)
        top1.add_widget(blank)
        top1.add_widget(logo_label)

        self.hostel_btn = ToggleButton(text = "Hostel", on_press = self.hostel_func, state = "down")
        self.flat_btn = ToggleButton(text = "Flat", on_press = self.flat_func)
        self.roommate_btn = ToggleButton(text = "Room Mate", on_press = self.roommate_func)
        top2.add_widget(self.hostel_btn)
        top2.add_widget(self.flat_btn)
        top2.add_widget(self.roommate_btn)

        self.textinput = TextInput(hint_text = "search", multiline = False)
        search_btn = Button(text = "search", on_press = self.search, size_hint = (0.1, 1.0))
        top3.add_widget(self.textinput)
        top3.add_widget(search_btn)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        self.buttons = []
        for i in range(10):
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = BLabel(text = f"#image{i+1}", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = BLabel(text = f"Hostel {htext}")
            area_name = BLabel(text = f"Area :{self.textinput.text}")
            rate_name = BLabel(text = f"Rate: {rtext * 500}")
            type_name = BLabel(text = f"Type: {ttext}")
            sep_name = BLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gohost)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)


        out.add_widget(top1)
        out.add_widget(top2)
        out.add_widget(top3)
        out.add_widget(self.scroll)
        self.add_widget(out)

    def hostel_func(self, instance):
        self.flat_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size = (500, 1000))
            btn_img = Image(source = f"btn{i+1}")
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = BLabel(text = f"Hostel {htext}")
            area_name = BLabel(text = f"Area :{self.textinput.text}")
            rate_name = BLabel(text = f"Rate: {rtext * 500}")
            type_name = BLabel(text = f"Type: {ttext}")
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gohost)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)


    def flat_func(self, instance):
        self.hostel_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            ftext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size = (500, 1000))
            btn_img = Image(source = f"btn{i+1}")
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            flat_name = BLabel(text = f"Flat {ftext}")
            area_name = BLabel(text = f"Area :{self.textinput.text}")
            rate_name = BLabel(text = f"Rate: {rtext * 100}")
            type_name = BLabel(text = f"Type: {ttext}")
            in_btn_layout.add_widget(flat_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.goflat)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)


    def roommate_func(self, instance):
        self.flat_btn.state = "normal"
        self.hostel_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            htext = random.choice(["Ruhan", "Yash", "Atul", "Prem", "Ayush", "Mayur"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Room", "Roommate"])
            btn_layout = BoxLayout(size = (500, 1000))
            btn_img = Image(source = f"btn{i+1}")
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = BLabel(text = f"{htext}")
            area_name = BLabel(text = f"Area :{self.textinput.text}")
            rate_name = BLabel(text = f"Rate: {rtext * 500}")
            type_name = BLabel(text = f"Searching for: {ttext}")
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.goroom)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)



    def gohost(self, instance):
        pass
    def goflat(self, instance):
        pass
    def goroom(self, instance):
        pass

    def search(self, instance):
        area = self.textinput.text
        for button in self.buttons:
            button.text = f"Area :{self.textinput.text}"
    def goto(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"       

    def tools(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "push")
        self.manager.current = "toolpage"

class ToolPage(Screen):
    def __init__(self,**kwargs):
        super(ToolPage,self).__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')
        top_box = BoxLayout(orientation = 'horizontal', size_hint = (1.0, 0.2))
        back_btn = Button(text = "Back", on_press = self.back, size_hint = (0.2, 1.0))
        logo_image = Image(source = 'user_logo.png', size_hint = (0.3, 1.0))
        user_name = BLabel(text="user_name")
        mess_btn = Button(text = "message", on_press = self.mess, size_hint = (0.2, 1.0))
        top_box.add_widget(back_btn)
        top_box.add_widget(logo_image)
        top_box.add_widget(user_name)
        top_box.add_widget(mess_btn)

        btn_box = BoxLayout(orientation = "vertical")
        prof_btn = Button(text = "Profile", on_press = self.prof)
        saved_btn = Button(text = "Saved", on_press = self.save)
        upgrade_btn = Button(text = "Upgrades", on_press = self.upgrade)
        term_btn = Button(text = "Terms & Policies", on_press = self.term)
        land_btn = Button(text = "Be a Landlord", on_press = self.land)
        btn_box.add_widget(prof_btn)
        btn_box.add_widget(saved_btn)
        btn_box.add_widget(upgrade_btn)
        btn_box.add_widget(term_btn)
        btn_box.add_widget(land_btn)

        sepa = BoxLayout(size_hint = (1.0, 0.2))
        line = Color(0,0,0,1)
        sepa.canvas.add(Line(points = (0,0, layout.width, 1), color = line))

        bot = BoxLayout(size_hint = (1.0, 0.2))
        faq_btn = Button(text = "FAQs", on_press = self.faq)
        set_btn = Button(text = "Settings", on_press = self.setf)
        bot.add_widget(faq_btn)
        bot.add_widget(set_btn)

        layout.add_widget(top_box)
        layout.add_widget(btn_box)
        layout.add_widget(sepa)
        layout.add_widget(bot)

        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "pop")
        self.manager.current = "mainpage"

    def mess(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "messagepage"
    
    def prof(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "profilepage"
    def save(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "savedpage"
    def upgrade(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "upgradepage"
    def term(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "termspage"
    def land(self, instance):
        # Define the website link
        website_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        
        # Open the website link in the default web browser
        webbrowser.open(website_link)
    def faq(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "faqpage"
    def setf(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "settingspage"

class MessagePage(Screen):
    def __init__(self,**kwargs):
        super(MessagePage,self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        top_box = BoxLayout(orientation='horizontal', size_hint_y=0.15)
        back_button = Button(text='Back',size_hint_x = 0.2,  on_press=self.back)
        self.textinput = TextInput(hint_text='Search Messages')
        search_button = Button(text='Search',size_hint_x = 0.2, on_press=self.search)
        top_box.add_widget(back_button)
        top_box.add_widget(self.textinput)
        top_box.add_widget(search_button)

        toggle_box = BoxLayout(orientation='horizontal', size_hint_y=0.25)
        self.focused_button = ToggleButton(text='Focused', on_press=self.focus, state = "down")
        self.other_button = ToggleButton(text='Other', on_press=self.other)
        toggle_box.add_widget(self.focused_button)
        toggle_box.add_widget(self.other_button)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(10):
            htext = random.choice(["Ruhan", "Yash", "Atul", "Prem", "Mayur", "Ayush"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = BLabel(text = f"#image{i+1}", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            user_name = BLabel(text = f"{htext}")
            sep_name = BLabel(text = "_"*100)
            in_btn_layout.add_widget(user_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gomess)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)


        write = Button(text = "Write message", size_hint_y = 0.2, on_press = self.goto)

        layout.add_widget(top_box)
        layout.add_widget(toggle_box)
        layout.add_widget(self.scroll)
        layout.add_widget(write)

        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"
    def search(self, instance):
        area = self.textinput.text
        if area:
            self.grid.clear_widgets()
            self.scroll.clear_widgets()
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = BLabel(text = f"#image", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            user_name = BLabel(text = f"{area}")
            sep_name = BLabel(text = "_"*100)
            in_btn_layout.add_widget(user_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gomess)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.scroll.add_widget(self.grid)

    def goto(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"
    def gomess(self, instance):
        pass

    def focus(self, instance):
        self.other_button.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        for i in range(5):
            htext = random.choice(["Ruhan", "Yash", "Atul", "Prem", "Mayur", "Ayush"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = BLabel(text = f"#image{i+1}", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            user_name = BLabel(text = f"{htext}")
            sep_name = BLabel(text = "_"*100)
            in_btn_layout.add_widget(user_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gomess)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)
    def other(self, instance):
        self.focused_button.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        for i in range(5):
            htext = random.choice(["Ad", "Promotion", "Sponser", "Spam", "Fraud"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = BLabel(text = f"#image{i+1}", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            user_name = BLabel(text = f"{htext}")
            sep_name = BLabel(text = "_"*100)
            in_btn_layout.add_widget(user_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gomess)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)

class ProfilePage(Screen):
    def __init__(self,**kwargs):
        super(ProfilePage,self).__init__(**kwargs)
        grid = BoxLayout(orientation = "vertical")
        grid.bind(minimum_height = grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = BLabel(text = "Profile      ")
        account_btn = Button(text = "Account", size_hint_x = 0.3, on_press = self.account)
        top.add_widget(back_btn)
        top.add_widget(label)
        top.add_widget(account_btn)
        grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source='logo.png', size_hint=(0.3, 1.0))
        right_layout = BoxLayout(orientation='vertical')
        username_label = BLabel(text='Username')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = BLabel(text='Area', size_hint=(0.7, 1.0))
        edit_profile_button = Button(text='Edit Profile', size_hint=(0.3, 1.0), on_press = self.edit_prof)
        area_layout.add_widget(area_label)
        area_layout.add_widget(edit_profile_button)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, grid.width, 1), color = line))
        grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = BLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = BLabel(text = "gender : male", font_size = 30)
        age = BLabel(text = "age : 20", font_size = 30)
        study = BLabel(text = "Years of study : FE", font_size = 30)
        branch = BLabel(text = "Branch : CS", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, grid.width, 1), color = line))
        grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = BLabel(text = "Preference:")
        edit_pre_btn = Button(text = "edit", size_hint_x = 0.2, on_press = self.edit_pre)
        bot_top.add_widget(pre_label)
        bot_top.add_widget(edit_pre_btn)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        for i in range(14):
            pre_box = BoxLayout(orientation = "vertical")
            pre_logo = Image(source=f'pre{i+1}.png')
            pre_pre_label = BLabel(text = f"{i+1}")
            pre_box.add_widget(pre_logo)
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        grid.add_widget(bot)

        self.add_widget(grid)

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"
    def account(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "loginpage"
    def edit_prof(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "editprofpage"
    def edit_pre(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "editprefpage"

class EditProfPage(Screen):
    def __init__(self,**kwargs):
        super(EditProfPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label= BLabel(text = "Edit Profile")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        img_lay = BoxLayout(size_hint_y = 0.3)
        img = Image(source = 'user.png', size = (100,100), size_hint = (None,None))
        img_btn = Button(text = "change", size_hint = (None, None), size = (50,50), on_press = self.change_img)
        img_lay.add_widget(img)
        img_lay.add_widget(img_btn)
        layout.add_widget(img_lay)

        grid = GridLayout(cols = 2)
        name_label = BLabel(text = "Name:", size_hint_x = 0.25)
        name_text = TextInput(hint_text = "enter your name")
        place_label = BLabel(text = "Place:", size_hint_x = 0.25)
        place_text = TextInput(hint_text = "enter your place")
        ph_label = BLabel(text = "Phone no:", size_hint_x = 0.25)
        ph_text = TextInput(hint_text = "enter your phone number")
        email_label = BLabel(text = "Email:", size_hint_x = 0.25)
        email_text = TextInput(hint_text = "enter your email address")
        gender_label = BLabel(text = "Gender:", size_hint_x = 0.25)
        gender_text = TextInput(hint_text = "enter your gender")
        age_label = BLabel(text = "Age:", size_hint_x = 0.25)
        age_text = TextInput(hint_text = "enter your age")
        study_label = BLabel(text = "Year of study:", size_hint_x = 0.25)
        study_text = TextInput(hint_text = "enter your tear of study")
        branch_label = BLabel(text = "Branch:", size_hint_x = 0.25)
        branch_text = TextInput(hint_text = "enter your Branch")
        grid.add_widget(name_label)
        grid.add_widget(name_text)
        grid.add_widget(place_label)
        grid.add_widget(place_text)
        grid.add_widget(ph_label)
        grid.add_widget(ph_text)
        grid.add_widget(email_label)
        grid.add_widget(email_text)
        grid.add_widget(gender_label)
        grid.add_widget(gender_text)
        grid.add_widget(age_label)
        grid.add_widget(age_text)
        grid.add_widget(study_label)
        grid.add_widget(study_text)
        grid.add_widget(branch_label)
        grid.add_widget(branch_text)
        layout.add_widget(grid)

        save_btn = Button(text = "save", on_press = self.save, size_hint_y = 0.2)
        layout.add_widget(save_btn)
        self.add_widget(layout)

    def back(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "profilepage"
    def save(self, instance):
        pass
    def change_img(self, instance):
        pass

class LoginPage(Screen):
    def __init__(self,**kwargs):
        super(LoginPage,self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "back", size_hint_x = 0.2, on_press = self.back)
        log_label = BLabel(text = "Account")
        top.add_widget(back_btn)
        top.add_widget(log_label)
        layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        email_box = BoxLayout()
        email_label = BLabel(text = "Email", halign = "left", size_hint_x = 0.3)
        email_text = TextInput(hint_text = "Enter email")
        email_box.add_widget(email_label)
        email_box.add_widget(email_text)
        pass_box = BoxLayout()
        pass_label = BLabel(text = "Password", halign = "left", size_hint_x = 0.3)
        pass_text = TextInput(hint_text = "Enter password", password = True)
        pass_box.add_widget(pass_label)
        pass_box.add_widget(pass_text)
        forgot_btn = Button(text = "Forgot Password?", on_press = self.forgot, size_hint_y = 0.4)
        sepa1 = BoxLayout(size_hint_y = 0.2)
        line = Color(0,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, mid.width, 1), color = line))
        mid.add_widget(sepa1)
        acc_box = BoxLayout(size_hint_y = 0.4)
        log_in = Button(text = "Log In", on_press = self.log)
        sign_in = Button(text = "Sign In", on_press = self.sign)
        acc_box.add_widget(log_in)
        acc_box.add_widget(sign_in)
        mid.add_widget(email_box)
        mid.add_widget(pass_box)
        mid.add_widget(forgot_btn)
        mid.add_widget(acc_box)
        layout.add_widget(mid)

        sepa2 = BoxLayout(size_hint_y = 0.35)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, layout.width, 1), color = line))
        layout.add_widget(sepa2)

        self.add_widget(layout)

    def back(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "profilepage"
    def forgot(self, instance):
        self.manager.transition =  CardTransition(direction = "left", mode = "push")
        self.manager.current = "forgotpage"
    def log(self, instance):
        pass
    def sign(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "signpage"

class SavedPage(Screen):
    def __init__(self, **kwargs):
        super(SavedPage, self).__init__(**kwargs)
        out = BoxLayout(orientation = "vertical")
        top1 = BoxLayout(size_hint = (1.0, 0.1))
        top2 = BoxLayout(size_hint = (1.0, 0.1))
        top3 = BoxLayout(size_hint = (1.0, 0.1))

        back_btn = Button(text = "Back", on_press = self.back, size_hint = (0.3, 1.0))
        blank = BLabel(text = "____", size_hint = (0.3, 1.0))
        logo_label = BLabel(text = "Saved profiles")
        top1.add_widget(back_btn)
        top1.add_widget(logo_label)
        top1.add_widget(blank)

        self.hostel_btn = ToggleButton(text = "Hostel", on_press = self.hostel_func, state = "down")
        self.flat_btn = ToggleButton(text = "Flat", on_press = self.flat_func)
        self.roommate_btn = ToggleButton(text = "Room Mate", on_press = self.roommate_func)
        top2.add_widget(self.hostel_btn)
        top2.add_widget(self.flat_btn)
        top2.add_widget(self.roommate_btn)

        self.textinput = TextInput(hint_text = "search", multiline = False)
        search_btn = Button(text = "search", on_press = self.search, size_hint = (0.1, 1.0))
        top3.add_widget(self.textinput)
        top3.add_widget(search_btn)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Hostel{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)
        

        out.add_widget(top1)
        out.add_widget(top2)
        out.add_widget(top3)
        out.add_widget(self.scroll)
        self.add_widget(out)

    def hostel_func(self, instance):
        self.flat_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Hostel{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def flat_func(self, instance):
        self.hostel_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Flat{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def roommate_func(self, instance):
        self.flat_btn.state = "normal"
        self.hostel_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(10):
            btn = Button(text = f"Roommate{i+1} in {self.textinput.text}",size_hint_y = None, height = 150, on_press = self.goto)
            self.grid.add_widget(btn)
            self.buttons.append(btn)
        self.scroll.add_widget(self.grid)

    def search(self, instance):
        area = self.textinput.text
        for button in self.buttons:
            button.text = f"{button.text.split()[0]} in {area}"
    
    def goto(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"       

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"

class ForgotPage(Screen):
    def __init__(self, **kwargs):
        super(ForgotPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        logo_img = Image(source = "logo.png")
        top.add_widget(back_btn)
        top.add_widget(logo_img)
        layout.add_widget(top)

        otp_label = BLabel(text = "OTP: (send on email)", size_hint_y = 0.15)
        otp_text = TextInput(hint_text = "Enter OTP", size_hint_y = 0.15)
        otp_btn = Button(text = "Resend OTP", on_press = self.resend, size_hint_y = 0.15)
        newpass_label = BLabel(text = "New Password", size_hint_y = 0.15)
        newpass_text = TextInput(hint_text = "Enter new password", size_hint_y = 0.15)
        repass_label = BLabel(text = "Re-enter Password", size_hint_y = 0.15)
        repass_text = TextInput(hint_text = "Enter new password again", size_hint_y = 0.15)
        update_btn = Button(text = "update", on_press = self.update, size_hint_y = 0.15)
        sepa2 = BoxLayout(size_hint_y = 0.15)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, layout.width, 1), color = line))
        
        layout.add_widget(otp_label)
        layout.add_widget(otp_text)
        layout.add_widget(otp_btn)
        layout.add_widget(newpass_label)
        layout.add_widget(newpass_text)
        layout.add_widget(repass_label)
        layout.add_widget(repass_text)
        layout.add_widget(sepa2)
        layout.add_widget(update_btn)

        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "loginpage"
    def resend(self, instance):
        pass
    def update(self, instance):
        pass

class SignPage(Screen):
    def __init__(self, **kwargs):
        super(SignPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "back", size_hint_x = 0.2, on_press = self.back)
        sign_label = BLabel(text = "Sign in")
        top.add_widget(back_btn)
        top.add_widget(sign_label)
        layout.add_widget(top)

        user_label = BLabel(text = "User Name:", size_hint_y = 0.12)
        user_text = TextInput(hint_text = "Enter user name", size_hint_y = 0.12)
        email_label = BLabel(text = "Email:", size_hint_y = 0.12)
        email_text = TextInput(hint_text = "Enter email", size_hint_y = 0.12)
        ph_label = BLabel(text = "Phone number:", size_hint_y = 0.12)
        ph_text = TextInput(hint_text = "Enter phone number", size_hint_y = 0.12)
        pass_label = BLabel(text = "Password:", size_hint_y = 0.12)
        pass_text = TextInput(hint_text = "Enter password", size_hint_y = 0.12)
        repass_label = BLabel(text = "Re-enter Password:", size_hint_y = 0.12)
        repass_text = TextInput(hint_text = "Enter password again", size_hint_y = 0.12)
        create_btn = Button(text = "Create account", size_hint_y = 0.2, on_press = self.create)
        sepa2 = BoxLayout(size_hint_y = 0.15)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, layout.width, 1), color = line))
        layout.add_widget(user_label)
        layout.add_widget(user_text)
        layout.add_widget(email_label)
        layout.add_widget(email_text)
        layout.add_widget(ph_label)
        layout.add_widget(ph_text)
        layout.add_widget(pass_label)
        layout.add_widget(pass_text)
        layout.add_widget(repass_label)
        layout.add_widget(repass_text)
        layout.add_widget(sepa2)
        layout.add_widget(create_btn)

        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "loginpage"
    def create(self, instance):
        pass

class EditPrefPage(Screen):
    def __init__(self, **kwargs):
        super(EditPrefPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "back", size_hint_x = 0.2, on_press = self.back)
        edit_label = BLabel(text = "Edit Preference")
        top.add_widget(back_btn)
        top.add_widget(edit_label)
        layout.add_widget(top)

        grid = GridLayout(cols = 4)
        for i in range(21):
            pre_box = BoxLayout(orientation = "vertical")
            pre_logo = Image(source=f'pre{i+1}.png')
            pre_btn = ToggleButton(text = f"{i+1}", size_hint_y = 0.4)
            pre_box.add_widget(pre_logo)
            pre_box.add_widget(pre_btn)
            grid.add_widget(pre_box)
        layout.add_widget(grid)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(0,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, layout.width, 1), color = line))
        layout.add_widget(sepa2)
        save_btn = Button(text = "Save", on_press = self.save, size_hint_y = 0.2)
        layout.add_widget(save_btn)

        self.add_widget(layout)

    def back(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "profilepage"
    def save(self, instance):
        pass

class FAQPage(Screen):
    def __init__(self, **kwargs):
        super(FAQPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        faq_label = BLabel(text = "FAQs")
        top.add_widget(back_btn)
        top.add_widget(faq_label)
        layout.add_widget(top)

        bot = BoxLayout(orientation = "vertical")
        prob_label = BLabel(text = "Problem Statement:")
        prob_text = TextInput(text = "A solution for college students\nto find hostel/flat/roommate", multiline = True, readonly = True)
        team_label = BLabel(text = "Team Members:")
        team_text = TextInput(text = "- Ruhan Saad Dave\n- Yash Sanjay Chavan\n- Prem Gautam Gavhane\n- Ayush\n- Mayur Abhay Sadguru\nAtul Govind Sangale", multiline = True, readonly = True)
        tool_label = BLabel(text = "Tools used in building this app:")
        tool_text = TextInput(text = "Python\nKivy\npymongo\nimportlib\nsubprocess", multiline = True, readonly = True)
        bot.add_widget(prob_label)
        bot.add_widget(prob_text)
        bot.add_widget(team_label)
        bot.add_widget(team_text)
        bot.add_widget(tool_label)
        bot.add_widget(tool_text)
        layout.add_widget(bot)
        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"

class UpgradePage(Screen):
    def __init__(self, **kwargs):
        super(UpgradePage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = BLabel(text = "Upgrade")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        call_box = BoxLayout()
        call_label = BLabel(text = "Calls left:")
        call_value_label = BLabel(text = " ")
        call_box.add_widget(call_label)
        call_box.add_widget(call_value_label)
        layout.add_widget(call_box)

        message_box = BoxLayout()
        message_label = BLabel(text = "Messages left:")
        message_value_label = BLabel(text = " ")
        message_box.add_widget(message_label)
        message_box.add_widget(message_value_label)
        layout.add_widget(message_box)

        sub_box = BoxLayout()
        sub_label = BLabel(text = "Subscriptin end date:")
        sub_value_label = BLabel(text = " ")
        sub_box.add_widget(sub_label)
        sub_box.add_widget(sub_value_label)
        layout.add_widget(sub_box)

        purchase_label = RLabel(text = "Purchase:")
        layout.add_widget(purchase_label)

        call_option = BoxLayout()
        for i in range(4):
            in_call_box = BoxLayout(orientation = "vertical")
            in_call_label = BLabel(text = f"{i+1} call", size_hint_y = 0.65)
            in_call_btn = Button(text = f"Rs. {(i+1)*10}", on_press = self.call)
            in_call_box.add_widget(in_call_label)
            in_call_box.add_widget(in_call_btn)
            call_option.add_widget(in_call_box)
        layout.add_widget(call_option)

        message_option = BoxLayout()
        for i in range(4):
            in_message_box = BoxLayout(orientation = "vertical")
            in_message_label = BLabel(text = f"{(i+1)*10} message", size_hint_y = 0.65)
            in_message_btn = Button(text = f"Rs. {(i+1)*10}", on_press = self.message)
            in_message_box.add_widget(in_message_label)
            in_message_box.add_widget(in_message_btn)
            message_option.add_widget(in_message_box)
        layout.add_widget(message_option)

        sub_option = BoxLayout()
        for i in range(4):
            in_sub_box = BoxLayout(orientation = "vertical")
            in_sub_label = BLabel(text = f"{i+1} month subscription", size_hint_y = 0.65)
            in_sub_btn = Button(text = f"Rs. {(i+1)*300}", on_press = self.sub)
            in_sub_box.add_widget(in_sub_label)
            in_sub_box.add_widget(in_sub_btn)
            sub_option.add_widget(in_sub_box)
        layout.add_widget(sub_option)


        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"
    def call(self, instance):
        pass
    def message(self, instance):
        pass
    def sub(self, instance):
        pass

class TermsPage(Screen):
    def __init__(self, **kwargs):
        super(TermsPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = BLabel(text = "Terms & Policies")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        term_text1 = TextInput(font_size = 15, text = "Acceptance of Terms:\nUsers agree to these terms by accessing or using the platform.", multiline = True, readonly = True)
        term_text2 = TextInput(font_size = 12,text = "Description of Service:\n[Your Platform Name] facilitates online searches for hostels, flats, or roommates. Users can create profiles, list properties, search for accommodations, and connect with potential roommates.", multiline = True, readonly = True)
        term_text3 = TextInput(font_size = 12,text = "User Responsibilities:\nProvide accurate information. Maintain account confidentiality. Adhere to community guidelines and avoid illegal activities.", multiline = True, readonly = True)
        term_text4 = TextInput(font_size = 12,text = "Data Privacy:\nUser data is collected and processed according to the Privacy Policy. Consent to the collection, storage, and use of personal information.", multiline = True, readonly = True)
        term_text5 = TextInput(font_size = 12,text = "Intellectual Property:\n[Your Company Name] owns or licenses all content and materials on the platform. Users retain ownership rights to their uploaded content.", multiline = True, readonly = True)
        term_text6 = TextInput(font_size = 12,text = "Liability:\nNo guarantee of availability, accuracy, or completeness of content. Not liable for damages or losses from platform use.", multiline = True, readonly = True)
        term_text7 = TextInput(font_size = 15,text = "Termination:\nRight to suspend or terminate accounts for violations. Users can terminate accounts by contacting support.", multiline = True, readonly = True)
        term_text8 = TextInput(font_size = 15,text = "Dispute Resolution:\nDisputes resolved through arbitration or mediation. Laws of [Your Jurisdiction] govern these terms.", multiline = True, readonly = True)
        term_text9 = TextInput(font_size = 15,text = "Changes to Terms:\nTerms may be updated without prior notice. Users responsible for reviewing changes periodically.", multiline = True, readonly = True)
        term_text10 = TextInput(font_size = 15,text = "Contact Information:\nFor questions or concerns, contact [Your Contact Email].", multiline = True, readonly = True)
        layout.add_widget(term_text1)
        layout.add_widget(term_text2)
        layout.add_widget(term_text3)
        layout.add_widget(term_text4)
        layout.add_widget(term_text5)
        layout.add_widget(term_text6)
        layout.add_widget(term_text7)
        layout.add_widget(term_text8)
        layout.add_widget(term_text9)
        layout.add_widget(term_text10)

        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"

class SettingsPage(Screen):
    def __init__(self, **kwargs):
        super(SettingsPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = BLabel(text = "Settings")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        self.audio_slider = Slider(min = 0, max = 100, value = 50)
        self.audio_label = BLabel(text = f"Audio: {self.audio_slider.value}")
        self.audio_label.bind(on_value = self.update_audio)
        mid.add_widget(self.audio_label)
        mid.add_widget(self.audio_slider)
        self.brightness_label = Label(text="Brightness: 0")
        self.brightness_slider = Slider(min=0, max=1, value=0.5)
        self.brightness_slider.bind(on_value=self.on_slider_change)
        mid.add_widget(self.brightness_label)
        mid.add_widget(self.brightness_slider)
        noti_box = BoxLayout()
        noti_label = BLabel(text = "Notification:")
        self.noti_btn = ToggleButton(text = "On", state = "down", on_press = self.noti)
        noti_box.add_widget(noti_label)
        noti_box.add_widget(self.noti_btn)
        mid.add_widget(noti_box)
        layout.add_widget(mid)

        sepa = BoxLayout(size_hint = (1.0, 0.2))
        line = Color(0,0,0,1)
        sepa.canvas.add(Line(points = (0,0, layout.width, 1), color = line))
        layout.add_widget(sepa)

        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"

    def update_audio(self, instance):
        self.audio_label.text = f"Audio:  {self.audio_slider.value}"
    def on_slider_change(self, instance):
        value = self.brightness_slider.value
        brightness_value = int(value * 100)
        self.brightness_label.text = f"Brightness: {brightness_value}"
        Window.clearcolor = [value, value, value, 1]
    def noti(self, instance):
        if self.noti_btn.state == "down":
            self.noti.text = "On"
        else:
            self.noti.text = "Off"

class Blank(Screen):
    def __init__(self,**kwargs):
        super(Blank,self).__init__(**kwargs)
        button = Button(text = "Nothing to see here for now", on_press = self.next)
        self.add_widget(button)
    def next(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "mainpage"

class ProjectApp(App):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(Start1Page(name='start1page'))
        screen_manager.add_widget(Start2Page(name='start2page'))
        screen_manager.add_widget(Start3Page(name='start3page'))
        screen_manager.add_widget(Start4Page(name='start4page'))
        screen_manager.add_widget(MainPage(name = "mainpage"))
        screen_manager.add_widget(Blank(name = "blank"))
        screen_manager.add_widget(ToolPage(name = "toolpage"))
        screen_manager.add_widget(SettingsPage(name = "settingspage"))
        screen_manager.add_widget(MessagePage(name = "messagepage"))
        screen_manager.add_widget(ProfilePage(name = "profilepage"))
        screen_manager.add_widget(LoginPage(name = "loginpage"))
        screen_manager.add_widget(ForgotPage(name = "forgotpage"))
        screen_manager.add_widget(SignPage(name = "signpage")) 
        screen_manager.add_widget(EditProfPage(name = "editprofpage"))
        screen_manager.add_widget(EditPrefPage(name = "editprefpage"))
        screen_manager.add_widget(SavedPage(name = "savedpage"))
        screen_manager.add_widget(UpgradePage(name = "upgradepage"))
        screen_manager.add_widget(FAQPage(name = "faqpage"))
        screen_manager.add_widget(TermsPage(name = "termspage"))
        

        return screen_manager
    
if __name__ == "__main__":
    cim()
    ProjectApp().run()