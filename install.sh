#!/usr/bin/env bash

echo "Installing OSCi..."

# Python tekshir
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python3 yo‘q. O‘rnating:"
    echo "Alpine: apk add python3"
    echo "Termux: pkg install python"
    exit 1
fi

# Git tekshir
if ! command -v git >/dev/null 2>&1; then
    echo "Git yo‘q. O‘rnating:"
    echo "Alpine: apk add git"
    echo "Termux: pkg install git"
    exit 1
fi

# OSCi yuklash
rm -rf $HOME/OSCi
git clone https://github.com/qw123456qwe/OSCi.git $HOME/OSCi

# OS aniqlash
if [ -d "/data/data/com.termux" ]; then
    BIN="$PREFIX/bin"
else
    BIN="/usr/bin"
fi

# CLI yaratish
cat > $BIN/osc << 'EOF'
#!/usr/bin/env bash
python3 $HOME/OSCi/run.py "$@"
EOF

chmod +x $BIN/osc

echo "OSCi installed successfully!"
echo "Run: osc test.osc"
