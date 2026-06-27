#!/bin/bash
echo "========================================"
echo "Installing tfformat..."
echo "========================================"

# Install the Python script
sudo cp tfformat/main.py /usr/local/bin/tfformat
sudo chmod +x /usr/local/bin/tfformat

# Install the database
sudo cp tfformat/magicDB.json /usr/local/bin/

# Make it executable
sudo chmod +x /usr/local/bin/tfformat

echo "✅ Done! Type 'tfformat' anywhere."
