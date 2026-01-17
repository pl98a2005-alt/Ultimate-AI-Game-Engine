[app]
title = Sovereign Architect
package.name = sovereign_architect
package.domain = com.sovereign.engine
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,bin
version = 1.25
requirements = python3,kivy

# الوضع الأفقي لضمان القبول
orientation = landscape

fullscreen = 1

# --- الإعدادات التصحيحية للقضاء على خطأ Aidl ---
android.api = 33
android.minapi = 21
android.ndk = 25.2.9519653
android.build_tools_version = 33.0.0
# منع النظام من البحث عن تحديثات تسبب ضياع المسارات
android.skip_update = False
android.accept_sdk_license = True

android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET
android.archs = arm64-v8a, armeabi-v7a
android.enable_vulkan = True

[buildozer]
log_level = 2
bin_dir = ./bin
