# Oblique Strategies

A Python tool to draw Oblique Strategies by Brian Eno.

## Installation

### Via PyPI
```bash
pip install oblique-strategies
```

### Via curl
```bash
curl -sSL https://raw.githubusercontent.com/dpretet/oblique_strategies/main/scripts/install.sh | bash
```

### Via Homebrew (coming soon)
```bash
brew tap dpretet/oblique
brew install oblique
```

## Usage

```bash
oblique  # Launch the Textual TUI interface
```

## Development

1. Clone the repository:
   ```bash
   git clone https://github.com/dpretet/oblique_strategies.git
   cd oblique_strategies
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install poetry rich
   ```

4. Install the package in development mode:
   ```bash
   poetry install
   ```

5. Run the CLI:
   ```bash
   python3 -m oblique_strategies.cli --lang fr
   ```

## License

MIT
