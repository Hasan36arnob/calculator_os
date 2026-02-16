# Setup Guide - Premium Calculator

## ✅ Prerequisites Checklist

- [ ] Python 3.8+ installed
- [ ] Git installed
- [ ] GitHub account created
- [ ] Text editor/IDE (VS Code recommended)
- [ ] Android device for testing (optional)
- [ ] ~5GB free disk space on GitHub (they provide)

## 🚀 Step-by-Step Setup

### Step 1: Clone or Create Repository

**Option A: New Repository**
```powershell
# Create folder
mkdir calculator_app
cd calculator_app

# Initialize git
git init
git config user.name "Your Name"
git config user.email "your.email@gmail.com"
```

**Option B: Clone Existing**
```powershell
git clone <repository-url>
cd calculator_app
```

### Step 2: Copy Project Files

Copy all project files into your directory:
- main.py
- buildozer.spec
- requirements.txt
- All files from scripts/
- .github/workflows/build.yml
- PRIVACY_POLICY.md
- TERMS_OF_SERVICE.md

### Step 3: Test Locally (Optional)

```powershell
# Install Python dependencies
pip install kivy==2.2.1

# Run calculator on desktop
python main.py
```

### Step 4: Push to GitHub

```powershell
# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Premium Calculator v1.0.0"

# Create main branch and push
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/calculator_app.git
git push -u origin main
```

### Step 5: Watch GitHub Actions Build

1. Go to: `https://github.com/YOUR_USERNAME/calculator_app`
2. Click **Actions** tab
3. You should see "Build APK" workflow running
4. Wait 5-15 minutes for build to complete
5. Once complete, click on the build
6. Scroll down and download **calculator-apk** artifact

✅ **You've built your first APK! 🎉**

## 🔐 For Production (Uptodown Selling)

### Step 6: Generate Signing Key

```powershell
# Download keytool if on Windows
# It's included in Java JDK

# Generate keystore
keytool -genkey -v -keystore premiumcalc.keystore `
    -keyalg RSA -keysize 4096 -validity 36500 `
    -alias premiumcalc

# When prompted:
# Keystore password: [Create strong password, save it!]
# First name: Premium Calc
# Last name: App
# Organizational Unit: Development
# Organization: YourName
# City: AnyCity
# State: AnyState
# Country: US
# CN: premiumcalc
```

⚠️ **CRITICAL: Save this keystore file and password securely!**  
Losing it means you cannot update your app forever!

### Step 7: Add to GitHub Secrets

1. Go to: `https://github.com/YOUR_USERNAME/calculator_app/settings/secrets/actions`

2. Click **New repository secret**

3. Add these secrets:

```
KEYSTORE_BASE64
Value: [Base64 encoded keystore]

KEYSTORE_PASS
Value: [Your keystore password]

KEY_ALIAS
Value: premiumcalc

KEY_PASS
Value: [Your key password]
```

**To get KEYSTORE_BASE64 on Windows PowerShell:**
```powershell
$keystore = Get-Content -AsByteStream premiumcalc.keystore
[Convert]::ToBase64String($keystore) | Set-Clipboard
# Paste from clipboard into GitHub Secret
```

### Step 8: Create Release Build

```powershell
# Update version in buildozer.spec
# version = 1.0.0

# Create git tag
git tag v1.0.0
git push origin v1.0.0

# GitHub Actions automatically builds signed APK!
```

## 📱 Uptodown Account Setup

### Create Developer Account

1. Go to: https://uptodown.com/api/user/register
2. Fill registration form
3. Verify email
4. No payment required! (unlike Google Play's $25 fee)

### Complete Developer Profile

1. Go to: https://uptodown.com/api/user/account/profile
2. Add real name
3. Add profile picture
4. Add bio/description

### Create First App Listing

1. Dashboard: https://uptodown.com/api/user/account
2. Click **New App**
3. Fill form:
   ```
   App Name: Premium Calculator
   Package: org.premiumdev.premiumcalc
   Category: Tools
   Description: Professional calculator app with secure design
   ```

## 📤 Upload APK to Uptodown

### Method 1: Manual Upload (Recommended for First Upload)

1. Download APK from GitHub Actions artifacts
2. Go to app dashboard on Uptodown
3. Click **Upload APK**
4. Select the APK file
5. Enter version: 1.0.0
6. Add description
7. Upload 2+ screenshots
8. Click **Publish**

### Method 2: Use Publish Script

```powershell
# After downloading APK
bash scripts/publish.sh path/to/apk-file.apk

# Follow the Uptodown manual steps
```

## 💰 Enable Monetization on Uptodown

### Setup Sales

1. Go to Uptodown Publisher Dashboard
2. Settings → Monetization
3. Choose pricing model:
   - Free + Ads
   - Premium (one-time purchase)
   - Free with Pro version

### Connect Payment

1. Add payment method:
   - PayPal
   - Bank transfer
   - Crypto (some regions)

2. Uptodown takes 30% commission
3. You get 70% of revenue

### Price Recommendation

For calculator:
- Free version: 0.00 USD (get users first)
- Premium: $1.99 - $2.99 USD

## 🧪 Testing Before Upload

### Desktop Testing

```powershell
python main.py

# Test operations:
# - Type: 5 + 3 =
# - Type: 10 / 2 =
# - Test: = button works
# - Test: C clears
# - Test: ← deletes last
```

### APK Testing on Phone

```powershell
# Enable USB debugging on your Android phone
# Settings → Developer Options → USB Debugging

# Connect phone via USB
adb install bin/premiumcalc-debug.apk

# Test on phone
# Uninstall: adb uninstall org.premiumdev.premiumcalc
```

## 📈 Post-Launch

### Monitor App Performance

1. Uptodown Dashboard shows:
   - Downloads count
   - Rating/reviews
   - Revenue

2. Update app regularly:
   - Bug fixes
   - New features
   - Performance improvements

### Marketing Tips

- Add good screenshots
- Write compelling description
- Respond to reviews
- Regular updates keep ranking up
- Consider free tier first to get ratings
- Advertise on social media

## 🆘 Common Issues

### Issue: GitHub Actions build fails
**Solution**: Check Logs tab in Actions → See error → Fix issue in code

### Issue: APK installation fails
**Solution**: Your phone's Android version too old
- Update buildozer.spec: `android.minapi = 21` (Android 5.0+)

### Issue: App crashes on startup
**Solution**: Check phone logs
```powershell
adb logcat | findstr premiumcalc
```

### Issue: Keystore password forgotten
**Solution**: 😞 You need to generate new keystore and create new app listing
- Never forget this password again!

## ✨ Next Steps

1. ✅ Setup complete! Push code to GitHub
2. ⏳ Wait for GitHub Actions build (5-15 min)
3. 📥 Download APK from artifacts
4. 📱 Test on phone (optional)
5. 📤 Upload to Uptodown manually first time
6. 💰 Enable price and monetization
7. 📢 Share app link with friends
8. 📈 Monitor downloads and revenue!

## 📞 Support Resources

| Issue | Resource |
|-------|----------|
| GitHub Actions help | https://docs.github.com/en/actions |
| Kivy problems | https://kivy.org/doc/stable/ |
| Buildozer questions | https://buildozer.readthedocs.io/ |
| Uptodown publishing | https://uptodown.com/api/ |
| Android development | https://developer.android.com |

---

**You're ready! Good luck with your app! 🚀**
