#!/bin/bash
# Security: Upload APK to Uptodown
# Requires: APK file path as argument

set -e

if [ $# -eq 0 ]; then
    echo "Usage: ./publish.sh <path-to-apk>"
    echo "Example: ./publish.sh bin/calculator-1.0.0-release.apk"
    exit 1
fi

APK_FILE="$1"

if [ ! -f "$APK_FILE" ]; then
    echo "Error: APK file not found: $APK_FILE"
    exit 1
fi

# Verify APK
echo "Verifying APK..."
unzip -t "$APK_FILE" > /dev/null
echo "✓ APK validation passed"

# Get APK info
echo ""
echo "APK Information:"
ls -lh "$APK_FILE"
echo ""
echo "SHA256: $(sha256sum "$APK_FILE")"
echo ""

# APK size check
SIZE=$(stat -f%z "$APK_FILE" 2>/dev/null || stat -c%s "$APK_FILE" 2>/dev/null)
SIZE_MB=$((SIZE / 1024 / 1024))
echo "Size: ${SIZE_MB}MB"

# Uptodown instructions
echo ""
echo "==========================================="
echo "Manual Upload to Uptodown:"
echo "==========================================="
echo ""
echo "1. Go to https://uptodown.com/api/user/account/login"
echo "2. Sign in to your Uptodown Developer Account"
echo "3. Create new app or update existing: 'Premium Calculator'"
echo "4. Upload this APK: $APK_FILE"
echo "5. Add description and screenshots"
echo "6. Set version: 1.0.0"
echo "7. Review and publish"
echo ""
echo "Note: Uptodown requires:"
echo "  - Privacy Policy"
echo "  - App description (min 100 chars)"
echo "  - At least 2 screenshots"
echo "  - Category selection"
echo ""
