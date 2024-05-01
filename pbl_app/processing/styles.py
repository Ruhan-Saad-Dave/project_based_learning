"""
This file is used to design different styles for the widgets.
"""

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, Line, Rectangle
from kivy.utils import get_color_from_hex


class RLabel(Label):
    '''
    This class creates a red colour background for the labels, as is the original labels the background is transpart.

    Inheriting from the original Label class and making changes to it.
    '''
    def __init__(self, **kwargs):
        '''Initiallization of the widget'''
        super(RLabel, self).__init__(**kwargs)
        self.color = (0,0,0,1)
        # Bind the size and position properties to trigger the update_rect method
        self.bind(size=self.update_rect, pos=self.update_rect)    
        # Update the rectangle initially
        self.update_rect()    

    def update_rect(self, *args):
        # Clear any existing graphics instructions
        self.canvas.before.clear()
        with self.canvas.before:
            # Set the color to red
            Color(1,1,225/255,1)  # RGBA values, where (1, 0, 0, 1) represents red color
            # Draw a rectangle behind the label
            Rectangle(pos=self.pos, size=self.size)

class LBLabel(Label):
    '''
    This class creates a black colour background for the labels, as is the original labels the background is transpart.

    Inheriting from the original Label class and making changes to it.
    '''
    def __init__(self, **kwargs):
        #Initiallization of the widget
        super(LBLabel, self).__init__(**kwargs)
        # Bind the size and position properties to trigger the update_rect method
        self.bind(size=self.update_rect, pos=self.update_rect)
        # Update the rectangle initially
        self.update_rect()

    def update_rect(self, *args):
        # Clear any existing graphics instructions
        self.canvas.before.clear()
        with self.canvas.before:
            # Set the color to red
            Color(0.5, 0.5, 1, 1)  # RGBA values, where (0.5, 0.5, 1, 1) represents light blue color
            # Draw a rectangle behind the label
            Rectangle(pos=self.pos, size=self.size, width=1)

class LGLabel(Label):
    '''
    This class creates a black colour background for the labels, as is the original labels the background is transpart.

    Inheriting from the original Label class and making changes to it.
    '''
    def __init__(self, **kwargs):
        #Initiallization of the widget
        super(LGLabel, self).__init__(**kwargs)
        # Bind the size and position properties to trigger the update_rect method
        self.bind(size=self.update_rect, pos=self.update_rect)
        # Update the rectangle initially
        self.update_rect()

    def update_rect(self, *args):
        # Clear any existing graphics instructions
        self.canvas.before.clear()
        with self.canvas.before:
            # Set the color to red
            Color(0.87, 0, 0.16, 1)  # RGBA values, where (0.5, 0.5, 1, 1) represents light blue color
            # Draw a rectangle behind the label
            Rectangle(pos=self.pos, size=self.size, width=1)

class LogoLabel(Label):
    def __init__(self, **kwargs):
        super(LogoLabel, self).__init__(**kwargs)

        self.background_colour = get_color_from_hex('#FFFFFF')
        self.color = get_color_from_hex('#00008B')

class FeatureButton(Button):
    def __init__(self, **kwargs):
        super(FeatureButton, self).__init__(**kwargs)
        
        self.background_color = get_color_from_hex('#FFFFE1')
        self.color = get_color_from_hex('#E6F7FF')

class MyTextInput(TextInput):
    def on_focus(self, instance, value):
        if value:
            self.y = Window.height / 2
        else:
            self.y = 0

class ChatTextInput(TextInput):
    def __init__(self, **kwargs):
        super(ChatTextInput, self).__init__(**kwargs)

        self.background_color = (1,1,225/255,1)
        self.readonly = True
        self.foreground_color = (0,0,0,1)
        self.allow_copy = False

class ChatMyTextInput(TextInput):
    def __init__(self, **kwargs):
        super(ChatMyTextInput, self).__init__(**kwargs)

        self.background_color = (0.5, 0.5, 1, 1)
        self.readonly = True