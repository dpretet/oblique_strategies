"""Core functionality for Oblique Strategies."""

import json
import random
import os


def load_strategies(lang="en"):
    """Load strategies from a JSON file based on language."""
    locale_file = os.path.join(
        os.path.dirname(__file__), "data", "locales", f"{lang}.json"
    )
    with open(locale_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["strategies"]


def draw_strategy(lang="en"):
    """Draw a random oblique strategy."""
    strategies = load_strategies(lang)
    return random.choice(strategies)
