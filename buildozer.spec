[app]
title = Sovereign Engine
package.name = sovereign.phi
package.domain = org.king

# جودة الجرافيك والفيزياء (دعم OpenGL 3 لتنافس ببجي)
android.arch = arm64-v8a
android.api = 33
android.minapi = 21

# المتطلبات البرمجية (المحركات التي طلبناها)
requirements = python3,kivy,requests,urllib3

# الصلاحيات (مهمة جداً للـ QR والـ OBB)
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# إعدادات الشاشة (مثل الألعاب العالمية)
orientation = portrait
fullscreen = 1

# أيقونة التطبيق (سنغيرها لاحقاً بشعار السيادة)
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
