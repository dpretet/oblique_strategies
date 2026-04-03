#!/usr/bin/env python3
"""Main entry point for Oblique Strategies."""

import sys
import os

# Ajout du chemin src au PYTHONPATH si nécessaire
if getattr(sys, 'frozen', False):
    # Si nous sommes dans un exécutable PyInstaller
    application_path = os.path.dirname(sys.executable)
else:
    # Si nous sommes en développement
    application_path = os.path.dirname(os.path.abspath(__file__))

# Ajout du chemin src au PYTHONPATH
src_path = os.path.join(os.path.dirname(application_path), 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from oblique_strategies.cli import main

if __name__ == "__main__":
    main()
