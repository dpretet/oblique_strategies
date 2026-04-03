#!/bin/bash
set -e

echo "Installing Oblique Strategies..."

if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed. Please install Python3 first."
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 is required but not installed. Please install pip3 first."
    exit 1
fi

echo "Installing via pip..."
pip3 install --user --break-system-packages git+https://github.com/dpretet/oblique_strategies.git

echo "Installation complete. Run 'oblique' to draw a strategy."
