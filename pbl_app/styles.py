"""
This file is used to design different styles for the widgets.
"""

from kivy.uix.label import Label
from kivy.graphics import Color, Line, Rectangle

class RLabel(Label):
    '''
    This class creates a red colour background for the labels, as is the original labels the background is transpart.

    Inheriting from the original Label class and making changes to it.
    '''
    def __init__(self, **kwargs):
        '''Initiallization of the widget'''
        super(RLabel, self).__init__(**kwargs)
        # Bind the size and position properties to trigger the update_rect method
        self.bind(size=self.update_rect, pos=self.update_rect)    
        # Update the rectangle initially
        self.update_rect()    

    def update_rect(self, *args):
        # Clear any existing graphics instructions
        self.canvas.before.clear()
        with self.canvas.before:
            # Set the color to red
            Color(1, 0, 0, 1)  # RGBA values, where (1, 0, 0, 1) represents red color
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

