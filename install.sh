#!/data/data/com.termux/files/usr/bin/bash

echo "Installing OSCi v1..."

rm -rf $HOME/OSCi
git clone https://github.com/qw123456qwe/OSCi.git $HOME/OSCi

cat > $PREFIX/bin/osc << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
bash $HOME/OSCi/osc "$@"
EOF

chmod +x $PREFIX/bin/osc

echo "OSCi v1 installed!"
echo "Run: osc test.osc"
