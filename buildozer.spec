[app]

title = Premium Calculator
package.name = premiumcalc
package.domain = org.premiumdev

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# Core requirements
requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0

# Minimal permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# API levels
android.api = 31
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True

# Security settings
android.features = 

# App signing
android.keystore = 0

# Single architecture for faster builds (arm64 only)
android.archs = arm64-v8a

# Gradle settings for reliability
android.gradle_dependencies = 
android.gradle_options = org.gradle.jvmargs=-Xmx2048m

# App metadata
android.window = 1
android.presplash_iconsize = 50

# Build settings
[buildozer]

log_level = 2
warn_on_root = 1

