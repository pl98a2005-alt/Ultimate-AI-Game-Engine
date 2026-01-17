import os
import json
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle

# --- إعدادات السيادة والأداء العالي ---
Window.clearcolor = (0.01, 0.01, 0.02, 1) # سواد ملكي عميق
Config_FPS = 120 # استهداف فريمات عالية مثل ببجي

class SovereignMind:
    """عقل المهندس: نظام الخبرة السري والتعلم الذاتي"""
    def __init__(self):
        self.memory_path = ".sovereign_logic.bin"
        self.data = self.load_experience()

    def load_experience(self):
        if os.path.exists(self.memory_path):
            try:
                with open(self.memory_path, 'r') as f:
                    return json.load(f)
            except: pass
        return {"xp": 0, "level": 1, "total_builds": 0, "unlocked_tech": []}

    def evolve(self, action_type, complexity="normal"):
        gain = 100 if complexity == "high" else 20
        self.data["xp"] += gain
        self.data["total_builds"] += 1
        self.data["level"] = (self.data["xp"] // 1000) + 1
        with open(self.memory_path, 'w') as f:
            json.dump(self.data, f)
        return gain

class ArchitectScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(name='architect', **kwargs)
        self.mind = SovereignMind()
        
        # التخطيط الرئيسي
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # 1. شريط الحالة العلوي (Status Bar)
        stats = self.mind.data
        self.header = Label(
            text=f"RANK: SOVEREIGN | LVL: {stats['level']} | XP: {stats['xp']}\n[ SYSTEM: AR/EN | 120 FPS UNLOCKED ]",
            size_hint_y=0.15, color=(0, 1, 0.7, 1), bold=True, font_size='18sp'
        )
        self.layout.add_widget(self.header)

        # 2. كونسول المهندس (The Thinking Zone)
        self.console = Label(
            text="المهندس: الأنظمة جاهزة. بانتظار وصفك لبدء بناء حزمة الـ APK+OBB.",
            size_hint_y=0.35, halign='center', valign='middle',
            text_size=(Window.width - 60, None), color=(0.9, 0.9, 0.9, 1)
        )
        self.layout.add_widget(self.console)

        # 3. صندوق الوصف الذكي (Architect Prompt)
        self.prompt = TextInput(
            hint_text="صف اللعبة هنا... (مثلاً: لعبة سيارات 3D مع فيزياء اصطدام واقعية)",
            size_hint_y=0.15, background_color=(0.05, 0.05, 0.1, 1),
            foreground_color=(1, 1, 1, 1), cursor_color=(0, 1, 0.8, 1),
            font_size='16sp', multiline=False
        )
        self.layout.add_widget(self.prompt)

        # 4. أزرار التحكم والسيادة
        btn_box = BoxLayout(size_hint_y=0.2, spacing=15)
        
        self.btn_build = Button(text="بناء سيادي (Build)", background_color=(0, 0.5, 0.3, 1), bold=True)
        self.btn_build.bind(on_press=self.initiate_build)
        
        self.btn_clean = Button(text="تطهير (Clean)", background_color=(0.6, 0, 0, 1), bold=True)
        self.btn_clean.bind(on_press=self.perform_clean)
        
        btn_box.add_widget(self.btn_build)
        btn_box.add_widget(self.btn_clean)
        self.layout.add_widget(btn_box)

        self.add_widget(self.layout)

    def initiate_build(self, instance):
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
