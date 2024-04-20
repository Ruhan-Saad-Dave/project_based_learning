from check import check_and_install_module as cim
cim()    #Tests for presence of required libraries, need to keep this and the beginning to avoid any errors.

#These are the sub-modules of the kivy library, which will be used to develop the app interface.
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition, FadeTransition, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.slider import Slider
from kivy.graphics import Color, Line, Rectangle

import webbrowser    #Used to take user to a website
import random    #Used for randomly generating artificial data, will be removed once the project will be launched in the market.
import time    #Used for delaying appearance of few effects.
from styles import *
from chatbot import ask_chatbot



class Start1Page(Screen):
    '''
    This is the 1st part of the introduction page.

    This page (and all the other 3 introduction page) explains what does our project offers.

    skip button - Takes the user directly to main page.
    next button - Takes the user to the next introduction page. 
    '''
    def __init__(self,**kwargs):    #Initiallization of the screen/page.
        super(Start1Page,self).__init__(**kwargs)
        #A widgets holder that displays information
        pg1 = BoxLayout(orientation = "vertical")
        top1_label = RLabel(text = "Welcome to", size_hint = (1.0, 0.3), font_size = 50 ,color=(1, 1, 1, 1))
        logo1_label = RLabel(text = "#1Place holder for project logo",size_hint = (1.0, 0.3))
        text1_label = RLabel(text = "Before we begin, lets see \nall the features you \ncould get your hands on",size_hint = (1.0, 0.3), font_size = 30)

        #A widgets holder for the 'skip' and 'next' button
        pg1_1 = BoxLayout(size_hint = (1.0, 0.15))
        btn1_skip = Button(text = "Skip", size_hint = (0.3, 1.0), on_press = self.skip)
        btn1_next = Button(text = "Next", size_hint = (0.3, 1.0), on_press = self.next)
        pg1_1.add_widget(btn1_skip)
        pg1_1.add_widget(btn1_next)

        #Adds the widgets holder to the outer most holder, then saving it into the screen/page
        pg1.add_widget(top1_label)
        pg1.add_widget(logo1_label)
        pg1.add_widget(text1_label)
        pg1.add_widget(pg1_1)
        self.add_widget(pg1)

    def skip(self, instance):    #Function for the 'skip' button
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"
    
    def next(self, instance):    #Function for the 'next' button
        self.manager.transition = SlideTransition()
        self.manager.current = "start2page"

class Start2Page(Screen):
    '''
    This is the 2nd part of the introduction page.

    This page (and all the other 3 introduction page) explains what does our project offers.

    skip button - Takes the user directly to main page.
    previous button - Takes the user to the previous page incase he/she accidentally press 'next' and didn't read the content.
    next button - Takes the user to the next introduction page. 
    '''
    def __init__(self,**kwargs):    #Initiallization of the screen/page
        super(Start2Page,self).__init__(**kwargs)
        #Widgets holder for the content to be displayed
        pg2 = BoxLayout(orientation = "vertical")
        logo2_label = RLabel(text = "#2Placeholder for project logo", size_hint = (1.0, 0.3),font_size = 30)
        my_text1 = "In CRoom, you can: \n-Find 1k+ hostels and flats\nin you area \n-Search for hostel/flat in\n20+ areas \n-Save your favourite room\nfor later \n-be a landlord \n-And more..."
        text2_label = RLabel(text = my_text1, font_size = 30)

        #Widgets holder for the buttons
        pg2_1 = BoxLayout(size_hint = (1.0, 0.2))
        btn2_skip = Button(text = "Skip", size_hint = (0.3, 1.0), on_press = self.skip)
        btn2_pre = Button(text = "Previous", size_hint = (0.3, 1.0), on_press = self.pre)
        btn2_next = Button(text = "Next", size_hint = (0.3, 1.0), on_press = self.next)
        #Adds the buttons to the holder
        pg2_1.add_widget(btn2_skip)
        pg2_1.add_widget(btn2_pre)
        pg2_1.add_widget(btn2_next)

        #Adds all the widgets to the outer most holder, and saving it to the screen/page.
        pg2.add_widget(logo2_label)
        pg2.add_widget(text2_label)
        pg2.add_widget(pg2_1)
        self.add_widget(pg2)

    def skip(self, instance):    #Function for the 'skip' button.
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"

    def pre(self, instance):    #Function for the 'previous' button.
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "start1page"
    
    def next(self, instance):    #Function for the 'next' button.
        self.manager.transition = SlideTransition()
        self.manager.current = "start3page"

class Start3Page(Screen):
    '''
    This is the 3rd part of the introduction page.

    This page (and all the other 3 introduction page) explains what does our project offers.

    skip button - Takes the user directly to main page.
    previous button - Takes the user to the previous page incase he/she accidentally press 'next' and didnt read the content.
    next button - Takes the user to the next introduction page. 
    '''
    def __init__(self,**kwargs):    #Initiallization of the screen/page.
        super(Start3Page,self).__init__(**kwargs)
        #Widgets holder for the content to be displayed.
        pg3 = BoxLayout(orientation = "vertical")
        logo3_label = RLabel(text = "#3Placeholder for project logo", size_hint = (1.0, 0.2), font_size = 30)
        my_text2 = "We also provide:\n  Zer0 paper work,\n  Zer0 brokerage,\n  Zer0 Installment,\n  Reasonable price for\ncall and subscription!"
        text3_label = RLabel(text = my_text2, font_size = 30)

        #Widgets holder for the buttons.
        pg3_1 = BoxLayout(size_hint = (1.0, 0.2))
        btn3_skip = Button(text = "Skip", size_hint = (0.3, 1.0), on_press = self.skip)
        btn3_pre = Button(text = "Previous", size_hint = (0.3, 1.0), on_press = self.pre)
        btn3_next = Button(text = "Next", size_hint = (0.3, 1.0), on_press = self.next)
        #Adds the button to the holder.
        pg3_1.add_widget(btn3_skip)
        pg3_1.add_widget(btn3_pre)
        pg3_1.add_widget(btn3_next)

        #Adds all the widgets to the outer most holder, and saving it to the screen/page.
        pg3.add_widget(logo3_label)
        pg3.add_widget(text3_label)
        pg3.add_widget(pg3_1)
        self.add_widget(pg3)

    def skip(self, instance):    #Function for the 'skip' button.
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"
    
    def pre(self, instance):    #Function for the 'previous' button.
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "start2page"
    
    def next(self, instance):    #Function for the 'next' button.
        self.manager.transition = SlideTransition()
        self.manager.current = "start4page"

class Start4Page(Screen):
    '''
    This is the 4th part of the introduction page.

    This page (and all the other 3 introduction page) explains what does our project offers.

    previous button - Takes the user to the previous page incase he/she accidentally press 'next' and didnt read the content.
    start button - Takes the user to the main page. 
    '''
    def __init__(self,**kwargs):    #Initialization of the screen/page.
        super(Start4Page,self).__init__(**kwargs)
        #Widgets holder for the content to be displayed.
        pg4 = BoxLayout(orientation = "vertical")
        logo4_label = RLabel(text = "#4Placeholder for project logo", size_hint = (1.0, 0.3), font_size = 30)
        text4_label = RLabel(text = "So what are you \nwaiting for?", size_hint = (1.0,0.3), font_size = 30)
        text4_1_label = RLabel(text = "Put on your shoes\nand lets get\nstarted", size_hint = (1.0,0.3), font_size = 30)
        text4_2_label = RLabel(text = "#Placeholder for image", size_hint = (1.0, 0.3), font_size = 30)

        #Widgets holder for the buttons.
        pg4_1 = BoxLayout(size_hint = (1.0, 0.2))
        btn4_start = Button(text = "Start", size_hint = (0.3, 1.0), on_press = self.start)
        btn4_pre = Button(text = "Previous", size_hint = (0.3, 1.0), on_press = self.pre)
        #Adds the button to the holder
        pg4_1.add_widget(btn4_pre)
        pg4_1.add_widget(btn4_start)
        
        #Adds all the widgets to the outer most holder, and saving it to the screen/page.
        pg4.add_widget(logo4_label)
        pg4.add_widget(text4_label)
        pg4.add_widget(text4_1_label)
        pg4.add_widget(text4_2_label)
        pg4.add_widget(pg4_1)
        self.add_widget(pg4)

    def start(self, instance):    #Function for the 'start' button.
        self.manager.transition = SlideTransition(direction = "up")
        self.manager.current = "mainpage"
    
    def pre(self, instance):    #Function for the 'previous' button.
        self.manager.transition = SlideTransition(direction = "right")
        self.manager.current = "start3page"

