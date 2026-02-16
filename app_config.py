"""
App Metadata Configuration
Used for versioning, branding, and distribution
"""

APP_CONFIG = {
    "app_name": "Premium Calculator",
    "package_name": "org.premiumdev.premiumcalc",
    "version": "1.0.0",
    "version_code": 1,
    "author": "Premium Dev Team",
    "description": "Professional calculator with secure design",
    "long_description": """Premium Calculator is a feature-rich calculator application 
    with beautiful design and enhanced security. Perfect for quick calculations on the go.""",
    "url": "https://uptodown.com",
    "support_email": "support@premiumdev.org",
    "privacy_policy": "https://premiumdev.org/privacy",
    "terms_of_service": "https://premiumdev.org/terms",
    
    # Monetization
    "monetization": {
        "model": "paid",  # Options: free, paid, freemium
        "price_usd": 0.99,
        "currency": "USD",
        "regions": ["US", "EU", "Latin America"],
    },
    
    # Distribution
    "stores": {
        "uptodown": {
            "enabled": True,
            "url": "https://uptodown.com/windows/item/premium-calculator",
            "requires_review": True
        },
        "google_play": {
            "enabled": False,
            "reason": "Optional - requires $25 developer account"
        }
    },
    
    # Security
    "security": {
        "min_api_level": 21,
        "target_api_level": 31,
        "signing_algorithm": "RSA-4096",
        "encryption": "AES-256",
        "obfuscation": False,
    },
    
    # Analytics (disabled for privacy)
    "analytics": {
        "enabled": False,
        "reason": "Privacy first - no tracking"
    },
    
    # Permissions
    "permissions": {
        "INTERNET": "reserved",
        "ACCESS_NETWORK_STATE": "reserved"
    }
}

def get_version():
    """Get app version"""
    return APP_CONFIG["version"]

def get_package():
    """Get package name"""
    return APP_CONFIG["package_name"]

if __name__ == "__main__":
    print(f"App: {APP_CONFIG['app_name']}")
    print(f"Version: {APP_CONFIG['version']}")
    print(f"Package: {APP_CONFIG['package_name']}")
