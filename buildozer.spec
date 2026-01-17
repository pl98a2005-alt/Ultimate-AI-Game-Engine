[app]
# (str) عنوان التطبيق
title = Sovereign Architect

# (str) اسم الحزمة (Package name)
package.name = sovereign_architect

# (str) اسم النطاق (Package domain)
package.domain = com.sovereign.engine

# (str) مسار الكود المصدري
source.dir = .

# (list) الملفات المضمنة (مهم جداً للتعلم السري)
source.include_exts = py,png,jpg,kv,atlas,json,bin

# (str) نسخة التطبيق
version = 1.25

# (list) المتطلبات البرمجية (دعم الجرافيك والأداء)
requirements = python3,kivy,hostpython3,android,pyjnius,jnius

# (str) اتجاه الشاشة (يدعم التدوير لتجربة الألعاب)
orientation = all

# (bool) تفعيل وضع ملء الشاشة
fullscreen = 1

# (list) أذونات السيادة (الوصول للملفات لتوليد OBB و Data)
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET, BLUETOOTH, BLUETOOTH_ADMIN

# (int) مستوى الأندرويد المستهدف (أحدث نسخة لعام 2026)
android.api = 34
android.minapi = 21

# (list) معماريات المعالج (دعم 64 بت للأداء العالي)
android.archs = arm64-v8a, armeabi-v7a

# (bool) تفعيل نظام الـ OBB تلقائياً للملفات الضخمة
android.copy_libs = 1
android.enable_vulkan = True

# (str) أيقونة التطبيق (سيقوم المهندس بتوليدها لاحقاً)
# icon.filename = %(source.dir)s/data/icon.png

# (list) دعم أجهزة التحكم (Gamepads) عبر USB وبلوتوث
android.features = android.hardware.usb.host, android.hardware.bluetooth

# (str) وضع الـ Log (مهم لمراقبة الـ XP والتعلم)
android.logcat_filters = *:S python:D

[buildozer]
# (int) مستوى التقرير (Level 2 يظهر تفاصيل البناء)
log_level = 2

# (str) المسار المؤقت للبناء
bin_dir = ./bin
