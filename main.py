import os, json, time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# إعدادات المظهر الملكي
Window.clearcolor = (0.02, 0.02, 0.02, 1)

class MainInterface(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # الشعار: O بوسطها شخطة (Phi Symbol)
        self.logo = Label(text='Φ', font_size='80sp', color=(1, 0.8, 0, 1), size_hint_y=0.2)
        
        # منطقة المحادثة مع المهندس
        self.display = TextInput(text='[المهندس]: مرحباً بك في عرش الصناعة. صف لي حلمك وسأكمله لك...', 
                                readonly=True, background_color=(0.05, 0.05, 0.05, 1), 
                                foreground_color=(1, 1, 1, 1), font_size='16sp')
        
        self.input = TextInput(hint_text='ادمج ببجي وكود مع عالم مفتوح...', multiline=True, size_hint_y=0.3)
        
        # أزرار التحكم
        btn_layout = BoxLayout(size_hint_y=0.15, spacing=10)
        self.build_btn = Button(text='بدء التحليل والصنع', background_color=(0, 0.5, 0.2, 1))
        self.projects_btn = Button(text='المشاريع السابقة', background_color=(0.2, 0.2, 0.2, 1))
        
        btn_layout.add_widget(self.build_btn)
        btn_layout.add_widget(self.projects_btn)
        
        layout.add_widget(self.logo)
        layout.add_widget(self.display)
        layout.add_widget(self.input)
        layout.add_widget(btn_layout)
        self.add_widget(layout)

class SovereignApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainInterface(name='main'))
        return sm

if __name__ == '__main__':
    SovereignApp().run()
