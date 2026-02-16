#!/bin/bash
# Security: Generate keystore for app signing
# Run this ONCE before first release

set -e

KEYSTORE_PATH="$HOME/.android/release.keystore"
VALIDITY_DAYS=36500  # 100 years

if [ -f "$KEYSTORE_PATH" ]; then
    echo "Keystore already exists at $KEYSTORE_PATH"
    exit 1
fi

echo "Generating keystore for app signing..."

keytool -genkey \
    -v \
    -keystore "$KEYSTORE_PATH" \
    -keyalg RSA \
    -keysize 4096 \
    -validity $VALIDITY_DAYS \
    -alias premiumcalc \
    -storepass "$(openssl rand -base64 32)" \
    -keypass "$(openssl rand -base64 32)"

echo "Keystore created successfully!"
echo "Path: $KEYSTORE_PATH"
echo ""
echo "IMPORTANT: Backup this keystore securely!"
echo "If you lose it, you cannot update your app on any app store."
echo ""
echo "To use with GitHub Actions:"
echo "1. Encode: base64 -w 0 $KEYSTORE_PATH > keystore.b64"
echo "2. Add to GitHub Secrets as KEYSTORE_BASE64"
echo "3. Also add: KEYSTORE_PASS, KEY_ALIAS, KEY_PASS to GitHub Secrets"
