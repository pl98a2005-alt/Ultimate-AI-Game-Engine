[app]
title = Game Architect Φ
package.name = sovereign.phi.architect
package.domain = org.king
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0.0
requirements = python3,kivy,requests,urllib3,certifi,idna

# أيقونة التطبيق (O بوسطها شخطة)
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# الصلاحيات المطلوبة للتحميل الداخلي للموارد
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# قبول التراخيص تلقائياً
android.accept_sdk_license = True
log_level = 2
