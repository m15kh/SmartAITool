#!/bin/bash
set -e

# Check if version is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <new-version>"
    exit 1
fi

NEW_VERSION=$1

# Update version in setup.py
if [ -f "setup.py" ]; then
    sed -i "s/version=\"[^\"]*\"/version=\"$NEW_VERSION\"/g" setup.py
    echo "Updated version to $NEW_VERSION in setup.py"
fi

# Update version in pyproject.toml
if [ -f "pyproject.toml" ]; then
    sed -i "s/version = \"[^\"]*\"/version = \"$NEW_VERSION\"/g" pyproject.toml
    echo "Updated version to $NEW_VERSION in pyproject.toml"
fi

# Update version in all yoml files
for yoml_file in *.yoml; do
    if [ -f "$yoml_file" ]; then
        sed -i "s/version: .*/version: $NEW_VERSION/g" "$yoml_file"
        echo "Updated version to $NEW_VERSION in $yoml_file"
    fi
done

echo "Using version $NEW_VERSION to publish!"

# Clean up any old builds
rm -rf dist/ build/ *.egg-info/

# Build the package
python -m build

# Upload to PyPI
python -m twine upload dist/* --verbose

echo "Successfully published version $NEW_VERSION to PyPI!"
