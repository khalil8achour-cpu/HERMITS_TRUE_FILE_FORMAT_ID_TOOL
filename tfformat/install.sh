#!/bin/bash
echo "========================================"
echo "Installing tfformat..."
echo "========================================"
sudo cp tfformat/main.py /usr/local/bin/tfformat
sudo chmod +x /usr/local/bin/tfformat
sudo cp tfformat/magicDB.json /usr/local/bin/
sudo chmod +x /usr/local/bin/tfformat

echo "✅ Done! Type 'tfformat' anywhere."
