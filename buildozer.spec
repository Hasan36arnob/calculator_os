[app]

title = Premium Calculator
package.name = premiumcalc
package.domain = org.premiumdev

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True

# Security settings
android.features = 

# App signing (configure before production)
android.keystore = 0

# Architecture
android.archs = arm64-v8a,armeabi-v7a

# Gradle
android.gradle_dependencies = 

# Build
[buildozer]

log_level = 2
warn_on_root = 1
