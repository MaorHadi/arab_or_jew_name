echo "📦 Deactivating existing virtual environment..."
if [[ -n "$VIRTUAL_ENV" ]]; then
    deactivate 2>/dev/null || true
    echo "✅ Deactivated previous virtual environment"
else
    echo "ℹ️  No active virtual environment to deactivate"
fi
# Remove existing virtual environment
echo "🗑️  Removing existing .venv directory..."
rm -rf .venv

# Create new virtual environment
echo "🔨 Creating new virtual environment..."
python -m venv .venv

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source .venv/Scripts/activate


# Verify activation
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Virtual environment activated: $VIRTUAL_ENV"
else
    echo "❌ Failed to activate virtual environment"
    exit 1
fi

# Install requirements
echo "📚 Installing requirements..."
if [[ -f "requirements.txt" ]]; then
    pip install -r requirements.txt
    echo "✅ Requirements installed successfully"
else
    echo "⚠️  Warning: requirements.txt not found"
fi
