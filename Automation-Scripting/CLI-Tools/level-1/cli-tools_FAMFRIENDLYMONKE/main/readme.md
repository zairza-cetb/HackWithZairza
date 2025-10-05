# CLI Tools

A collection of command-line tools for common calculations and conversions.

## Features

- Unit conversion between different measurement systems
- Modular architecture for easy extension
- Configuration via TOML files
- Environment variable support for API keys

## Installation

1. Clone the repository
2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your API keys

## Available Modules

- [Unit Conversion](modules/unit_conversion/README.md) - Convert between different units of measurement

## Usage

Basic unit conversion:

```sh
python main.py convert --from kg --to lbs --value 75
```

For detailed options:

```sh
python main.py --help
```

## Project Structure

```
.
├── .env.example          # Template for environment variables
├── main.py              # Main entry point
├── cli_tools/           # Core CLI functionality
│   ├── cli.py          # CLI implementation
│   └── options.toml     # Configuration
└── modules/            # Tool modules
    └── unit_conversion/ # Unit conversion module
```

## Contributing

1. Choose a new tool to implement
2. Create a module in the `modules` directory
3. Add configuration to `options.toml`
4. Update documentation

## License

MIT License - See LICENSE file for details
