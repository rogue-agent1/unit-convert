#!/usr/bin/env python3
"""Unit converter — length, weight, temperature, volume, time."""
import sys

CONVERSIONS = {
    "length": {"m":1,"km":1000,"cm":0.01,"mm":0.001,"mi":1609.344,"ft":0.3048,"in":0.0254,"yd":0.9144},
    "weight": {"kg":1,"g":0.001,"mg":0.000001,"lb":0.453592,"oz":0.0283495,"t":1000},
    "volume": {"l":1,"ml":0.001,"gal":3.78541,"qt":0.946353,"pt":0.473176,"cup":0.236588,"floz":0.0295735},
    "time": {"s":1,"ms":0.001,"us":0.000001,"min":60,"h":3600,"d":86400,"wk":604800},
}

def convert(value, from_unit, to_unit):
    from_u, to_u = from_unit.lower(), to_unit.lower()
    # Temperature special case
    if from_u in ("c","f","k") and to_u in ("c","f","k"):
        if from_u == to_u: return value
        # Convert to Celsius first
        if from_u == "f": c = (value - 32) * 5/9
        elif from_u == "k": c = value - 273.15
        else: c = value
        if to_u == "f": return c * 9/5 + 32
        elif to_u == "k": return c + 273.15
        return c
    for category in CONVERSIONS.values():
        if from_u in category and to_u in category:
            return value * category[from_u] / category[to_u]
    raise ValueError(f"Cannot convert {from_unit} to {to_unit}")

def test():
    assert abs(convert(1, "km", "m") - 1000) < 0.01
    assert abs(convert(1, "mi", "km") - 1.609344) < 0.01
    assert abs(convert(100, "c", "f") - 212) < 0.01
    assert abs(convert(32, "f", "c") - 0) < 0.01
    assert abs(convert(0, "c", "k") - 273.15) < 0.01
    assert abs(convert(1, "lb", "kg") - 0.453592) < 0.001
    assert abs(convert(1, "gal", "l") - 3.78541) < 0.01
    assert abs(convert(1, "h", "min") - 60) < 0.01
    print("  unit_convert: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else:
        v, f, t = float(sys.argv[2]), sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else (1, "km", "mi")
        print(f"{v} {f} = {convert(v, f, t):.4f} {t}")
