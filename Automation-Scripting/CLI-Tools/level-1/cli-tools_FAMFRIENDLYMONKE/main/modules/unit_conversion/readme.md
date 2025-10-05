# Unit Conversion Module

Convert between different units of measurement using the API-Ninjas unit conversion API.

## Features

- Support for multiple measurement types:
  - Weight (kg, lbs, oz)
  - Length (m, ft, in)
  - Temperature (C, F, K)
  - Volume (l, gal, ml)

## Configuration

Requires API key from API-Ninjas in `.env`:

```
UNIT_CONVERSION_API_KEY=your_api_key_here
```

## Usage

```sh
# Convert weight
python main.py convert --from kg --to lbs --value 75

# Convert length
python main.py convert --from m --to ft --value 10

# Convert temperature
python main.py convert --from C --to F --value 25
```

## API Integration

Uses the API-Ninjas unit conversion endpoint for accurate conversions. Includes error handling for:

- Invalid units
- API errors
- Connection issues

## Error Messages

- "Invalid unit type" - Unit not supported
- "API error" - Problem with conversion service
- "Network error" - Connection issues

## Dependencies

- requests>=2.31.0
- python-dotenv>=1.0.0
