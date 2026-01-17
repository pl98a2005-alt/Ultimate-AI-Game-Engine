import os
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.text import LabelBase

# تسجيل الخط العربي (تأكد من وجود الملف أو سيتم تحميله عبر الـ Workflow)
try:
    LabelBase.register(name='Arabic', fn_regular='Cairo-Bold.ttf')
except Exception as e:
    print(f"Font loading error: {e}")

Window.clearcolor = (0.01, 0.01, 0.02, 1)

class SovereignMind:
    def __init__(self):
        self.memory_path = ".sovereign_logic.bin"
        self.data = self.load_experience()

    def load_experience(self):
        if os.path.exists(self.memory_path):
            try:
                with open(self.memory_path, 'r') as f:
                    return json.load(f)
            except: pass
        return {"xp": 0, "level": 1}

    def evolve(self, action_type):
        self.data["xp"] += 50
        self.data["level"] = (self.data["xp"] // 1000) + 1
        with open(self.memory_path, 'w') as f:
            json.dump(self.data, f)
        return 50

class ArchitectScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(name='architect', **kwargs)
        self.mind = SovereignMind()
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        stats = self.mind.data
        self.header = Label(
            text=f"RANK: SOVEREIGN | LVL: {stats['level']} | XP: {stats['xp']}\n[ SYSTEM: AR/EN | 120 FPS ]",
            size_hint_y=0.2, color=(0, 1, 0.7, 1), bold=True, font_size='20sp', font_name='Arabic'
        )
        
        self.console = Label(
            text="المهندس: الأنظمة جاهزة. بانتظار أوامر البناء السيادية.",
            size_hint_y=0.4, halign='center', font_name='Arabic', font_size='18sp'
        )
        
        self.prompt = TextInput(
            hint_text="صف مشروعك هنا...", size_hint_y=0.15, 
            font_name='Arabic', halign='right', background_color=(0.05, 0.05, 0.1, 1),
            foreground_color=(1, 1, 1, 1)
        )
        
        btn_box = BoxLayout(size_hint_y=0.2, spacing=15)
        self.btn_build = Button(text="بناء (Build)", background_color=(0, 0.5, 0.3, 1), font_name='Arabic')
        self.btn_build.bind(on_press=self.initiate_build)
        
        self.btn_clean = Button(text="تطهير (Clean)", background_color=(0.6, 0, 0, 1), font_name='Arabic')
        
        btn_box.add_widget(self.btn_build)
        btn_box.add_widget(self.btn_clean)
        
        self.layout.add_widget(self.header)
        self.layout.add_widget(self.console)
        self.layout.add_widget(self.prompt)
        self.layout.add_widget(btn_box)
        self.add_widget(self.layout)

    def initiate_build(self, instance):
        xp = self.mind.evolve("build")
        self.console.text = f"تم البناء بنجاح! اكتسبت {xp} XP."
        self.header.text = f"RANK: SOVEREIGN | LVL: {self.mind.data['level']} | XP: {self.mind.data['xp']}"

class SovereignApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ArchitectScreen())
        return sm

if __name__ == "__main__":
    SovereignApp().run()
        desc = self.prompt.text
        if not desc:
            self.console.text = "المهندس: لا يمكنني بناء العدم. صف رؤيتك يا ملك."
            return

        # محاكاة منطق البناء المتقدم
        self.console.text = "المهندس: جاري حقن مكتبات Vulkan لضمان 120 فريم...\nتجهيز ملفات OBB للأصول الضخمة...\nحفظ الخبرة في العقل السري..."
        
        # زيادة الخبرة
        complexity = "high" if len(desc) > 30 else "normal"
        xp_gain = self.mind.evolve("build", complexity)
        
        # تحديث الواجهة
        Clock.schedule_once(lambda dt: self.update_ui(xp_gain), 2)

    def update_ui(self, gain):
        stats = self.mind.data
        self.header.text = f"RANK: SOVEREIGN | LVL: {stats['level']} | XP: {stats['xp']}\n[ SYSTEM: AR/EN | 120 FPS UNLOCKED ]"
        self.console.text = f"المهندس: تم البناء بنجاح! اكتسبت {gain} XP.\nالحزمة جاهزة: APK + Data + OBB."
        self.prompt.text = ""

    def perform_clean(self, instance):
        self.console.text = "المهندس: بروتوكول التطهير يعمل...\nتم حذف المخلفات. الألعاب والخبرات والملفات الأساسية في أمان مطلق."

class SimulatorScreen(Screen):
    """محاكي الأداء العالي لتجربة الألعاب"""
    def __init__(self, **kwargs):
        super().__init__(name='simulator', **kwargs)
        # هنا يتم وضع محرك الجرافيك الفائق مستقبلاً
        pass

class SovereignApp(App):
    def build(self):
        self.title = "Sovereign Architect Factory"
        sm = ScreenManager()
        sm.add_widget(ArchitectScreen())
        sm.add_widget(SimulatorScreen())
        return sm

if __name__ == "__main__":
    SovereignApp().run()
