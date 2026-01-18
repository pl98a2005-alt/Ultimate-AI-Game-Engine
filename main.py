from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

class SovereignApp(App):
    def build(self):
        layout = BoxLayout(padding=50)
        lbl = Label(
            text="[ SYSTEM ONLINE ]\nREADY TO ENGINEER",
            font_size='32sp',
            color=get_color_from_hex('#00FF00'),
            halign='center'
        )
        layout.add_widget(lbl)
        return layout

if __name__ == '__main__':
    SovereignApp().run()
