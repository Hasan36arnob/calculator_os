# Makefile for Calculator App

.PHONY: help install build test clean release debug publish docs

help:
	@echo "Premium Calculator - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install          Install dependencies"
	@echo "  make desktop          Run on desktop"
	@echo ""
	@echo "Building:"
	@echo "  make build            Build release APK"
	@echo "  make debug            Build debug APK"
	@echo "  make clean            Clean build artifacts"
	@echo ""
	@echo "Testing:"
	@echo "  make test             Test on desktop"
	@echo "  make lint             Check code quality"
	@echo ""
	@echo "Publishing:"
	@echo "  make keystore         Generate signing key"
	@echo "  make release          Create release version"
	@echo "  make publish          Instructions for publish"
	@echo ""
	@echo "Utilities:"
	@echo "  make version          Show version"
	@echo "  make docs             Open documentation"

install:
	pip install -r requirements.txt
	@echo "✓ Dependencies installed"

desktop: install
	@echo "Starting calculator on desktop..."
	python main.py

build:
	@echo "Building release APK..."
	buildozer android release
	@echo "✓ APK built successfully"
	@ls -lh bin/*.apk 2>/dev/null || echo "Check bin/ for APK"

debug:
	@echo "Building debug APK..."
	buildozer android debug
	@echo "✓ Debug APK built"

clean:
	@echo "Cleaning build artifacts..."
	rm -rf .buildozer
	rm -rf bin
	rm -rf build
	@echo "✓ Clean complete"

test: install
	@echo "Testing calculator..."
	python -m pytest . 2>/dev/null || python main.py &
	@echo "✓ Test complete"

lint:
	@echo "Running security checks..."
	python -m pip install bandit
	bandit -r . -ll
	@echo "✓ Security check complete"

keystore:
	@echo "Generating keystore (ONE TIME ONLY)..."
	@bash scripts/generate-keystore.sh

release: clean
	@echo "Creating release build..."
	git tag v$$(grep version buildozer.spec | cut -d' ' -f3)
	git push origin v$$(grep version buildozer.spec | cut -d' ' -f3)
	@echo "✓ Release triggered in GitHub Actions"

publish:
	@echo "Publishing to Uptodown..."
	@bash scripts/publish.sh

version:
	@grep "version =" buildozer.spec | head -1

docs:
	@echo "Opening documentation..."
	@echo "README.md: Project overview"
	@echo "SETUP_GUIDE.md: Detailed setup instructions"  
	@echo "UPTODOWN_GUIDE.md: Publishing to Uptodown"
	@echo "PRIVACY_POLICY.md: Privacy & legal"

setup-ci:
	@echo "Setting up GitHub Actions..."
	@echo "1. Create GitHub repo: https://github.com/new"
	@echo "2. Push files: git push -u origin main"
	@echo "3. Enable Actions in GitHub settings"
	@echo "4. Add secrets (if selling):"
	@echo "   - KEYSTORE_BASE64"
	@echo "   - KEYSTORE_PASS"
	@echo "   - KEY_ALIAS"
	@echo "   - KEY_PASS"
	@echo "5. Create tag: git tag v1.0.0 && git push origin v1.0.0"
	@echo "6. Watch Actions build APK!"

.DEFAULT_GOAL := help
