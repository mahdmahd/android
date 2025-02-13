[app]
# (str) Title of your application
title = OpenAI Kivy App

# (str) Package name
package.name = openaiapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located.
source.dir = .
# (list) File extensions to include (you can adjust if you have additional files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Here we include python3, kivy, and openai (plus any other dependencies you may have)
requirements = python3,kivy,openai

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Whether to use fullscreen mode (1 for yes, 0 for no)
fullscreen = 0

# (list) Permissions
# The INTERNET permission is needed for making API calls to OpenAI.
android.permissions = INTERNET

# (int) Android API to use (29 is common; adjust if needed)
android.api = 29

# (int) Minimum API your APK will support (21 is a safe minimum)
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 20

# (str) Android NDK version to use (the recommended version is usually 21b)
android.ndk = 21b

# (bool) Use --private data storage (True) or external storage (False)
android.private_storage = True

# (int) Application version code (integer, increment with each release)
version_code = 1

# (str) Application version
version = 0.1

[buildozer]
# (int) log level (2 = debug, 1 = info, 0 = critical)
log_level = 2
warn_on_root = 1
