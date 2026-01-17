[app]
title = Sovereign Engine
package.name = sovereign.phi
package.domain = org.king
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 1.0.0

# المكتبات: أضفت مكتبات المعالجة لضمان عمل "المهندس" و"نظام التحميل"
requirements = python3,kivy,requests,urllib3,certifi,charset-normalizer,idna

orientation = portrait
fullscreen = 1

# الصلاحيات: إضافة صلاحية التثبيت (REQUEST_INSTALL_PACKAGES) ليعمل نظام التحديث التلقائي بلا فجوات
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, REQUEST_INSTALL_PACKAGES

# إعدادات الأدوات (مضبوطة لتتوافق مع سيرفر 2026)
android.api = 33
android.minapi = 21
# نستخدم 25b لأنه الأكثر استقراراً لمحركات الذكاء الاصطناعي
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# هذه المسارات سيتم تجاوزها بواسطة main.yml ولكن تركناها للاحتياط
android.sdk_path = /home/runner/android_sdk
android.ndk_path = /home/runner/android_sdk/ndk/25.2.9519653
android.accept_sdk_license = True

# أيقونة التطبيق (إذا أردت وضع واحدة لاحقاً)
# android.icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
