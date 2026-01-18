import threading
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SovereignEngineer(App):
    def build(self):
        # إعداد بيئة المصنع
        Window.clearcolor = get_color_from_hex('#050505')
        self.root_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # الرأس القيادي
        self.header = Label(
            text="[ SOVEREIGN ARCHITECT - V2.5 ]",
            font_size='28sp',
            color=get_color_from_hex('#00CCFF'),
            bold=True,
            size_hint_y=0.1
        )

        # شاشة الكونسول (لمراقبة عمل المهندس لحظة بلحظة)
        self.console_scroll = ScrollView(size_hint_y=0.3)
        self.console_output = Label(
            text=">> System Initialized...\n>> Awaiting Blueprint Description...",
            font_size='12sp',
            color=get_color_from_hex('#00FF00'),
            halign='left',
            valign='top',
            size_hint_y=None
        )
        self.console_output.bind(texture_size=self.console_output.setter('size'))
        self.console_scroll.add_widget(self.console_output)

        # مدخلات الوصف (الخيال الهندسي)
        self.blueprint_input = TextInput(
            hint_text="صف اللعبة أو البرنامج المطلوب هندسته هنا...",
            background_color=get_color_from_hex('#101010'),
            foreground_color=(1, 1, 1, 1),
            font_size='18sp',
            multiline=True
        )

        # أزرار التحكم والسيادة
        controls = BoxLayout(size_hint_y=0.15, spacing=10)
        
        build_btn = Button(
            text="بدء الهندسة والحقن",
            background_color=get_color_from_hex('#004466'),
            bold=True
        )
        build_btn.bind(on_press=self.run_engine)

        clean_btn = Button(
            text="تنظيف الزوائد",
            background_color=get_color_from_hex('#660000'),
            size_hint_x=0.3
        )
        clean_btn.bind(on_press=self.smart_cleanup)

        controls.add_widget(build_btn)
        controls.add_widget(clean_btn)

        # تجميع المصنع
        self.root_layout.add_widget(self.header)
        self.root_layout.add_widget(self.console_scroll)
        self.root_layout.add_widget(self.blueprint_input)
        self.root_layout.add_widget(controls)

        return self.root_layout

    def log_to_console(self, message):
        self.console_output.text += f"\n>> {message}"

    def run_engine(self, instance):
        desc = self.blueprint_input.text
        if desc:
            threading.Thread(target=self.process_engineering, args=(desc,)).start()

    def process_engineering(self, description):
        # محاكاة لعمليات البحث والحقن العالمية [2026-01-11]
        self.log_to_console(f"Analyzing Blueprint: {description[:20]}...")
        time.sleep(1)
        self.log_to_console("Searching Global Repositories for Logic...")
        time.sleep(1.5)
        self.log_to_console("Injecting Asset Engine (Images/Sounds)...")
        time.sleep(1)
        self.log_to_console("Compiling Autonomous Game Engine...")
        time.sleep(2)
        self.log_to_console("SUCCESS: Game Blueprint Ready for Export.")
        self.header.color = get_color_from_hex('#FFD700')

    def smart_cleanup(self, instance):
        # تنظيف الزوائد مع استثناء الأكواد والخبرات [2026-01-13]
        self.blueprint_input.text = ""
        self.log_to_console("Cleaning Cache... Keeping Core Experiences Intact.")
        self.header.color = get_color_from_hex('#00CCFF')

if __name__ == '__main__':
    SovereignEngineer().run()
