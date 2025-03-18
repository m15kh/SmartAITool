# SmartAITool

A smart AI tool package for Python that provides useful utilities for terminal output formatting and data processing.

## Installation

```bash
pip install SmartAITool
```

## Usage

### Colored Terminal Output

```python
from SmartAITool import core

# Print with colored output
core.cprint("Success message", "green")
core.cprint("Error message", "red")
core.cprint("Warning message", "yellow")
core.cprint("Information message", "blue")
```

### Data Processing

```python
from SmartAITool import core

# Process data
result = core.process_data("your input data")
print(result)
```

## Features

- **Colored Terminal Output**: Easy-to-use colored text printing in terminal
- **Support for 8 Colors**: black, red, green, yellow, blue, magenta, cyan, white
- **Simple API**: Intuitive and straightforward functions

## Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/m15kh/SmartAITool.git
cd SmartAITool

# Install development dependencies
pip install -r requirements-dev.txt

# Install the package in development mode
pip install -e .
```

### Running tests

```bash
pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
