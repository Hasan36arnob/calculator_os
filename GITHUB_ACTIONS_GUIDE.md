# GitHub Actions Troubleshooting Guide

Complete guide to troubleshoot and optimize GitHub Actions APK builds.

## 📋 Quick Checklist

Before debugging, verify:
- [ ] Repository is public (free private builds require pro)
- [ ] `.github/workflows/build.yml` exists
- [ ] All required files in root: main.py, buildozer.spec, requirements.txt
- [ ] Code pushed to GitHub successfully
- [ ] No merge conflicts

## 🔍 Common Issues & Solutions

### Issue 1: Build doesn't start

**If no Actions tab visible:**
```
1. Go to repository setting
2. Actions → Generall
3. Check "Allow all actions and reusable workflows"
4. Save
5. Push new commit - build should start now
```

**If Actions tab visible but no builds:**
```
1. Go to Actions tab
2. Enable: "I understand my workflows, re-enable them"
3. Make small commit and push
4. Build should trigger
```

### Issue 2: Build fails with "Python not found"

**Error message includes:** `python: command not found`

**Solution:**
```yaml
# Already in workflow, but verify .github/workflows/build.yml has:
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'
```

**Action:** No change needed - workflow already handles this.

### Issue 3: "Buildozer not found"

**Error message:** `buildozer: command not found`

**Solution:**
In `.github/workflows/build.yml`, verify this step exists:
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install buildozer cython
```

**Action:** Update workflow file if missing.

### Issue 4: Build times out (> 1 hour)

**Why:** Android SDK download takes time

**Solutions:**
1. GitHub Actions timeout is 6 hours - builds won't timeout first
2. Check logs for where it's stuck
3. Most builds complete in 10-20 minutes
4. First build: 15-30 minutes (caches SDKs after)

**Optimization:**
```yaml
# Add caching (already included):
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: |
      ~/.android/sdk
      ~/.gradle/wrapper
    key: ${{ runner.os }}-gradle-${{ hashFiles('**/buildozer.spec') }}
    restore-keys: ${{ runner.os }}-gradle
```

### Issue 5: APK build succeeds but artifacts not found

**Error:** `APK not found`

**Cause:** Buildozer output path different

**Solutions:**
```bash
# Check where APK actually is:
find . -name "*.apk" -type f

# Common paths:
# bin/*.apk (default)
# .buildozer/android/platform/build/build-release/outputs/apk/
```

**Action needed:** None - workflow finds it automatically.

### Issue 6: "APK validation failed"

**Error:** Security scan fails

**Common causes:**
- APK file corrupted
- Python bytecode flagged (false positive)
- Need signed APK for release

**Solutions:**
```
1. For debug builds: Usually false alarm, ignore
2. For release: Ensure keystore properly configured
3. Try: Download APK locally, check with `file` command
4. Contact Uptodown support if unsure
```

### Issue 7: Signing fails with "Keystore not found"

**Error:** `Keystore password incorrect` or `File not found`

**Cause:** GitHub Secrets not configured

**Solutions:**
```
1. Go to: Settings → Secrets and variables → Actions
2. Add these secrets:
   KEYSTORE_BASE64 = [your base64 keystore]
   KEYSTORE_PASS = [your keystore password]
   KEY_ALIAS = premiumcalc
   KEY_PASS = [your key password]

3. Verify base64 encoding:
   Windows PowerShell:
   $keystore = Get-Content -AsByteStream premiumcalc.keystore
   [Convert]::ToBase64String($keystore) | Set-Clipboard
```

### Issue 8: GitHub Actions "Resource unavailable"

**Error:** Cannot access Android SDK download

**Cause:** Temporary network issue

**Solution:**
```
1. Wait 5 minutes
2. Re-run failed job: 
   - Go to Actions → Failed build
   - Click "Re-run failed jobs"
   - Build should succeed on retry
```

### Issue 9: "Permission denied" when downloading SDKs

**Error:** `chmod: permission denied`

**Cause:** Rare - usually on first run

**Solution:**
```bash
# Permission issue usually resolves on retry
# Github Actions has proper permissions set up

