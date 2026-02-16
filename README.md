# Premium Calculator - Professional Grade Mobile App

> A secure, beautiful calculator app built with Python and Kivy for mobile platforms

## 🎯 Features

✨ **Premium Design**  
- Dark theme with modern UI  
- Smooth animations  
- Intuitive button layout  
- Clean typography

🔒 **Security First**  
- Input validation & sanitization  
- No data collection  
- No external APIs  
- Secure calculation environment  
- Cryptographic signing  

⚡ **Performance**  
- Fast calculations  
- Minimal footprint  
- Smooth animations  
- No battery drain

🚀 **Automation**  
- GitHub Actions CI/CD  
- Automated APK builds  
- One-click releases  

## 📋 Requirements

### For Local Development
- Python 3.11+
- Kivy 2.2.1
- Buildozer 1.5.0
- Java 11+ (for APK building)
- Android SDK (optional for GitHub Actions builds)

### For GitHub Actions (No Local Setup Needed!)
- GitHub account
- Git knowledge
- Just push code, APK built automatically!

## 🚀 Quick Start

### Option 1: Using GitHub Actions (Recommended - No Setup!)

```bash
# 1. Clone or create repository
git clone <your-repo>
cd calculator_app

# 2. Push to GitHub
git push origin main

# 3. GitHub Actions automatically builds APK!
# Download from Actions artifacts
```

### Option 2: Local Build (Advanced)

```bash
# Install dependencies
pip install -r requirements.txt

# Build for Linux/Desktop
python main.py

# Build for Android (requires Java, Android SDK)
buildozer android debug
```

## 📦 Building APK with GitHub Actions

### First Time Setup

1. **Create GitHub repository** (if not already done)
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Premium Calculator"
   git push -u origin main
   ```

2. **Enable Actions** (if needed)
   - Go to Actions tab in GitHub
   - Click "Enable GitHub Actions"

3. **Create release trigger** (optional)
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

4. **Watch the build**
   - Go to GitHub > Actions
   - See build progress in real-time
   - Download APK from artifacts when complete!

### Building Releases

```bash
# Create version tag
git tag v1.0.1
git push origin v1.0.1

# APK is automatically built and released!
```

## 🔐 Security & Signing

### For Production Release (Uptodown)

1. Generate app signing key:
```bash
bash scripts/generate-keystore.sh
```

2. Add to GitHub Secrets:
   - `KEYSTORE_BASE64`: Base64 encoded keystore
   - `KEYSTORE_PASS`: Keystore password
   - `KEY_ALIAS`: Key alias
   - `KEY_PASS`: Key password

3. Push to GitHub - APK is automatically signed!

### Security Features Included
- ✓ 4096-bit RSA signing key
- ✓ Input validation
- ✓ Secure evaluation
- ✓ No external dependencies
- ✓ Memory-safe calculations
- ✓ No data leaks

## 📤 Publishing to Uptodown

### Prerequisites
1. **Create Uptodown Developer Account**
   - Visit: https://uptodown.com/api/user/register
   - Complete verification
   - No publishing fee! (Unlike Google Play)

2. **Prepare Marketing Materials**
   - App description (min 100 chars)
   - Screenshots (min 2, recommended 5)
   - Feature list
   - App icon (512x512 PNG)

3. **Privacy & Legal**
   - Privacy Policy (included: PRIVACY_POLICY.md)
   - Terms of Service (included: TERMS_OF_SERVICE.md)

### Upload Steps

```bash
# 1. Build APK with GitHub Actions (covered above)

# 2. Download APK from GitHub Actions artifacts

# 3. Use publish script (manual for Uptodown now)
bash scripts/publish.sh bin/calculator-release.apk

# 4. Go to Uptodown developer console
# https://uptodown.com/api/user/account

# 5. Create new app:
#    - App name: Premium Calculator
#    - Package: org.premiumdev.premiumcalc
#    - Upload APK file
#    - Add screenshots
#    - Set category: Tools/Productivity
#    - Add description

# 6. Submit for review and publish!
```

### Uptodown vs Google Play

| Feature | Uptodown | Google Play |
|---------|----------|-----------|
| Account fee | Free | $25 once |
| Publishing fee | Free | Per app |
| Review time | Hours | Days |
| Commission | 30% | 30% |
| Monetization | Direct sales, ads, IAP | All types |
| Review process | Lenient | Strict |
| Geographic coverage | Excellent | Better |

**Why Uptodown?**
- Lower barrier to entry
- Faster publishing
- Better for new developers
- Good user base in Latin America & Spain
- Alternative app store ecosystem

## 💰 Monetization Strategy

### Option 1: Direct Sales
- Charge one-time fee ($0.99 - $4.99)
- Uptodown handles payments
- 70% revenue to you, 30% to Uptodown

### Option 2: Free + Ads
- Use AdMob for banner ads
- Passive income stream
- Lower user friction

### Option 3: Premium Features
- Free version: Basic calculator
- Premium: Scientific calculator, history export, themes
- Dual pricing model

### Option 4: Multiple Stores
- Publish on multiple platforms:
  - ✓ Uptodown (easy first choice)
  - ✓ Amazon Appstore
  - ✓ F-Droid (if open-sourced)
  - ✓ Direct APK distribution

## 🔧 Customization

### Change App Name
```bash
# Edit buildozer.spec
title = Your App Name
package.name = yourappname
package.domain = org.yourdev
```

### Change Version
```bash
# Edit buildozer.spec
version = 2.0.0

# Or make git tag
git tag v2.0.0
git push origin v2.0.0
```

### Add Custom Theme
Edit `main.py` section:
```python
# In CalculatorApp.__build()
self.theme = 'dark'  # or 'light'
```

## 📊 Project Structure

```
calculator_app/
├── main.py                 # Main application
├── buildozer.spec          # Android build config
├── requirements.txt        # Python dependencies
├── PRIVACY_POLICY.md       # Required for stores
├── TERMS_OF_SERVICE.md     # Required for stores
├── .github/
│   └── workflows/
│       └── build.yml       # GitHub Actions automation
└── scripts/
    ├── generate-keystore.sh
    └── publish.sh
```

## 🐛 Troubleshooting

### APK Build Fails on GitHub Actions
1. Check build logs in Actions tab
2. Common issues:
   - Missing Java installation (unlikely on GitHub)
   - Old Gradle (run: `buildozer android release`)
   - Missing libraries (already installed)

### App Crashes on Startup
- Check logcat: `adb logcat | grep premiumcalc`
- Ensure Python dependencies are installed
- Try debug build: `buildozer android debug`

### APK too large
- Typical size: 50-100MB
- Includes full Python runtime
- Use arm64-v8a only if size critical

## 📚 Resources

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Buildozer Guide](https://buildozer.readthedocs.io/)
- [Uptodown Developer](https://uptodown.com/api/)
- [Android Signing](https://developer.android.com/studio/publish/app-signing)
- [GitHub Actions CI/CD](https://docs.github.com/en/actions)

## 📝 License

Proprietary - Premium Calculator™  
All rights reserved.  
See LICENSE file for details.

## 🤝 Support

For issues or questions:
1. Check GitHub Issues tab
2. Review documentation
3. Consult action logs

## 📈 Version History

### v1.0.0 (2026-02-16)
- Initial release
- Core calculator functionality
- Secure input validation
- GitHub Actions automation
- Ready for Uptodown

---

**Made with ❤️ by Senior Developer**  
Ready for production. Ready to sell.
