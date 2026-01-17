import os
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase

# تسجيل الخط العربي (سيقوم المحرك بتحميله آلياً إلى المجلد)
try:
    LabelBase.register(name='Arabic', fn_regular='Cairo-Bold.ttf')
except:
    pass

Window.clearcolor = (0.01, 0.01, 0.05, 1)

class ArchitectScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(name='architect', **kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=25)
        
        # هيدر بنظام الخبرة والسيادة
        self.header = Label(
            text="RANK: SOVEREIGN | LVL: 1 | XP: 0\n[ نـظـام الـسـيـادة الـمـطـلـقـة ]",
            size_hint_y=0.2, color=(0, 1, 0.8, 1), bold=True, 
            font_size='22sp', font_name='Arabic', halign='center'
        )
        
        self.console = Label(
            text="المهندس السيادي: الأنظمة جاهزة لبناء عالمك.",
            size_hint_y=0.4, font_name='Arabic', font_size='18sp', halign='center'
        )
        
        self.prompt = TextInput(
            hint_text="اكتب مواصفات عالمك هنا...", size_hint_y=0.15,
            font_name='Arabic', halign='right', background_color=(0.1, 0.1, 0.2, 1),
            foreground_color=(1, 1, 1, 1), cursor_color=(0, 1, 0.8, 1)
        )
        
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=20)
        self.btn_build = Button(
            text="إطلاق البناء (Build)", background_color=(0, 0.6, 0.4, 1),
            font_name='Arabic', font_size='18sp', bold=True
        )
        
        btn_layout.add_widget(self.btn_build)
        
        self.layout.add_widget(self.header)
        self.layout.add_widget(self.console)
        self.layout.add_widget(self.prompt)
        self.layout.add_widget(btn_layout)
        self.add_widget(self.layout)

class SovereignApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ArchitectScreen())
        return sm

if __name__ == "__main__":
    SovereignApp().run()
