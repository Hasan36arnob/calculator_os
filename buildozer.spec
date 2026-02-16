[app]

title = Premium Calculator
package.name = premiumcalc
package.domain = org.premiumdev
version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy

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

[buildozer]

log_level = 2
warn_on_root = 1


