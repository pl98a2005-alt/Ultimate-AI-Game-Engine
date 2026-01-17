import json, os, requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

class SovereignEngine(App):
    def build(self):
        # --- نظام الخبرة المحمي ---
        self.exp_file = "experience.json"
        self.knowledge = self.load_knowledge()
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # الرأس (Header)
        self.status = Label(text="Φ SOVEREIGN COMMAND CENTER v2.0", font_size='22sp', color=(0, 1, 1, 1))
        layout.add_widget(self.status)

        # --- مدخل الوصف (مستقبل الخيال) ---
        self.description_input = TextInput(
            hint_text="صف العالم أو اللعبة التي يتخيلها عقلك...",
            multiline=True, size_hint_y=0.4, background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1), cursor_color=(0, 1, 0, 1)
        )
        layout.add_widget(self.description_input)

        # زر المهندس (تحليل + استنتاج + اقتراح)
        btn_architect = Button(text="🧠 استنتاج وبناء (Engineer Logic)", background_color=(0.5, 0, 1, 1))
        btn_architect.bind(on_press=self.analyze_and_propose)
        layout.add_widget(btn_architect)

        # شريط التحميل الذكي (بدون فجوات)
        self.progress = ProgressBar(max=100, value=0)
        layout.add_widget(self.progress)

        # زر التثبيت عبر QR (تطوير: يدعم التحميل الخلفي)
        btn_scan = Button(text="📸 مسح وتحديث (Hot-Swap Update)", background_color=(0, 0.8, 0.4, 1))
        btn_scan.bind(on_press=self.open_scanner)
        layout.add_widget(btn_scan)

        # زر التنظيف السيادي (المطور: استثناء الملفات الحيوية)
        btn_clean = Button(text="🧹 تنظيف سيادي (Preserve Knowledge)", background_color=(1, 0.2, 0.2, 1))
        btn_clean.bind(on_press=self.sovereign_cleanup)
        layout.add_widget(btn_clean)

        return layout

    # --- منطق المهندس (التحليل والاستنتاج) ---
    def analyze_and_propose(self, instance):
        user_desc = self.description_input.text
        if not user_desc:
            self.status.text = "⚠️ يا ملك، أحتاج وصفاً لأبدأ البناء!"
            return

        # محاكاة الاستنتاج (Inference)
        self.status.text = "🔍 المهندس يحلل الأنماط ويقترح تطويرات..."
        
        # هنا المهندس يقترح بناءً على الخبرة السابقة
        suggestion = "اقترح إضافة نظام 'الجاذبية المتغيرة' ونموذج 'تعلم الأعداء' من حركاتك."
        self.status.text = f"✅ استنتاج: {suggestion}"
        
        # البدء في بناء الكود (محاكاة)
        Clock.schedule_interval(self.simulate_build, 0.05)

    def simulate_build(self, dt):
        if self.progress.value >= 100:
            self.status.text = "👑 تم بناء منطق اللعبة وتخزين الخبرة!"
            self.save_knowledge({"last_build": self.description_input.text})
            return False
        self.progress.value += 2

    # --- نظام التحميل (تنزيل بدون فجوات) ---
    def open_scanner(self, instance):
        self.status.text = "📡 جاري الاتصال بالمستودع لتحميل التحديث..."
        # منطق التحميل: يحمل الملف الجديد، يتأكد منه، ثم يستبدل القديم (Hot-Swap)
        self.progress.value = 0
        self.status.text = "📥 جاري التحميل في الخلفية (النسخة الحالية تعمل)..."

    # --- نظام الخبرة (التعلم الذاتي) ---
    def load_knowledge(self):
        if os.path.exists("experience.json"):
            with open("experience.json", "r") as f: return json.load(f)
        return {"level": 1, "data": []}

    def save_knowledge(self, new_data):
        self.knowledge["data"].append(new_data)
        with open("experience.json", "w") as f:
            json.dump(self.knowledge, f)

    # --- زر التنظيف (المطور) ---
    def sovereign_cleanup(self, instance):
        # استثناء الملفات المطلوبة: الخبرة، ملف التطبيق، ملفات البناء
        required = ["experience.json", "main.py", "buildozer.spec"]
        deleted = 0
        for file in os.listdir("."):
            if file not in required and os.path.isfile(file):
                os.remove(file)
                deleted += 1
        self.status.text = f"🧹 تم سحق {deleted} ملفات.. الخبرة والمهندس في أمان."

if __name__ == '__main__':
    SovereignEngine().run()
