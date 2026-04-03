#!/bin/bash

# Oblique Strategies Flow Script
# Usage: ./flow.sh [command]
# Commands:
#   venv        - Create and activate the virtual environment
#   build       - Build the project
#   install     - Install the package in development mode
#   test        - Run tests
#   run         - Run the application
#   clean       - Clean build artifacts
#   all         - Build, install, and run

set -e

# Function to display help
help() {
    echo "Usage: $0 [command]"
    echo "Commands:"
    echo "  venv        - Create and activate the virtual environment"
    echo "  build       - Build the project"
    echo "  install     - Install the package in development mode"
    echo "  package     - Create a standalone executable"
    echo "  test        - Run tests"
    echo "  run         - Run the application"
    echo "  clean       - Clean build artifacts"
    echo "  all         - Build, install, and run"
    exit 0
}

# Function to create and activate the virtual environment
venv() {
    echo "Setting up the virtual environment..."
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo "Virtual environment is ready. Install dependencies with: pip install -r requirements.txt"
}

# Function to build the project
build() {
    echo "Building the project..."
    poetry build
}

# Function to install the package in development mode
install() {
    echo "Installing the package in development mode..."
    pip install -e .
}

# Function to create a standalone executable
package() {
    echo "Creating standalone executable..."
    if ! command -v pyinstaller &> /dev/null; then
        echo "PyInstaller is not installed. Installing..."
        pip install pyinstaller
    fi
    
    # Clean previous builds
    rm -rf build/ dist/
    
    # Use PyInstaller with minimal options
    pyinstaller --onefile --name oblique --paths src/ --hidden-import oblique_strategies --noupx --exclude-module tk --exclude-module unittest src/oblique_strategies/__main__.py

    echo "Standalone executable created: dist/oblique"
}

# Function to run tests
test() {
    echo "Running tests..."
    # Add your test command here, for example:
    # pytest tests/
    echo "No tests defined yet."
}

# Function to run the application
run() {
    echo "Running the application..."
    oblique
}

# Function to clean build artifacts
clean() {
    echo "Cleaning build artifacts..."
    rm -rf dist/ *.egg-info/
}

# Function to run all steps
all() {
    build
    install
    run
}

# Main script logic
if [ $# -eq 0 ]; then
    help
fi

case "$1" in
    venv)
        venv
        ;;
    build)
        build
        ;;
    install)
        install
        ;;
    package)
        package
        ;;
    test)
        test
        ;;
    run)
        run
        ;;
    clean)
        clean
        ;;
    all)
        all
        ;;
    *)
        help
        ;;
esac
