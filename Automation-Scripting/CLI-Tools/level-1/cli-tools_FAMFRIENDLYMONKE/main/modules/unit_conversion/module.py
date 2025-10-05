import re
from pint import UnitRegistry

def convert_units(**kwargs):
    source = kwargs.get("from")
    target = kwargs.get("to")

    # Create unit registry
    ureg = UnitRegistry()

    match_source = re.match(r"(\d+)([a-zA-Z]+)", source)
    if not match_source:
        print("Invalid '--from' format. Use like 10kg")
        return

    value, unit_from = match_source.groups()
    unit_to = target

    try:
        value = float(value)
        quantity = value * getattr(ureg, unit_from)
        result = quantity.to(unit_to)
        
        print(f"{result:.2f}")
    except (AttributeError, ValueError) as e:
        print(f"Conversion error: Invalid units or value. {str(e)}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
