[app]
title = Sovereign Architect
package.name = sovereign_architect
package.domain = com.sovereign.engine
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,bin
version = 1.25
requirements = python3,kivy

# التعديل الذهبي هنا:
orientation = landscape

fullscreen = 1
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.enable_vulkan = True
android.accept_sdk_license = True
android.skip_update = True

[buildozer]
log_level = 2
bin_dir = ./bin
