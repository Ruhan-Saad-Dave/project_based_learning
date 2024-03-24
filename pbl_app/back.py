from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class MyLabelApp(App):
    def build(self):
        # Create a BoxLayout to contain the label with background color
        label_container = BoxLayout(orientation='vertical')

        # Set the background color of the label container
        with label_container.canvas.before:
            Color(1, 0, 0, 1)  # Background color (red)
            self.rect = Rectangle(pos=label_container.pos, size=label_container.size)

        # Bind the size of the label container to update the background color
        label_container.bind(size=self.update_rect)

        # Create a Label widget
        label = Label(
            text='Hello, Kivy!',
            size_hint=(None, None),
            size=(400, 100),
            color=(1, 1, 1, 1)  # Text color (white)
        )

        # Add the label to the label container
        label_container.add_widget(label)

        return label_container

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MyLabelApp().run()
