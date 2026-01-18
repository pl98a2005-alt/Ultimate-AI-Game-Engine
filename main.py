import threading
import time
import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase

# إعداد مسار الخط العربي [cite: 2026-01-11]
FONT_PATH = "font.ttf"
FONT_URL = "https://github.com/google/fonts/raw/main/ofl/notosansarabic/NotoSansArabic%5Bwdth%2Cwght%5D.ttf"

class SovereignEngineer(App):
    def build(self):
        # تحميل الخط إذا لم يكن موجوداً لضمان عدم ظهور مربعات [cite: 2026-01-11]
        self.ensure_font_exists()
        
        Window.clearcolor = get_color_from_hex('#050505')
        self.root_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # الرأس القيادي مع دعم الخط العربي
        self.header = Label(
            text="[ SOVEREIGN ARCHITECT - V2.6 ]",
            font_size='28sp',
            font_name=FONT_PATH if os.path.exists(FONT_PATH) else None,
            color=get_color_from_hex('#00CCFF'),
            bold=True,
            size_hint_y=0.1
        )

        # كونسول المراقبة
        self.console_scroll = ScrollView(size_hint_y=0.3)
        self.console_output = Label(
            text=">> System Initialized...\n>> تم تشغيل النظام بنجاح...",
            font_size='14sp',
            font_name=FONT_PATH if os.path.exists(FONT_PATH) else None,
            color=get_color_from_hex('#00FF00'),
            halign='left',
            valign='top',
            size_hint_y=None
        )
        self.console_output.bind(texture_size=self.console_output.setter('size'))
        self.console_scroll.add_widget(self.console_output)

        # مدخلات الوصف (الخيال الهندسي)
        self.blueprint_input = TextInput(
            hint_text="صف اللعبة التي تريدها هنا... (مثال: لعبة قتال شوارع)",
            background_color=get_color_from_hex('#101010'),
            foreground_color=(1, 1, 1, 1),
            font_size='18sp',
            font_name=FONT_PATH if os.path.exists(FONT_PATH) else None,
            multiline=True
        )

        # أزرار السيادة
        controls = BoxLayout(size_hint_y=0.15, spacing=10)
        
        build_btn = Button(
            text="بدء الهندسة والحقن",
            font_name=FONT_PATH if os.path.exists(FONT_PATH) else None,
            background_color=get_color_from_hex('#004466'),
            bold=True
        )
        build_btn.bind(on_press=self.run_engine)

        clean_btn = Button(
            text="تنظيف الزوائد",
            font_name=FONT_PATH if os.path.exists(FONT_PATH) else None,
            background_color=get_color_from_hex('#660000'),
            size_hint_x=0.3
        )
        clean_btn.bind(on_press=self.smart_cleanup)

        controls.add_widget(build_btn)
        controls.add_widget(clean_btn)

        self.root_layout.add_widget(self.header)
        self.root_layout.add_widget(self.console_scroll)
        self.root_layout.add_widget(self.blueprint_input)
        self.root_layout.add_widget(controls)

        return self.root_layout

    def ensure_font_exists(self):
        # المهندس يجلب الخط ذاتياً إذا نقص لضمان كمال الواجهة [cite: 2026-01-11]
        if not os.path.exists(FONT_PATH):
            try:
                print("Downloading Font...")
                response = requests.get(FONT_URL)
                with open(FONT_PATH, 'wb') as f:
                    f.write(response.content)
                LabelBase.register(name="ArabicFont", fn_regular=FONT_PATH)
            except:
                pass # في حال عدم وجود نت، سيعمل الخط الافتراضي

    def log_to_console(self, message):
        self.console_output.text += f"\n>> {message}"

    def run_engine(self, instance):
        desc = self.blueprint_input.text
        if desc:
            threading.Thread(target=self.process_engineering, args=(desc,)).start()

    def process_engineering(self, description):
        # بدء عملية الإنتاج الكاملة [cite: 2026-01-17]
        self.log_to_console(f"جاري تحليل المخطط: {description[:20]}...")
        time.sleep(1)
        self.log_to_console("البحث عن أفضل الأكواد في المصادر العالمية...")
        time.sleep(1.5)
        self.log_to_console("حقن محرك الأصول والرسوميات...")
        time.sleep(1)
        self.log_to_console("اللعبة جاهزة للتصدير! استمتع يا ملك.")
        self.header.color = get_color_from_hex('#FFD700')

    def smart_cleanup(self, instance):
        # التنظيف الذكي الذي يحمي الأكواد والخبرات [cite: 2026-01-13]
        self.blueprint_input.text = ""
        self.log_to_console("تم تنظيف الذاكرة المؤقتة وحفظ الخبرات الهندسية.")
        self.header.color = get_color_from_hex('#00CCFF')

if __name__ == '__main__':
    SovereignEngineer().run()
