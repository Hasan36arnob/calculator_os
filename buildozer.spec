[app]

title = Premium Calculator
package.name = premiumcalc
package.domain = org.premiumdev
version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Specify versions for reproducible builds
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25.2.9519653
android.accept_sdk_license = True
android.archs = arm64-v8a

# Gradle settings for stability
android.gradle_options = org.gradle.jvmargs=-Xmx2048m
android.gradle_dependencies = 
android.entrypoint = org.kivy.android.PythonActivity
android.logcat_filters = *:S python:D

# Build settings
android.add_src = 
android.add_libs_armeabi_v8a = 

p4a.requirements = python3,kivy

[buildozer]

log_level = 2
warn_on_root = 1


