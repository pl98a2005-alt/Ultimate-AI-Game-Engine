[app]
title = Sovereign Engine
package.name = sovereign.phi
package.domain = org.king
source.dir = .
version = 1.0.0

# الملفات المطلوبة
source.include_exts = py,png,jpg,kv,atlas,json

# المكتبات البرمجية
requirements = python3,kivy,requests,urllib3,certifi

# إعدادات الشاشة والجرافيك
orientation = portrait
fullscreen = 1

# صلاحيات الوصول الكاملة (السيادة)
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# الربط مع أدوات GitHub الحديثة (2026)
android.api = 34
android.minapi = 21
android.ndk = 27b
android.archs = arm64-v8a

# مسارات الأدوات الجاهزة في السيرفر
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# قبول الرخص تلقائياً
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
