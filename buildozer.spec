[app]
# (str) عنوان التطبيق
title = Sovereign Engine

# (str) اسم الحزمة (مهم جداً للسيادة)
package.name = sovereign.phi

# (str) الدومين
package.domain = org.king

# (str) مكان ملف main.py (النقطة التي كانت ناقصة)
source.dir = .

# (str) رقم الإصدار (النقطة الثانية التي كانت ناقصة)
version = 1.0.0

# (list) الملفات التي سيتم تضمينها
source.include_exts = py,png,jpg,kv,atlas,json

# (list) المتطلبات البرمجية
requirements = python3,kivy,requests,urllib3,certifi

# (str) إعدادات الشاشة
orientation = portrait
fullscreen = 1

# (list) الصلاحيات (للكاميرا والملفات والإنترنت)
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) المستهدف من الأندرويد (حديث جداً 2026)
android.api = 33
android.minapi = 21
android.arch = arm64-v8a

# (bool) قبول الرخص تلقائياً
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