# If persists:
1. Delete .buildozer folder
2. Push empty commit
3. Try rebuild
```

### Issue 10: Build succeeds but APK is blank

**Error:** App installs but shows blank screen

**Cause:** Python runtime not included properly

**Likely issue:** main.py has syntax errors

**Solutions:**
```
1. Test locally: python main.py
2. Check for errors in output
3. Fix syntax issues
4. Push updated code
5. Re-run build
```

## 🔧 Advanced Troubleshooting

### Check detailed logs

1. Go to Actions → Your build
2. Scroll to step that failed
3. Click step to expand
4. Read full error output

### Common log messages

**"Downloading SDK..."** - Normal, wait
**"Building APK..."** - Normal, can take 5+ min
**"Error: Module not found"** - Check requirements.txt
**"Gradle build failed"** - Check buildozer.spec syntax

### Export and debug locally

```powershell
# Download full build log
# Actions → Your build → Download logs

# Extract and search for errors
# Look for: "ERROR", "FATAL", "Exception"
```

### Contact support

If still stuck:
1. Take screenshot of error
2. Go to GitHub Issues (in your repo)
3. Create issue: "Build failing on GitHub Actions"
4. Include:
   - Error message
   - Build log excerpt
   - buildozer.spec content
   - main.py first 20 lines

## ⚡ Performance Optimization

### Speed up builds

**Reduce build time from 20min → 5min:**

```yaml
# In build.yml:
android.archs = arm64-v8a  # Remove armeabi-v7a

# Only build for 64-bit modern phones
# Reduces size: 100MB → 50MB
# Faster build: 20min → 5min
```

### Parallel jobs

Current workflow has two jobs:
1. `build` - Creates APK (15 min)
2. `security-scan` - Checks code (1 min)

Running parallel - both complete in ~15 min total.

### Caching improvements

Already optimized:
- ✓ Android SDK cached
- ✓ Gradle cache enabled
- ✓ Python packages cached

Cache hits save 5-10 minutes on rebuilds!

## 📊 Monitor Build Performance

### View build times

1. Actions tab
2. Select workflow
3. All-Workflows view shows build times
4. Green checkmark = success
5. Red X = failed

### Trends

First few builds: Slow (caching)
Subsequent builds: Fast (30-50% faster)

## 🔐 Secrets Security

### Best practices

**DO:**
- ✓ Use GitHub Secrets for sensitive data
- ✓ Never expose secrets in logs
- ✓ Rotate keys yearly
- ✓ Use strong passwords
- ✓ Limit secret access

**DON'T:**
- ✗ Commit keystore to GitHub
- ✗ Print secrets in logs
- ✗ Share keystore with anyone
- ✗ Use same password for all
- ✗ Disable security scanning

### Inspect secrets safely

```yaml
# View secrets (masked in logs):
- run: echo "${{ secrets.KEYSTORE_PASS }}"
# Output: ****** (masked)
```

## 🐛 Debug mode

### Enable extra logging

Edit `.github/workflows/build.yml`:
```yaml
- name: Build APK
  run: |
    export ANDROID_HOME=/opt/android-sdk
    export DEBUG=1
    buildozer android debug
    buildozer -v android debug  # Verbose
```

### Check GitHub Actions debug logs

In your repo settings:
```
Settings → Secrets and variables → Actions
Enable "Publish debug logs"
```

This provides extra information (be careful - might leak secrets!)

## 📞 Getting Help

### Where to find solutions

1. **GitHub Docs:** https://docs.github.com/en/actions
2. **Buildozer Docs:** https://buildozer.readthedocs.io/
3. **Kivy Docs:** https://kivy.org/doc/stable/
4. **Stack Overflow:** Tag "github-actions",  "buildozer"
5. **GitHub Discussions:** In your repo

### Create minimal reproduction

If reporting issue:
```bash
# Create clean test
git clone <your-repo> test
cd test
# Try to reproduce issue
# Document exact steps
```

---

**Most issues resolve by re-running the build! Give it 2 tries before investigating.** 🚀

## 💡 Pro Tips

1. **First build is slow** - Android SDK download is large
2. **Subsequent builds faster** - GitHub Actions caches SDK
3. **Test locally** - Saves GitHub Actions minutes
4. **Tag releases** - Automatic version management
5. **Check logs first** - 90% of issues visible in logs

You've got this! 🎉
