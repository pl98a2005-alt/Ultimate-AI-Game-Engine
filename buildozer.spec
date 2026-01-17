[app]
title = Sovereign Engine
package.name = sovereign.phi
package.domain = org.king
source.dir = .
version = 1.0.0

# الملفات المضمنة
source.include_exts = py,png,jpg,kv,atlas,json

# المتطلبات البرمجية
requirements = python3,kivy,requests,urllib3,certifi

# إعدادات الشاشة
orientation = portrait
fullscreen = 1

# الصلاحيات السيادية
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# دعم المعالجات (التصحيح الجديد)
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# إعدادات الاندرويد
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
