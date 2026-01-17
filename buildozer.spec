[app]
# (str) عنوان التطبيق
title = Sovereign Architect

# (str) اسم الحزمة
package.name = sovereign_architect

# (str) اسم النطاق
package.domain = com.sovereign.engine

# (str) مسار الكود المصدري
source.dir = .

# (list) الملفات المضمنة (مهم للذاكرة السرية)
source.include_exts = py,png,jpg,kv,atlas,json,bin

# (str) نسخة التطبيق
version = 1.25

# (list) المتطلبات البرمجية
requirements = python3,kivy,hostpython3,android,pyjnius,jnius

# (str) اتجاه الشاشة (تم التعديل لـ sensor ليعمل في كل الاتجاهات)
orientation = sensor

# (bool) تفعيل وضع ملء الشاشة
fullscreen = 1

# (list) أذونات السيادة
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET, BLUETOOTH, BLUETOOTH_ADMIN

# (int) مستوى الأندرويد المستهدف
android.api = 33
android.minapi = 21

# (list) معماريات المعالج (دعم القوة الكاملة)
android.archs = arm64-v8a, armeabi-v7a

# (bool) تفعيل نظام الـ OBB تلقائياً
android.copy_libs = 1
android.enable_vulkan = True
android.accept_sdk_license = True
android.skip_update = True

# (list) دعم أجهزة التحكم
android.features = android.hardware.usb.host, android.hardware.bluetooth

# (str) وضع الـ Log
android.logcat_filters = *:S python:D

[buildozer]
# (int) مستوى التقرير
log_level = 2

# (str) المسار المؤقت للبناء
bin_dir = ./bin
