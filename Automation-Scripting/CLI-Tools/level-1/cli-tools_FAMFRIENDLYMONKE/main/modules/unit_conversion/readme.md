# Unit Conversion Module

Convert between different units of measurement using Python's Pint library.

## Features

- Support for multiple measurement types:
  - Weight (kg, lbs, oz)
  - Length (m, ft, in)
  - Temperature (C, F, K)
  - Volume (l, gal, ml)
  - And many more units supported by Pint!

## Usage

```sh
# Convert weight
python main.py unit-conversion --from 75kg --to lbs

# Convert length
python main.py unit-conversion --from 10m --to ft

# Convert temperature
python main.py unit-conversion --from 25C --to F
```

## Implementation Details

Uses the Pint library for accurate unit conversions with features including:

- Local conversion (no internet required)
- Extensive unit support
- High precision calculations
- Scientific notation support

## Error Handling

The module handles various error cases:

- Invalid unit formats
- Unsupported units
- Invalid numerical values
- Incompatible unit conversions

## Error Messages

- "Invalid '--from' format" - Input format should be like '10kg'
- "Conversion error" - Invalid units or values provided
- "Error during conversion" - General conversion failures

## Dependencies

- pint>=0.20
- toml>=0.10.2

## Examples

```sh
# Basic conversions
python main.py unit-conversion --from 10kg --to lbs
python main.py unit-conversion --from 100m --to ft
python main.py unit-conversion --from 1L --to ml

# Temperature conversions
python main.py unit-conversion --from 32F --to C
```
