[app]
title = Sovereign Architect
package.name = sovereign_architect
package.domain = com.sovereign.engine
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 2.5
requirements = python3,kivy,requests,urllib3,certifi

# الصلاحيات السيادية [2026-01-11]
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, ACCESS_NETWORK_STATE

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.allow_backup = True

# منع الأخطاء التي واجهناها سابقاً
android.skip_update = False
android.accept_sdk_license = True
android.no_byte_compile_python_optimization = True