class MainPage(Screen):
    """
    This is the main page or the main dashboard of the project.

    This page shows all the available hotels, flats and roommates based on your desired area. You can select the type of accommodaton you like,
    see the basic details of them, and also get access to more tools.

    hostel button: Displays all the hostels available if area not specified, else show hostel in the mentioned area.
    flat button: Displays all the flats available if area not specified, else show flats in the mentioned area.
    roommate button: Displays all users available as roommate in similar way.
    search button: Searches for all the properties with the specified area, you can specifythe area in the textbox given next to the button.
    tools button: Gives you more features to try that the project offers.
    go button (->): Takes the screen control to the property that you have chosen to see more details.
    """
    def __init__(self,**kwargs):    #Initializes the page/screen
        super(MainPage, self).__init__(**kwargs)
        #Making of multiple widgets container to store the widgets
        out = BoxLayout(orientation = "vertical")
        top1 = BoxLayout(size_hint = (1.0, 0.1))
        top2 = BoxLayout(size_hint = (1.0, 0.1))
        top3 = BoxLayout(size_hint = (1.0, 0.1))

        #Top part of the screen/page
        tools_btn = Button(text = "Tools", on_press = self.tools, size_hint = (0.3, 1.0))
        blank = LBLabel(text = "____", size_hint = (0.3, 1.0))
        logo_label = LBLabel(text = "#place for logo")
        top1.add_widget(tools_btn)
        top1.add_widget(blank)
        top1.add_widget(logo_label)

        #Options button to select between hostel, flat and roommate. Will show corresponding data.
        self.hostel_btn = ToggleButton(text = "Hostel", on_press = self.hostel_func, state = "down")
        self.flat_btn = ToggleButton(text = "Flat", on_press = self.flat_func)
        self.roommate_btn = ToggleButton(text = "Room Mate", on_press = self.roommate_func)
        top2.add_widget(self.hostel_btn)
        top2.add_widget(self.flat_btn)
        top2.add_widget(self.roommate_btn)

        #Text input and search button to check for specified area.
        self.textinput = TextInput(hint_text = "search", multiline = False)
        search_btn = Button(text = "search", on_press = self.search, size_hint = (0.1, 1.0))
        top3.add_widget(self.textinput)
        top3.add_widget(search_btn)

        #Shows all the relevant properties based on type and area, and also shows basic details of each.
        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        self.buttons = []
        self.host = []
        self.area = []
        self.rate = []
        self.type = []
        self.id = []
        for i in range(20):    ##Displays the details one by one, for now just showing random details, but later will fix it
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size_hint_y = None, height = 200)
            btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"Hostel {htext}")
            area_name = LBLabel(text = f"Area :{self.textinput.text}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Type: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            self.go_btn = Button(text = f"->{i}", size_hint_x = 0.2, on_press = lambda instance: self.gohost(instance, self.go_btn.text[-1]))
            btn_layout.add_widget(self.go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
            self.host.append(htext)
            self.area.append(self.textinput.text)
            self.rate.append(rtext)
            self.type.append(ttext)
            self.id.append(i)
        self.scroll.add_widget(self.grid)

        #Saving all the widgets on the screen
        out.add_widget(top1)
        out.add_widget(top2)
        out.add_widget(top3)
        out.add_widget(self.scroll)
        self.add_widget(out)

    def hostel_func(self, instance):    #Function to display all the hostels of required area.
        self.flat_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(20):    ##Displays the details one by one, for now just showing random details, but later will fix it
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size_hint_y = None, height = 200)
            btn_img = btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"Hostel {htext}")
            area_name = LBLabel(text = f"Area :{self.textinput.text}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Type: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            self.go_btn = Button(text = f"->{i}", size_hint_x = 0.2, on_press = lambda instance: self.gohost(instance, self.go_btn.text[-1]))
            btn_layout.add_widget(self.go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)

    def flat_func(self, instance):    #Function to display all the flats of required area
        self.hostel_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(20):    ##Displays the details one by one, for now just showing random details, but later will fix it
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size_hint_y = None, height = 200)
            btn_img = btn_img = Image(source = f"pbl_app\\image_dir\\flat{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"Flat {htext}")
            area_name = LBLabel(text = f"Area :{self.textinput.text}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Type: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.goflat)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)

    def roommate_func(self, instance):    ##Function to display all the user in a specified area, will work on filtering preference.
        self.flat_btn.state = "normal"
        self.hostel_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(20):    ##Displays the details one by one, for now just showing random details, but later will fix it
            htext = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Room", "Roommate"])
            btn_layout = BoxLayout(size_hint_y = None, height = 200)
            btn_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"{htext}")
            area_name = LBLabel(text = f"Area :{self.textinput.text}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Searching for: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.goroom)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)

    def gohost(self, instance, val):    #Function to take the user to see the details of the clicked hostel.
        id = int(val)
        with open('pbl_app\\main_ram.txt', 'w') as file:
            file.write(self.host[id] + '\n')
            file.write(self.area[id] + '\n')
            file.write(str(self.rate[id]) + '\n')
            file.write(self.type[id] + '\n')

        self.manager.transition = FadeTransition()
        self.manager.current = "hostelpage"
    def goflat(self, instance):    #Function to take the user to see the details of the clicked flat.
        self.manager.transition = FadeTransition()
        self.manager.current = "flatpage"
    def goroom(self, instance):    #Function to take the user to see the details of the clicked user.
        self.manager.transition = FadeTransition()
        self.manager.current = "roompage"

    def search(self, instance):    #Function to search for all the properties in the area entered at the text box.
        area = self.textinput.text
        for button in self.buttons:
            button.text = f"Area :{self.textinput.text}"     

    def tools(self,instance):    #Functions to show all the other features offered by the project.
        self.manager.transition = CardTransition(direction = "right", mode = "push")
        self.manager.current = "toolpage"

class ToolPage(Screen):
    """
    This is the tool page which displays all the features available for the user to choose.

    The user can choose to see messages, see profile, check for teams, upgrades, saved profiles,
    terms & policies, be a landlord, FAQs, settings and AI assistent(Not started yet)

    back button: Takes the user back to main screen.
    message button: Shows all the messages received and also sends messages.
    profile button: Takes the user to profile page, can also change account or log-in.
    team button: Shows all the teams formed by other users. Can join or create own team.
    saved button: Shows all the profiles saved by the user.
    upgrades button: Here the user can make purchases. It can be calls, messages and subscription.
    terms button: Shows all the terms & conditions that the user needs to agree on.
    landlord button: Takes the user to a website where they can be a landlord.
    faq button: For Answerable Questions.
    settings button: Just what the name suggests.
    Assistant button: Coming soon.
    """
    def __init__(self,**kwargs):    #Initialization of the screen/page.
        super(ToolPage,self).__init__(**kwargs)
        #Making of a widget holder to store all the widgets.
        layout = BoxLayout(orientation = 'vertical')
        #Widget holder for the top part of the page
        top_box = BoxLayout(orientation = 'horizontal', size_hint = (1.0, 0.2))
        back_btn = Button(text = "Back", on_press = self.back, size_hint = (0.2, 1.0))
        logo_image = Image(source = 'user_logo.png', size_hint = (0.3, 1.0))
        user_name = LBLabel(text="user_name")
        mess_btn = Button(text = "message", on_press = self.mess, size_hint = (0.2, 1.0))
        #Adding of widgets to the holder.
        top_box.add_widget(back_btn)
        top_box.add_widget(logo_image)
        top_box.add_widget(user_name)
        top_box.add_widget(mess_btn)

        #Widgets holder for all the features.
        btn_box = BoxLayout(orientation = "vertical")
        prof_btn = Button(text = "Profile", on_press = self.prof)
        team_btn = Button(text = "Team", on_press = self.team)
        saved_btn = Button(text = "Saved", on_press = self.save)
        upgrade_btn = Button(text = "Upgrades", on_press = self.upgrade)
        term_btn = Button(text = "Terms & Policies", on_press = self.term)
        land_btn = Button(text = "Be a Landlord", on_press = self.land)
        #Adding of widgets to the holder.
        btn_box.add_widget(prof_btn)
        btn_box.add_widget(team_btn)
        btn_box.add_widget(saved_btn)
        btn_box.add_widget(upgrade_btn)
        btn_box.add_widget(term_btn)
        btn_box.add_widget(land_btn)

        #Adding a seperation for widgets placements.
        sepa = BoxLayout(size_hint = (1.0, 0.2))
        line = Color(0,0,0,1)
        sepa.canvas.add(Line(points = (0,0, layout.width, 1), color = line))

        #Final widgets holder.
        bot = BoxLayout(size_hint = (1.0, 0.2))
        faq_btn = Button(text = "FAQs", on_press = self.faq)
        set_btn = Button(text = "Settings", on_press = self.setf)
        chat_btn = Button(text = "Chat Bot", on_press = self.chat)
        bot.add_widget(faq_btn)
        bot.add_widget(set_btn)
        bot.add_widget(chat_btn)

        #Saving all the widgets and holders to the page.
        layout.add_widget(top_box)
        layout.add_widget(btn_box)
        layout.add_widget(sepa)
        layout.add_widget(bot)
        self.add_widget(layout)

    def back(self, instance):    #Function to transfer user to main page.
        self.manager.transition = CardTransition(direction = "left", mode = "pop")
        self.manager.current = "mainpage"

    def mess(self,instance):    #Function to transfer user to message page.
        self.manager.transition = FadeTransition()
        self.manager.current = "messagepage"
    
    def prof(self,instance):    #Function to transfer user to profile page.
        self.manager.transition = FadeTransition()
        self.manager.current = "profilepage"
    def team(self, instance):    #Function to transfer user to team page.
        self.manager.transition = FadeTransition()
        self.manager.current = "teampage"
    def save(self, instance):    #Function to transfer user to saved page
        self.manager.transition = FadeTransition()
        self.manager.current = "savedpage"
    def upgrade(self, instance):    #Function to transfer used to upgrade page.
        self.manager.transition = FadeTransition()
        self.manager.current = "upgradepage"
    def term(self, instance):    #Function to transfer used to terms page.
        self.manager.transition = FadeTransition()
        self.manager.current = "termspage"
    def land(self, instance):    #Function to transfer user to website for being a landlord.
        website_link = "www.google.com"
        webbrowser.open(website_link)
    def faq(self, instance):    #Function to transfer user to FAQs page.
        self.manager.transition = FadeTransition()
        self.manager.current = "faqpage"
    def setf(self, instance):    #Function to transfer user to settings page.
        self.manager.transition = FadeTransition()
        self.manager.current = "settingspage"
    def chat(self, instance):    #Function to transfer user to chat bot page.
        self.manager.transition = FadeTransition()
        self.manager.current = "chatbotpage"

class MessagePage(Screen):
    """
    This page contains the message service.

    The user can see all the incoming messages, write a message, and chat with other users.
    """
    def __init__(self,**kwargs):
        super(MessagePage,self).__init__(**kwargs)
        #Outer most layer of widget holder
        layout = BoxLayout(orientation='vertical')

        #Widget holder for the top part of the screen.
        top_box = BoxLayout(orientation='horizontal', size_hint_y=0.15)
        back_button = Button(text='Back',size_hint_x = 0.2,  on_press=self.back)
        self.textinput = TextInput(hint_text='Search Messages')
        search_button = Button(text='Search',size_hint_x = 0.2, on_press=self.search)
        top_box.add_widget(back_button)
        top_box.add_widget(self.textinput)
        top_box.add_widget(search_button)

        #Options to choose between focused message(by other users) and other message(spam, advertisement etc.)
        toggle_box = BoxLayout(orientation='horizontal', size_hint_y=0.25)
        self.focused_button = ToggleButton(text='Focused', on_press=self.focus, state = "down")
        self.other_button = ToggleButton(text='Other', on_press=self.other)
        toggle_box.add_widget(self.focused_button)
        toggle_box.add_widget(self.other_button)

        #Shows all the income message.
        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(10):    #Temporarily makes random chats.
            htext = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            user_name = LBLabel(text = f"{htext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(user_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gomess)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)

        #This part is under construction
        #write = Button(text = "Write message", size_hint_y = 0.2, on_press = self.goto)

        #Adds all the widgets to the outer most widgets holder and saving it to the screen.
        layout.add_widget(top_box)
        layout.add_widget(toggle_box)
        layout.add_widget(self.scroll)
        #layout.add_widget(write)
        self.add_widget(layout)

    def back(self, instance):    #Function to take user back to the tools page.
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"
    def search(self, instance):    #Search for specific user's message.
        area = self.textinput.text
        if area:
            self.grid.clear_widgets()
            self.scroll.clear_widgets()
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = LBLabel(text = f"#image", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            user_name = LBLabel(text = f"{area}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(user_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gomess)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.scroll.add_widget(self.grid)

    def goto(self, instance):    #under construction
        self.manager.transition = FadeTransition()
        self.manager.current = "blank"
    def gomess(self, instance):    #Transfer the user to see in detail the messages of the selected user.
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "messpage"
    def focus(self, instance):    #Shows all the focused messages on the screen. Mainly from all users.
        self.other_button.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        for i in range(5):
            htext = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            user_name = LBLabel(text = f"{htext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(user_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.gomess)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)
    def other(self, instance):    #Shows all the other messages on the screem. Namely spam, advertisement, sponser.
        self.focused_button.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        for i in range(5):
            htext = random.choice(["Ad", "Promotion", "Sponser", "Spam", "Fraud"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = LBLabel(text = f"#image{i+1}", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            user_name = LBLabel(text = f"{htext}")
            sep_name = LBLabel(text = "_"*100)
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
        label = LBLabel(text = "Profile      ")
        account_btn = Button(text = "Account", size_hint_x = 0.3, on_press = self.account)
        top.add_widget(back_btn)
        top.add_widget(label)
        top.add_widget(account_btn)
        grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.2)
        logo = Image(source='logo.png', size_hint=(0.3, 1.0))
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text='Username: Ruhan')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text='Area: Akurdi', size_hint=(0.7, 1.0))
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
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = "gender : male", font_size = 30)
        age = LBLabel(text = "age : 21", font_size = 30)
        study = LBLabel(text = "Years of study : FE", font_size = 30)
        branch = LBLabel(text = "Branch : CS", font_size = 30)
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
        pre_label = LBLabel(text = "Preference:")
        edit_pre_btn = Button(text = "edit", size_hint_x = 0.2, on_press = self.edit_pre)
        bot_top.add_widget(pre_label)
        bot_top.add_widget(edit_pre_btn)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in pre_list:
            pre_pre_label = LBLabel(text = f"{i}")
            bot_grid.add_widget(pre_pre_label)
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
        label= LBLabel(text = "Edit Profile")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        img_lay = BoxLayout(size_hint_y = 0.3)
        img = Image(source = 'user.png', size_hint_x = 0.2)
        img_btn = Button(text = "change", on_press = self.change_img, size_hint = (None, None), height = 200)
        img_label = LBLabel(text = "", size_hint_x = 0.4)
        img_lay.add_widget(img)
        img_lay.add_widget(img_btn)
        img_btn.add_widget(img_label)
        layout.add_widget(img_lay)

        grid = GridLayout(cols = 2)
        name_label = LBLabel(text = "Name:", size_hint_x = 0.25)
        name_text = TextInput(hint_text = "enter your name", text = "Ruhan")
        place_label = LBLabel(text = "Place:", size_hint_x = 0.25)
        place_text = TextInput(hint_text = "enter your place", text = "Akurdi")
        ph_label = LBLabel(text = "Phone no:", size_hint_x = 0.25)
        ph_text = TextInput(hint_text = "enter your phone number", text = "3141592653")
        email_label = LBLabel(text = "Email:", size_hint_x = 0.25)
        email_text = TextInput(hint_text = "enter your email address", text = "babablacksheep@gmail.com")
        gender_label = LBLabel(text = "Gender:", size_hint_x = 0.25)
        gender_text = TextInput(hint_text = "enter your gender", text = "Male")
        age_label = LBLabel(text = "Age:", size_hint_x = 0.25)
        age_text = TextInput(hint_text = "enter your age", text = "21")
        study_label = LBLabel(text = "Year of study:", size_hint_x = 0.25)
        study_text = TextInput(hint_text = "enter your year of study", text = "1st")
        branch_label = LBLabel(text = "Branch:", size_hint_x = 0.25)
        branch_text = TextInput(hint_text = "enter your Branch", text = "CS")
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
        log_label = LBLabel(text = "Account")
        top.add_widget(back_btn)
        top.add_widget(log_label)
        layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        email_box = BoxLayout()
        email_label = LBLabel(text = "Email", halign = "left", size_hint_x = 0.3)
        email_text = TextInput(hint_text = "Enter email")
        email_box.add_widget(email_label)
        email_box.add_widget(email_text)
        pass_box = BoxLayout()
        pass_label = LBLabel(text = "Password", halign = "left", size_hint_x = 0.3)
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

class TeamPage(Screen):
    def __init__(self, **kwargs):
        super(TeamPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y= 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Team")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        self.buttons = []
        for i in range(20):
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            atext = random.choice(["Akurdi", "Pimpri", "Lonavala", "Pune", "Vashi", "Nerul", "Ulwe", "Mumbai"])
            ttext = random.choice(["Boys", "Girls", "All"])
            mtext = random.randint(1,5)
            btn_layout = BoxLayout(size_hint_y = None, height = 300)
            btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"Hostel {htext}")
            area_name = LBLabel(text = f"Area: {atext}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Type: {ttext}")
            member_name = LBLabel(text = f"Member count: {mtext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(member_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.goteam)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)

        create_btn = Button(text = "Create", size_hint_y = 0.2, on_press = self.create)
        #layout.add_widget(create_btn)


        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "toolpage"

    def goteam(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "jointeampage"
    def create(self, instance):
        pass

class JoinTeamPage(Screen):
    def __init__(self, **kwargs):
        super(JoinTeamPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Team details:")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
        rtext = random.randint(1, 9)
        atext = random.choice(["Akurdi", "Pimpri", "Lonavala", "Pune", "Vashi", "Nerul", "Ulwe", "Mumbai"])
        ttext = random.choice(["Boys", "Girls", "All"])
        mtext = random.randint(1,5)
        self.btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        self.btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Hostel {htext}")
        area_name = LBLabel(text = f"Area: {atext}")
        rate_name = LBLabel(text = f"Rate: {rtext * 500}")
        type_name = LBLabel(text = f"Type: {ttext}")
        member_name = LBLabel(text = f"Member count: {mtext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(member_name)
        in_btn_layout.add_widget(sep_name)
        self.btn_layout.add_widget(in_btn_layout)
        self.layout.add_widget(self.btn_layout)

        self.mid = BoxLayout(orientation = "vertical")
        mem_label = LBLabel(text = "Members:")
        self.mid.add_widget(mem_label)
        for i in range(mtext):
            mem_box = BoxLayout()
            ut = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            user_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            user_name = LBLabel(text = f"{ut}", size_hint_x = None, width = 150)
            user_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.user)
            mem_box.add_widget(user_img)
            mem_box.add_widget(user_name)
            mem_box.add_widget(user_btn)
            self.mid.add_widget(mem_box)
        self.layout.add_widget(self.mid)

        bot = BoxLayout(size_hint_y = 0.2)
        self.join_btn = Button(text = "Join", on_press = self.join)
        self.leave_btn = Button(text = "Leave", on_press = self.leave, disabled = True)
        bot.add_widget(self.join_btn)
        bot.add_widget(self.leave_btn)
        self.layout.add_widget(bot)

        self.add_widget(self.layout)

    def back(self, instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "teampage"
        self.layout.clear_widgets()
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Team details:")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
        rtext = random.randint(1, 9)
        atext = random.choice(["Akurdi", "Pimpri", "Lonavala", "Pune", "Vashi", "Nerul", "Ulwe", "Mumbai"])
        ttext = random.choice(["Boys", "Girls", "All"])
        mtext = random.randint(1,5)
        self.btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        self.btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Hostel {htext}")
        area_name = LBLabel(text = f"Area: {atext}")
        rate_name = LBLabel(text = f"Rate: {rtext * 500}")
        type_name = LBLabel(text = f"Type: {ttext}")
        member_name = LBLabel(text = f"Member count: {mtext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(member_name)
        in_btn_layout.add_widget(sep_name)
        self.btn_layout.add_widget(in_btn_layout)
        self.layout.add_widget(self.btn_layout)

        self.mid = BoxLayout(orientation = "vertical")
        mem_label = LBLabel(text = "Members:")
        self.mid.add_widget(mem_label)
        for i in range(mtext):
            mem_box = BoxLayout()
            ut = random.choice(["Ruhan", "Yash", "Atul", "Prem", "Ayush", "Mayur"])
            user_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            user_name = LBLabel(text = f"{ut}")
            user_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.user)
            mem_box.add_widget(user_img)
            mem_box.add_widget(user_name)
            mem_box.add_widget(user_btn)
            self.mid.add_widget(mem_box)
        self.layout.add_widget(self.mid)

        bot = BoxLayout(size_hint_y = 0.2)
        self.join_btn = Button(text = "Join", on_press = self.join)
        self.leave_btn = Button(text = "Leave", on_press = self.leave, disabled = True)
        bot.add_widget(self.join_btn)
        bot.add_widget(self.leave_btn)
        self.layout.add_widget(bot)
       
    def user(self, instance):
        self.manager.transition = CardTransition(direction = "left", mode = "push")
        self.manager.current = "teamuserpage"
    def join(self,instance):
        self.join_btn.disabled = True
        self.leave_btn.disabled = False
    def leave(self, instance):
        self.leave_btn.disabled = True
        self.join_btn.disabled = False

class SavedPage(Screen):
    def __init__(self, **kwargs):
        super(SavedPage, self).__init__(**kwargs)
        out = BoxLayout(orientation = "vertical")
        top1 = BoxLayout(size_hint = (1.0, 0.1))
        top2 = BoxLayout(size_hint = (1.0, 0.1))
        top3 = BoxLayout(size_hint = (1.0, 0.1))

        back_btn = Button(text = "Back", on_press = self.back, size_hint_x = 0.2)
        blank = LBLabel(text = "Saved")
        top1.add_widget(back_btn)
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
        for i in range(20):
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size_hint_y = None, height = 200)
            btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"Hostel {htext}")
            area_name = LBLabel(text = f"Area :{self.textinput.text}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Type: {ttext}")
            sep_name = LBLabel(text = "_"*100)
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
        for i in range(20):
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size_hint_y = None, height = 200)
            btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"Hostel {htext}")
            area_name = LBLabel(text = f"Area :{self.textinput.text}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Type: {ttext}")
            sep_name = LBLabel(text = "_"*100)
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

    def flat_func(self, instance):
        self.hostel_btn.state = "normal"
        self.roommate_btn.state = "normal"
        self.grid.clear_widgets()
        self.scroll.clear_widgets()
        self.buttons = []
        for i in range(20):
            htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Boys", "Girls", "All"])
            btn_layout = BoxLayout(size_hint_y = None, height = 200)
            btn_img = Image(source = f"pbl_app\\image_dir\\flat{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"Flat {htext}")
            area_name = LBLabel(text = f"Area :{self.textinput.text}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Type: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
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
        for i in range(20):
            htext = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            rtext = random.randint(1, 9)
            ttext = random.choice(["Room", "Roommate"])
            btn_layout = BoxLayout(size_hint_y = None, height = 200)
            btn_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"{htext}")
            area_name = LBLabel(text = f"Area :{self.textinput.text}")
            rate_name = LBLabel(text = f"Rate: {rtext * 500}")
            type_name = LBLabel(text = f"Searching for: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(area_name)
            in_btn_layout.add_widget(rate_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.goroom)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
            self.buttons.append(area_name)
        self.scroll.add_widget(self.grid)

    def gohost(self, instance):
        self.manager.transiton = FadeTransition()
        self.manager.current = "savehostelpage"
    def goflat(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "saveflatpage"
    def goroom(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "saveroompage"

    def search(self, instance):
        area = self.textinput.text
        for button in self.buttons:
            button.text = f"Area :{self.textinput.text}"
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

        otp_label = LBLabel(text = "OTP: (send on email)", size_hint_y = 0.15)
        otp_text = TextInput(hint_text = "Enter OTP", size_hint_y = 0.15)
        otp_btn = Button(text = "Resend OTP", on_press = self.resend, size_hint_y = 0.15)
        newpass_label = LBLabel(text = "New Password", size_hint_y = 0.15)
        newpass_text = TextInput(hint_text = "Enter new password", size_hint_y = 0.15)
        repass_label = LBLabel(text = "Re-enter Password", size_hint_y = 0.15)
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
        sign_label = LBLabel(text = "Sign in")
        top.add_widget(back_btn)
        top.add_widget(sign_label)
        layout.add_widget(top)

        user_label = LBLabel(text = "User Name:", size_hint_y = 0.12)
        user_text = TextInput(hint_text = "Enter user name", size_hint_y = 0.12)
        email_label = LBLabel(text = "Email:", size_hint_y = 0.12)
        email_text = TextInput(hint_text = "Enter email", size_hint_y = 0.12)
        ph_label = LBLabel(text = "Phone number:", size_hint_y = 0.12)
        ph_text = TextInput(hint_text = "Enter phone number", size_hint_y = 0.12)
        pass_label = LBLabel(text = "Password:", size_hint_y = 0.12)
        pass_text = TextInput(hint_text = "Enter password", size_hint_y = 0.12)
        repass_label = LBLabel(text = "Re-enter Password:", size_hint_y = 0.12)
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
        edit_label = LBLabel(text = "Edit Preference")
        top.add_widget(back_btn)
        top.add_widget(edit_label)
        layout.add_widget(top)

        grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in pre_list:
            pre_box = BoxLayout(orientation = "vertical")
            pre_btn = ToggleButton(text = f"{i}", size_hint_y = 0.4)
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
        faq_label = LBLabel(text = "FAQs")
        top.add_widget(back_btn)
        top.add_widget(faq_label)
        layout.add_widget(top)

        bot = BoxLayout(orientation = "vertical")
        prob_label = LBLabel(text = "Problem Statement:")
        prob_text = TextInput(text = "A solution for college students\nto find hostel/flat/roommate", multiline = True, readonly = True)
        team_label = LBLabel(text = "Team Members:")
        team_text = TextInput(text = "- Ruhan Saad Dave\n- Yash Sanjay Chavan\n- Prem Gautam Gavhane\n- Ayush\n- Mayur Abhay Sadguru\nAtul Govind Sangale", multiline = True, readonly = True)
        tool_label = LBLabel(text = "Tools used in building this app:")
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
        label = LBLabel(text = "Upgrade")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        call_box = BoxLayout()
        call_label = LBLabel(text = "Calls left:")
        self.call_value_label = LBLabel(text = "0")
        call_box.add_widget(call_label)
        call_box.add_widget(self.call_value_label)
        layout.add_widget(call_box)

        message_box = BoxLayout()
        message_label = LBLabel(text = "Messages left:")
        self.message_value_label = LBLabel(text = "0")
        message_box.add_widget(message_label)
        message_box.add_widget(self.message_value_label)
        layout.add_widget(message_box)

        sub_box = BoxLayout()
        sub_label = LBLabel(text = "Subscriptin end date:")
        self.sub_value_label = LBLabel(text = "0 months")
        sub_box.add_widget(sub_label)
        sub_box.add_widget(self.sub_value_label)
        layout.add_widget(sub_box)

        purchase_label = RLabel(text = "Purchase:")
        layout.add_widget(purchase_label)

        call_option = BoxLayout()
        for i in range(4):
            in_call_box = BoxLayout(orientation = "vertical")
            in_call_label = LBLabel(text = f"{i+1} call", size_hint_y = 0.65)
            in_call_btn = Button(text = f"Rs. {(i+1)*10}", on_press = self.call)
            in_call_box.add_widget(in_call_label)
            in_call_box.add_widget(in_call_btn)
            call_option.add_widget(in_call_box)
        layout.add_widget(call_option)

        message_option = BoxLayout()
        for i in range(4):
            in_message_box = BoxLayout(orientation = "vertical")
            in_message_label = LBLabel(text = f"{(i+1)*10} message", size_hint_y = 0.65)
            in_message_btn = Button(text = f"Rs. {(i+1)*10}", on_press = self.message)
            in_message_box.add_widget(in_message_label)
            in_message_box.add_widget(in_message_btn)
            message_option.add_widget(in_message_box)
        layout.add_widget(message_option)

        sub_option = BoxLayout()
        for i in range(4):
            in_sub_box = BoxLayout(orientation = "vertical")
            in_sub_label = LBLabel(text = f"{i+1} month subscription", size_hint_y = 0.65)
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
        count = int(self.call_value_label.text)
        count += random.randint(1,4)
        self.call_value_label.text = f"{count}"

    def message(self, instance):
        count = int(self.message_value_label.text)
        count += random.randint(1,4)
        count *= 10
        self.message_value_label.text = f"{count}"
    def sub(self, instance):
        count = int(self.sub_value_label.text[0])
        count += random.randint(1,4)
        self.sub_value_label.text = f"{count} months"

class TermsPage(Screen):
    def __init__(self, **kwargs):
        super(TermsPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Terms & Policies")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        #reading contents of terms.txt file and putting it it the textinput
        with open("pbl_app\\terms.txt", "r") as f:
            terms = f.read()
        term_text = TextInput(text = terms, multiline = True, readonly = True)
        layout.add_widget(term_text)

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
        label = LBLabel(text = "Settings")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        self.audio_slider = Slider(min = 0, max = 100, value = 50)
        self.audio_label = LBLabel(text = f"Audio: {self.audio_slider.value}")
        mid.add_widget(self.audio_label)
        mid.add_widget(self.audio_slider)
        self.brightness_label = Label(text="Brightness: 0")
        self.brightness_slider = Slider(min=0, max=1, value=0.5)
        mid.add_widget(self.brightness_label)
        mid.add_widget(self.brightness_slider)
        noti_box = BoxLayout()
        noti_label = LBLabel(text = "Notification:")
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
            self.noti_btn.text = "On"
        else:
            self.noti_btn.text = "off"

class HostelPage(Screen):
    def __init__(self, **kwargs):
        super(HostelPage, self).__init__(**kwargs)

        word_list = []    #This part is used to retrive information from the selected hostel, to avoid chaos.
        count = 0
        with open('pbl_app\\main_ram.txt', 'r') as file:
            for line in file:
                word_list.append(line.strip())
                count += 1
            file.close()
        if count < 4:
            word_list = ['','',0,'']

        self.layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Hostel")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        htext = word_list[0]
        atext = word_list[1]
        rtext = int(word_list[2])
        ttext = word_list[3]
        btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Hostel {htext}")
        area_name = LBLabel(text = f"Area :{atext}")
        rate_name = LBLabel(text = f"Rate: {rtext}")
        type_name = LBLabel(text = f"Type: {ttext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(sep_name)
        btn_layout.add_widget(in_btn_layout) 
        self.layout.add_widget(btn_layout)

        sic =  BoxLayout(size_hint_y = 0.2)
        self.save_btn = ToggleButton(text = "Save", on_press = self.save)
        inter_btn = Button(text = "Interested", on_press = self.inter)
        call_btn = Button(text = "Call", on_press = self.call)
        sic.add_widget(self.save_btn)
        sic.add_widget(inter_btn)
        sic.add_widget(call_btn)
        self.layout.add_widget(sic)

        fac_label = LBLabel(text = "Facilities", size_hint_y = 0.2)
        self.layout.add_widget(fac_label)
        fac_grid = GridLayout(cols = 4)
        for i in range(random.randint(3,8)):
            txt = random.choice(["wifi", "Washing machine", "Cupboard", "Private washroom", "Gyser", "Water purifier", "Gym", "Garden", "Library", "Mess", "Computer centre"])
            fac_btn = Button(text = f"{txt}", disabled = True)
            fac_grid.add_widget(fac_btn)
        self.layout.add_widget(fac_grid)

        self.add_widget(self.layout)
        
    def back(self, instance):
        self.save_btn.state = "normal"
        self.save_btn.text = "save"
        self.manager.transition = FadeTransition()
        self.manager.current = "mainpage"
        self.layout.clear_widgets()
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Flat")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        word_list = []    #This part is used to retrive information from the selected hostel, to avoid chaos.
        count = 0
        with open('pbl_app\\main_ram.txt', 'r') as file:
            for line in file:
                word_list.append(line.strip())
                count += 1
            file.close()
        if count < 4:
            word_list = ['','',0,'']
        htext = word_list[0]
        atext = word_list[1]
        rtext = int(word_list[2])
        ttext = word_list[3]
        btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Hostel {htext}")
        area_name = LBLabel(text = f"Area :{atext}")
        rate_name = LBLabel(text = f"Rate: {rtext * 500}")
        type_name = LBLabel(text = f"Type: {ttext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(sep_name)
        btn_layout.add_widget(in_btn_layout)
        self.layout.add_widget(btn_layout)

        sic =  BoxLayout(size_hint_y = 0.2)
        self.save_btn = ToggleButton(text = "Save", on_press = self.save)
        inter_btn = Button(text = "Interested", on_press = self.inter)
        call_btn = Button(text = "Call", on_press = self.call)
        sic.add_widget(self.save_btn)
        sic.add_widget(inter_btn)
        sic.add_widget(call_btn)
        self.layout.add_widget(sic)

        fac_label = LBLabel(text = "Facilities", size_hint_y = 0.2)
        self.layout.add_widget(fac_label)
        fac_grid = GridLayout(cols = 4)
        for i in range(random.randint(1,8)):
            txt = random.choice(["wifi", "Washing machine", "Cupboard", "Private washroom", "Gyser", "Water purifier", "Gym", "Garden", "Library", "Mess", "Computer centre"])
            fac_btn = Button(text = f"{txt}", disabled = True)
            fac_grid.add_widget(fac_btn)
        self.layout.add_widget(fac_grid)    
        
    def save(self, instance):
        if self.save_btn.state == "down":
            self.save_btn.text = "saved"
        elif self.save_btn.state == "normal":
            self.save_btn.text = "save"
    def inter(self, instance):
        self.manager.transition = CardTransition(direction = "down", mode = "push")
        self.manager.current = "hostelinterestpage"
    def call(self, instance):
        self.manager.transition = CardTransition(direction = "down", mode = "push")
        self.manager.current = "callpage"

class FlatPage(Screen):
    def __init__(self, **kwargs):
        super(FlatPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Flat")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
        rtext = random.randint(1, 9)
        ttext = random.choice(["Boys", "Girls", "All"])
        atext = random.choice(["Akurdi", "Pimpri", "Lonavala", "Pune", "Vashi", "Nerul", "Ulwe", "Mumbai"])
        btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\flat{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Flat {htext}")
        area_name = LBLabel(text = f"Area :{atext}")
        rate_name = LBLabel(text = f"Rate: {rtext * 500}")
        type_name = LBLabel(text = f"Type: {ttext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(sep_name)
        btn_layout.add_widget(in_btn_layout)
        self.layout.add_widget(btn_layout)

        sic =  BoxLayout(size_hint_y = 0.2)
        self.save_btn = ToggleButton(text = "Save", on_press = self.save)
        inter_btn = Button(text = "Interested", on_press = self.inter)
        call_btn = Button(text = "Call", on_press = self.call)
        sic.add_widget(self.save_btn)
        sic.add_widget(inter_btn)
        sic.add_widget(call_btn)
        self.layout.add_widget(sic)

        fac_label = LBLabel(text = "Facilities", size_hint_y = 0.2)
        self.layout.add_widget(fac_label)
        fac_grid = GridLayout(cols = 4)
        for i in range(random.randint(1,8)):
            txt = random.choice(["wifi", "Washing machine", "Cupboard", "Private washroom", "Gyser", "Water purifier", "Gym", "Garden", "Library", "Mess", "Computer centre"])
            fac_btn = Button(text = f"{txt}", disabled = True)
            fac_grid.add_widget(fac_btn)
        self.layout.add_widget(fac_grid)

        self.add_widget(self.layout)
        
    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "mainpage"
        self.layout.clear_widgets()
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Flat")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
        rtext = random.randint(1, 9)
        ttext = random.choice(["Boys", "Girls", "All"])
        atext = random.choice(["Akurdi", "Pimpri", "Lonavala", "Pune", "Vashi", "Nerul", "Ulwe", "Mumbai"])
        btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\flat{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Flat {htext}")
        area_name = LBLabel(text = f"Area :{atext}")
        rate_name = LBLabel(text = f"Rate: {rtext * 500}")
        type_name = LBLabel(text = f"Type: {ttext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(sep_name)
        btn_layout.add_widget(in_btn_layout)
        self.layout.add_widget(btn_layout)

        sic =  BoxLayout(size_hint_y = 0.2)
        self.save_btn = ToggleButton(text = "Save", on_press = self.save)
        inter_btn = Button(text = "Interested", on_press = self.inter)
        call_btn = Button(text = "Call", on_press = self.call)
        sic.add_widget(self.save_btn)
        sic.add_widget(inter_btn)
        sic.add_widget(call_btn)
        self.layout.add_widget(sic)

        fac_label = LBLabel(text = "Facilities", size_hint_y = 0.2)
        self.layout.add_widget(fac_label)
        fac_grid = GridLayout(cols = 4)
        for i in range(random.randint(1,8)):
            txt = random.choice(["wifi", "Washing machine", "Cupboard", "Private washroom", "Gyser", "Water purifier", "Gym", "Garden", "Library", "Mess", "Computer centre"])
            fac_btn = Button(text = f"{txt}", disabled = True)
            fac_grid.add_widget(fac_btn)
        self.layout.add_widget(fac_grid)
        
    def save(self, instance):
        if self.save_btn.state == "down":
            self.save_btn.text = "saved"
        elif self.save_btn.state == "normal":
            self.save_btn.text = "save"
    def inter(self, instance):
        self.manager.transition = CardTransition(direction = "down", mode = "push")
        self.manager.current = "flatinterestpage"
    def call(self, instance):
        self.manager.transition = CardTransition(direction = "down", mode = "push")
        self.manager.current = "callpage"

class RoomPage(Screen):
    def __init__(self, **kwargs):
        super(RoomPage, self).__init__(**kwargs)
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height = self.grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text= f"Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}")
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

        self.add_widget(self.grid)

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "mainpage"
        self.grid.clear_widgets()
        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f"Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}")
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

class MessPage(Screen):
    def __init__(self, **kwargs):
        super(MessPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = f"User name: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(random.randint(2,10)):
            user = random.choice(["You", "Them"])
            answer = random.choice(["Hi", "Hello", "How are you?", "Wassup?", "Im good", "Im fine","How about you?","Just a regular coversation..."])
            btn_layout = BoxLayout(size_hint_y = None, height = 50)
            btn_img = LBLabel(text = f"{user}", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            user_text = LBLabel(text = f"{answer}")
            btn_layout.add_widget(user_text)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)
        mid.add_widget(self.scroll)
        self.layout.add_widget(mid)

        bot = BoxLayout(size_hint_y = 0.2)
        self.textinput = TextInput(hint_text = "Enter something?")
        send_btn = Button(text = "Send", size_hint_x = 0.2, on_press = self.send)
        bot.add_widget(self.textinput)
        bot.add_widget(send_btn)
        self.layout.add_widget(bot)

        self.add_widget(self.layout)
        
    def back(self, instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "messagepage"
        self.layout.clear_widgets()
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = f"Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(random.randint(2,10)):
            user = random.choice(["You", "Them"])
            answer = random.choice(["Hi", "Hello", "How are you?", "Wassup?", "Im good", "Im fine","How about you?","Just a regular coversation..."])
            btn_layout = BoxLayout(size_hint_y = None, height = 50)
            btn_img = LBLabel(text = f"{user}", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            user_text = LBLabel(text = f"{answer}")
            btn_layout.add_widget(user_text)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)
        mid.add_widget(self.scroll)
        self.layout.add_widget(mid)

        bot = BoxLayout(size_hint_y = 0.2)
        self.textinput = TextInput(hint_text = "Enter something?")
        send_btn = Button(text = "Send", size_hint_x = 0.2, on_press = self.send)
        bot.add_widget(self.textinput)
        bot.add_widget(send_btn)
        self.layout.add_widget(bot)

    def send(self,instance):
        btn_layout = BoxLayout(size_hint_y = None, height = 50)
        btn_img = LBLabel(text = f"You:", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        user_text = LBLabel(text = f"{self.textinput.text}")
        self.textinput.text = ""
        btn_layout.add_widget(user_text)
        self.grid.add_widget(btn_layout)

class HostelInterestPage(Screen):
    def __init__(self, **kwargs):
        super(HostelInterestPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Interested users.")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(4):    ##Displays the details one by one, for now just showing random details, but later will fix it
            htext = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            ttext = random.choice(["Room", "Roommate"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"{htext}")
            type_name = LBLabel(text = f"Searching for: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.seeuser)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)
        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = CardTransition(direction = "up", mode = "pop")
        self.manager.current = "hostelpage"

    def seeuser(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "hostintuserpage"

class HostIntUserPage(Screen):
    def __init__(self, **kwargs):
        super(HostIntUserPage, self).__init__(**kwargs)
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height = self.grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

        self.add_widget(self.grid)

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "hostelinterestpage"
        self.grid.clear_widgets()
        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

class FlatInterestPage(Screen):
    def __init__(self, **kwargs):
        super(FlatInterestPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Interested users.")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(4):    ##Displays the details one by one, for now just showing random details, but later will fix it
            htext = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            ttext = random.choice(["Room", "Roommate"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"{htext}")
            type_name = LBLabel(text = f"Searching for: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.seeuser)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)
        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = CardTransition(direction = "up", mode = "pop")
        self.manager.current = "flatpage"

    def seeuser(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "flatintuserpage"

class FlatIntUserPage(Screen):
    def __init__(self, **kwargs):
        super(FlatIntUserPage, self).__init__(**kwargs)
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height = self.grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

        self.add_widget(self.grid)

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "flatinterestpage"
        self.grid.clear_widgets()
        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

class TeamUserPage(Screen):
    def __init__(self, **kwargs):
        super(TeamUserPage, self).__init__(**kwargs)
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height = self.grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

        self.add_widget(self.grid)

    def back(self,instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "jointeampage"
        self.grid.clear_widgets()
        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

class SaveHostelInterestPage(Screen):
    def __init__(self, **kwargs):
        super(SaveHostelInterestPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Interested users.")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(4):    ##Displays the details one by one, for now just showing random details, but later will fix it
            htext = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            ttext = random.choice(["Room", "Roommate"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"{htext}")
            type_name = LBLabel(text = f"Searching for: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.seeuser)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)
        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = CardTransition(direction = "up", mode = "pop")
        self.manager.current = "savehostelpage"

    def seeuser(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "savehostintuserpage"

class SaveHostIntUserPage(Screen):
    def __init__(self, **kwargs):
        super(SaveHostIntUserPage, self).__init__(**kwargs)
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height = self.grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

        self.add_widget(self.grid)

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "savehostelinterestpage"
        self.grid.clear_widgets()
        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = "Branch : CS", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

class SaveFlatInterestPage(Screen):
    def __init__(self, **kwargs):
        super(SaveFlatInterestPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Interested users.")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        for i in range(4):    ##Displays the details one by one, for now just showing random details, but later will fix it
            htext = random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])
            ttext = random.choice(["Room", "Roommate"])
            btn_layout = BoxLayout(size_hint_y = None, height = 150)
            btn_img = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
            btn_layout.add_widget(btn_img)
            in_btn_layout = BoxLayout(orientation = "vertical")
            host_name = LBLabel(text = f"{htext}")
            type_name = LBLabel(text = f"Searching for: {ttext}")
            sep_name = LBLabel(text = "_"*100)
            in_btn_layout.add_widget(host_name)
            in_btn_layout.add_widget(type_name)
            in_btn_layout.add_widget(sep_name)
            btn_layout.add_widget(in_btn_layout)
            go_btn = Button(text = "->", size_hint_x = 0.2, on_press = self.seeuser)
            btn_layout.add_widget(go_btn)
            self.grid.add_widget(btn_layout)
        self.scroll.add_widget(self.grid)
        layout.add_widget(self.scroll)
        self.add_widget(layout)

    def back(self, instance):
        self.manager.transition = CardTransition(direction = "up", mode = "pop")
        self.manager.current = "saveflatpage"

    def seeuser(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "saveflatintuserpage"

class SaveFlatIntUserPage(Screen):
    def __init__(self, **kwargs):
        super(SaveFlatIntUserPage, self).__init__(**kwargs)
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height = self.grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}")}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

        self.add_widget(self.grid)

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "saveflatinterestpage"
        self.grid.clear_widgets()
        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}")}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

class SaveHostelPage(Screen):
    def __init__(self, **kwargs):
        super(SaveHostelPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Hostel")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
        rtext = random.randint(1, 9)
        ttext = random.choice(["Boys", "Girls", "All"])
        atext = random.choice(["Akurdi", "Pimpri", "Lonavala", "Pune", "Vashi", "Nerul", "Ulwe", "Mumbai"])
        btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Hostel {htext}")
        area_name = LBLabel(text = f"Area :{atext}")
        rate_name = LBLabel(text = f"Rate: {rtext}")
        type_name = LBLabel(text = f"Type: {ttext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(sep_name)
        btn_layout.add_widget(in_btn_layout) 
        self.layout.add_widget(btn_layout)

        sic =  BoxLayout(size_hint_y = 0.2)
        self.save_btn = ToggleButton(text = "Save", on_press = self.save)
        inter_btn = Button(text = "Interested", on_press = self.inter)
        call_btn = Button(text = "Call", on_press = self.call)
        sic.add_widget(self.save_btn)
        sic.add_widget(inter_btn)
        sic.add_widget(call_btn)
        self.layout.add_widget(sic)

        fac_label = LBLabel(text = "Facilities", size_hint_y = 0.2)
        self.layout.add_widget(fac_label)
        fac_grid = GridLayout(cols = 4)
        for i in range(random.randint(3,8)):
            txt = random.choice(["wifi", "Washing machine", "Cupboard", "Private washroom", "Gyser", "Water purifier", "Gym", "Garden", "Library", "Mess", "Computer centre"])
            fac_btn = Button(text = f"{txt}", disabled = True)
            fac_grid.add_widget(fac_btn)
        self.layout.add_widget(fac_grid)

        self.add_widget(self.layout)
        
    def back(self, instance):
        self.save_btn.state = "normal"
        self.save_btn.text = "save"
        self.manager.transition = FadeTransition()
        self.manager.current = "savedpage"
        self.layout.clear_widgets()
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Flat")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        word_list = []    #This part is used to retrive information from the selected hostel, to avoid chaos.
        count = 0
        with open('pbl_app\\main_ram.txt', 'r') as file:
            for line in file:
                word_list.append(line.strip())
                count += 1
            file.close()
        if count < 4:
            word_list = ['','',0,'']
        htext = word_list[0]
        atext = word_list[1]
        rtext = int(word_list[2])
        ttext = word_list[3]
        btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\hostel{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Hostel {htext}")
        area_name = LBLabel(text = f"Area :{atext}")
        rate_name = LBLabel(text = f"Rate: {rtext * 500}")
        type_name = LBLabel(text = f"Type: {ttext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(sep_name)
        btn_layout.add_widget(in_btn_layout)
        self.layout.add_widget(btn_layout)

        sic =  BoxLayout(size_hint_y = 0.2)
        self.save_btn = ToggleButton(text = "Save", on_press = self.save)
        inter_btn = Button(text = "Interested", on_press = self.inter)
        call_btn = Button(text = "Call", on_press = self.call)
        sic.add_widget(self.save_btn)
        sic.add_widget(inter_btn)
        sic.add_widget(call_btn)
        self.layout.add_widget(sic)

        fac_label = LBLabel(text = "Facilities", size_hint_y = 0.2)
        self.layout.add_widget(fac_label)
        fac_grid = GridLayout(cols = 4)
        for i in range(random.randint(1,8)):
            txt = random.choice(["wifi", "Washing machine", "Cupboard", "Private washroom", "Gyser", "Water purifier", "Gym", "Garden", "Library", "Mess", "Computer centre"])
            fac_btn = Button(text = f"{txt}", disabled = True)
            fac_grid.add_widget(fac_btn)
        self.layout.add_widget(fac_grid)    
        
    def save(self, instance):
        if self.save_btn.state == "down":
            self.save_btn.text = "saved"
        elif self.save_btn.state == "normal":
            self.save_btn.text = "save"
    def inter(self, instance):
        self.manager.transition = CardTransition(direction = "down", mode = "push")
        self.manager.current = "savehostelinterestpage"
    def call(self, instance):
        self.manager.transition = CardTransition(direction = "down", mode = "push")
        self.manager.current = "callpage"

class SaveFlatPage(Screen):
    def __init__(self, **kwargs):
        super(SaveFlatPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Flat")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
        rtext = random.randint(1, 9)
        ttext = random.choice(["Boys", "Girls", "All"])
        atext = random.choice(["Akurdi", "Pimpri", "Lonavala", "Pune", "Vashi", "Nerul", "Ulwe", "Mumbai"])
        btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\flat{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Flat {htext}")
        area_name = LBLabel(text = f"Area :{atext}")
        rate_name = LBLabel(text = f"Rate: {rtext * 500}")
        type_name = LBLabel(text = f"Type: {ttext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(sep_name)
        btn_layout.add_widget(in_btn_layout)
        self.layout.add_widget(btn_layout)

        sic =  BoxLayout(size_hint_y = 0.2)
        self.save_btn = ToggleButton(text = "Save", on_press = self.save)
        inter_btn = Button(text = "Interested", on_press = self.inter)
        call_btn = Button(text = "Call", on_press = self.call)
        sic.add_widget(self.save_btn)
        sic.add_widget(inter_btn)
        sic.add_widget(call_btn)
        self.layout.add_widget(sic)

        fac_label = LBLabel(text = "Facilities", size_hint_y = 0.2)
        self.layout.add_widget(fac_label)
        fac_grid = GridLayout(cols = 4)
        for i in range(random.randint(1,8)):
            txt = random.choice(["wifi", "Washing machine", "Cupboard", "Private washroom", "Gyser", "Water purifier", "Gym", "Garden", "Library", "Mess", "Computer centre"])
            fac_btn = Button(text = f"{txt}", disabled = True)
            fac_grid.add_widget(fac_btn)
        self.layout.add_widget(fac_grid)

        self.add_widget(self.layout)
        
    def back(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "savedpage"
        self.layout.clear_widgets()
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Flat")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        htext = random.choice(["Krishna", "A1", "Roshani", "Patil", "Royal", "Paradise", "Zolo"])
        rtext = random.randint(1, 9)
        ttext = random.choice(["Boys", "Girls", "All"])
        atext = random.choice(["Akurdi", "Pimpri", "Lonavala", "Pune", "Vashi", "Nerul", "Ulwe", "Mumbai"])
        btn_layout = BoxLayout(size_hint_y = None, height = 150)
        btn_img = Image(source = f"pbl_app\\image_dir\\flat{random.randint(0,9)}.jpeg", size_hint_x = None, width = 150)
        btn_layout.add_widget(btn_img)
        in_btn_layout = BoxLayout(orientation = "vertical")
        host_name = LBLabel(text = f"Flat {htext}")
        area_name = LBLabel(text = f"Area :{atext}")
        rate_name = LBLabel(text = f"Rate: {rtext * 500}")
        type_name = LBLabel(text = f"Type: {ttext}")
        sep_name = LBLabel(text = "_"*100)
        in_btn_layout.add_widget(host_name)
        in_btn_layout.add_widget(area_name)
        in_btn_layout.add_widget(rate_name)
        in_btn_layout.add_widget(type_name)
        in_btn_layout.add_widget(sep_name)
        btn_layout.add_widget(in_btn_layout)
        self.layout.add_widget(btn_layout)

        sic =  BoxLayout(size_hint_y = 0.2)
        self.save_btn = ToggleButton(text = "Save", on_press = self.save)
        inter_btn = Button(text = "Interested", on_press = self.inter)
        call_btn = Button(text = "Call", on_press = self.call)
        sic.add_widget(self.save_btn)
        sic.add_widget(inter_btn)
        sic.add_widget(call_btn)
        self.layout.add_widget(sic)

        fac_label = LBLabel(text = "Facilities", size_hint_y = 0.2)
        self.layout.add_widget(fac_label)
        fac_grid = GridLayout(cols = 4)
        for i in range(random.randint(1,8)):
            txt = random.choice(["wifi", "Washing machine", "Cupboard", "Private washroom", "Gyser", "Water purifier", "Gym", "Garden", "Library", "Mess", "Computer centre"])
            fac_btn = Button(text = f"{txt}", disabled = True)
            fac_grid.add_widget(fac_btn)
        self.layout.add_widget(fac_grid)
        
    def save(self, instance):
        if self.save_btn.state == "down":
            self.save_btn.text = "saved"
        elif self.save_btn.state == "normal":
            self.save_btn.text = "save"
    def inter(self, instance):
        self.manager.transition = CardTransition(direction = "down", mode = "push")
        self.manager.current = "saveflatinterestpage"
    def call(self, instance):
        self.manager.transition = CardTransition(direction = "down", mode = "push")
        self.manager.current = "callpage"

class SaveRoomPage(Screen):
    def __init__(self, **kwargs):
        super(SaveRoomPage, self).__init__(**kwargs)
        self.grid = BoxLayout(orientation = "vertical")
        self.grid.bind(minimum_height = self.grid.setter('height'))

        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

        self.add_widget(self.grid)

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "savedpage"
        self.grid.clear_widgets()
        top = BoxLayout(size_hint_y = 0.15)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Profile      ")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.grid.add_widget(top)

        top2 = BoxLayout(size_hint_y = 0.15)
        logo = Image(source = f"pbl_app\\image_dir\\user{random.randint(0,9)}.jpg", size_hint_x = None, width = 150)
        right_layout = BoxLayout(orientation='vertical')
        username_label = LBLabel(text=f'Username: {random.choice(["Ruhan", "Yash", "Prem", "Ayush", "Mayur", "Atul", "Raj", "Nikhil", "Hano", "Abhinav", "Sujay", "Shlok", "Charudatta", "Aditya", "Lokesh", "Yashraj", "Sahil"])}')
        area_layout = BoxLayout(size_hint_y = 0.25)
        area_label = LBLabel(text=f'Area: {random.choice(["Akurdi", "Pimpri", "Lonavala", "Shivaji Nagar","Talegaon", "Kanpur", "Pune", "Vashi", "Nerul", "Sanpada", "Juinagar", "Kalyan", "Ulwe", "Seawoods"])}', size_hint=(0.7, 1.0))
        area_layout.add_widget(area_label)
        right_layout.add_widget(username_label)
        right_layout.add_widget(area_layout)
        top2.add_widget(logo)
        top2.add_widget(right_layout)
        self.grid.add_widget(top2)
        
        sepa1 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa1.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa1)

        top3 = BoxLayout(orientation = "vertical", size_hint_y = 0.2)
        base = LBLabel(text = "Basic Details:", size_hint_y = 0.3)
        grid1 = GridLayout(cols = 2, y = 150)
        gender = LBLabel(text = f"gender: {random.choice(["Male", "Female", "Transgender", "Other", "Prefer not to say"])}", font_size = 30)
        age = LBLabel(text = f"age: {random.randint(18,22)}", font_size = 30)
        study = LBLabel(text = f"Years of study: {random.choice(["1st yr", "2nd yr", "3rd yr", "4th year", "Diploma"])}", font_size = 30)
        branch = LBLabel(text = f"Branch: {random.choice(["Computer", "Mechanical", "Civil", "Chemical", "AIDS", "ENTC", "BBA", "B-ARCH", "Semi-Conductors", "Instruments", "Deploma"])}", font_size = 30)
        grid1.add_widget(gender)
        grid1.add_widget(age)
        grid1.add_widget(study)
        grid1.add_widget(branch)
        top3.add_widget(base)
        top3.add_widget(grid1)
        self.grid.add_widget(top3)

        sepa2 = BoxLayout(size_hint_y = 0.05)
        line = Color(1,0,0,1)
        sepa2.canvas.add(Line(points = (0,0, self.grid.width, 1), color = line))
        self.grid.add_widget(sepa2)

        bot = BoxLayout(orientation = "vertical")
        bot_top = BoxLayout(size_hint_y = 0.2)
        pre_label = LBLabel(text = "Preference:")
        bot_top.add_widget(pre_label)
        bot.add_widget(bot_top)
        bot_grid = GridLayout(cols = 4)
        pre_list = ["Studious", "Gamer", "Invester", "Body Builder", "Partier", "Roamer", "Night owl", "Sleepy", "Content Creator", "Artist", "Reader", "Writer", "Coder", "No smoker", "No alcohol", "Quiet"]
        for i in range(random.randint(1,13)):
            pre_box = BoxLayout(orientation = "vertical")
            pre_pre_label = LBLabel(text = f"{random.choice(pre_list)}")
            pre_box.add_widget(pre_pre_label)
            bot_grid.add_widget(pre_box)
        bot.add_widget(bot_grid)
        self.grid.add_widget(bot)

class CallPage(Screen):
    def __init__(self, **kwargs):
        super(CallPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Call")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)
        
        self.label = LBLabel(text = "Calling Owner")
        self.layout.add_widget(self.label)
        self.add_widget(self.layout)

        self.calling(0)

    def back(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "mainpage"
    def calling(self, count):
        for i in range(5):
            if count == 1:
                self.label.text = "Calling Owner ."
            elif count == 2:
                self.label.text = "Calling Owner .."
            elif count == 3:
                self.label.text = "Calling Owner ..."
            elif count == 4:
                self.label.text = "Calling Owner ...."
            elif count == 5:
                self.label.text = "Calling Owner ....."
            elif count == 6:
                self.label.text = "Calling Owner ......" 
            elif count == 0:
                self.label.text = "Calling Owner"
            else:
                count = 0
            time.sleep(1)
            count += 1 

class ChatBotPage(Screen):
    def __init__(self, **kwargs):
        super(ChatBotPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = LBLabel(text = "Chat Bot")
        top.add_widget(back_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        self.scroll = ScrollView(do_scroll_y = True, bar_width = 30, bar_color = (1,1,1,1))
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        
        user = "Chat Bot:"
        answer = "Hi, Im your friendly chatbot. How can I help you?"
        btn_layout = BoxLayout(size_hint_y = None, height = 100)
        user_type = LBLabel(text = f"{user}", size_hint_x = 0.2)
        user_text = LBLabel(text = f"{answer}")
        btn_layout.add_widget(user_type)
        btn_layout.add_widget(user_text)
        self.grid.add_widget(btn_layout)

        self.scroll.add_widget(self.grid)
        mid.add_widget(self.scroll)
        self.layout.add_widget(mid)

        bottom = BoxLayout(size_hint_y = 0.2)
        self.textinput = TextInput(hint_text = "Enter something?")
        send_btn = Button(text = "Send", size_hint_x = 0.2, on_press = self.send)
        bottom.add_widget(self.textinput)
        bottom.add_widget(send_btn)
        self.layout.add_widget(bottom)

        self.add_widget(self.layout)
        
    def back(self, instance):
        self.manager.transition = CardTransition(direction = "right", mode = "pop")
        self.manager.current = "messagepage"

    def send(self,instance):
        btn_layout = BoxLayout(size_hint_y = None, height = 100)
        btn_img = LBLabel(text = f"You:", size_hint_x = 0.2)
        btn_layout.add_widget(btn_img)
        user_text = LBLabel(text = f"{self.textinput.text}")
        response = ask_chatbot(self.textinput.text)
        self.textinput.text = ""
        btn_layout.add_widget(user_text)
        self.grid.add_widget(btn_layout)
        
        #Function that asks chatbot for reply and display on screen
        btn_layout = BoxLayout(size_hint_y = None, height = 100)
        btn_img = LBLabel(text = f"Chat Bot:", size_hint_x = 0.2)
        btn_layout.add_widget(btn_img)
        self.bot_text = LBLabel(text = "Thinking of a suitable reply...")
        btn_layout.add_widget(self.bot_text)
        self.grid.add_widget(btn_layout)
        time.sleep(1)
        self.bot_text.text = f"{response}"
        


#Place to add new screens

class Blank(Screen):
    """
    This is a page/screen used for development of the project. 
    It is used as a placeholder for to be made pages.
    Will be replaced with ready made page once work is done.
    Dont delete this page as it will be usefull for future development.
    """
    def __init__(self,**kwargs):
        super(Blank,self).__init__(**kwargs)
        button = Button(text = "Nothing to see here for now", on_press = self.next)
        self.add_widget(button)
    def next(self,instance):
        self.manager.transition = FadeTransition()
        self.manager.current = "mainpage"

class ProjectApp(App):
    """
    This is the main part of the project which will be runned.
    """
    def build(self):
        screen_manager = ScreenManager()    #Manages all the screen

        #Listing all the screens that will be used to navigate by the app.
        screen_manager.add_widget(Start1Page(name='start1page'))
        screen_manager.add_widget(Start2Page(name='start2page'))
        screen_manager.add_widget(Start3Page(name='start3page'))
        screen_manager.add_widget(Start4Page(name='start4page'))
        screen_manager.add_widget(MainPage(name = "mainpage"))
        screen_manager.add_widget(Blank(name = "blank"))
        screen_manager.add_widget(ToolPage(name = "toolpage"))
        screen_manager.add_widget(TeamPage(name = "teampage"))
        screen_manager.add_widget(JoinTeamPage(name = "jointeampage"))
        screen_manager.add_widget(SettingsPage(name = "settingspage"))
        screen_manager.add_widget(MessagePage(name = "messagepage"))
        screen_manager.add_widget(MessPage(name = "messpage"))
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
        screen_manager.add_widget(HostelPage(name = "hostelpage"))
        screen_manager.add_widget(FlatPage(name = "flatpage"))
        screen_manager.add_widget(RoomPage(name = "roompage"))
        screen_manager.add_widget(HostelInterestPage(name = "hostelinterestpage"))
        screen_manager.add_widget(HostIntUserPage(name = "hostintuserpage"))
        screen_manager.add_widget(FlatInterestPage(name = "flatinterestpage"))
        screen_manager.add_widget(FlatIntUserPage(name = "flatintuserpage"))
        screen_manager.add_widget(TeamUserPage(name = "teamuserpage"))
        screen_manager.add_widget(SaveHostelInterestPage(name = "savehostelinterestpage"))
        screen_manager.add_widget(SaveHostIntUserPage(name = "savehostintuserpage"))
        screen_manager.add_widget(SaveFlatInterestPage(name = "saveflatinterestpage"))
        screen_manager.add_widget(SaveFlatIntUserPage(name = "saveflatintuserpage"))
        screen_manager.add_widget(SaveHostelPage(name = "savehostelpage"))
        screen_manager.add_widget(SaveFlatPage(name = "saveflatpage"))
        screen_manager.add_widget(SaveRoomPage(name = "saveroompage"))
        screen_manager.add_widget(CallPage(name = "callpage"))
        screen_manager.add_widget(ChatBotPage(name = "chatbotpage"))

        return screen_manager
    
if __name__ == "__main__":    #Checking if this file is being runned directly or as module.
    ProjectApp().run()    #Starts the app.


