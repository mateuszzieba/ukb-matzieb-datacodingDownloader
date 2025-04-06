#!/bin/bash

echo "▶️  Setting up environment for ukb-matzieb-datacodingDownloader"

# Path to virtual environment
VENV_DIR=".venv"

# 1. Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
  echo "📦 Creating virtual environment in $VENV_DIR..."
  python3 -m venv "$VENV_DIR"
else
  echo "ℹ️  Virtual environment already exists — skipping creation."
fi

# 2. Activate virtual environment
source "$VENV_DIR/bin/activate"

# 3. Install required packages
echo "⬇️  Installing required Python packages..."
pip install pandas requests beautifulsoup4 openpyxl

# 4. Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
  echo "📝 Creating .gitignore file..."
  cat <<EOF > .gitignore
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
*.sqlite3
*.log
*.xlsx
*.tsv
.ipynb_checkpoints/
EOF
else
  echo "ℹ️  .gitignore file already exists — skipping."
fi

# 5. Create utils/ directory and __init__.py if missing
if [ ! -d "utils" ]; then
  mkdir -p utils
  echo "📁 Created directory: utils/"
fi

if [ ! -f "utils/__init__.py" ]; then
  touch utils/__init__.py
  echo "✅ Created file: utils/__init__.py"
fi

# 6. Create results/data-coding/ directory
mkdir -p results/data-coding

echo "✅ Environment setup complete!"
echo "📌 Activate with: source $VENV_DIR/bin/activate"
echo "🚀 Run: python main.py <data_coding_id>"
