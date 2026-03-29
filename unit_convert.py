#!/usr/bin/env python3
"""Unit converter — length, weight, temperature, volume, speed, data."""
import sys

CONVERSIONS = {
    "length": {"m": 1, "km": 1000, "cm": 0.01, "mm": 0.001, "mi": 1609.344, "ft": 0.3048, "in": 0.0254, "yd": 0.9144},
    "weight": {"kg": 1, "g": 0.001, "mg": 1e-6, "lb": 0.453592, "oz": 0.0283495, "ton": 907.185},
    "volume": {"l": 1, "ml": 0.001, "gal": 3.78541, "qt": 0.946353, "pt": 0.473176, "cup": 0.236588, "floz": 0.0295735},
    "speed": {"mps": 1, "kph": 1/3.6, "mph": 0.44704, "knot": 0.514444},
    "data": {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4},
}

def convert(value, from_unit, to_unit):
    for cat, units in CONVERSIONS.items():
        if from_unit in units and to_unit in units:
            return value * units[from_unit] / units[to_unit]
    return None

def celsius_to_f(c): return c * 9/5 + 32
def f_to_celsius(f): return (f - 32) * 5/9
def celsius_to_k(c): return c + 273.15
def k_to_celsius(k): return k - 273.15

def convert_temp(value, from_u, to_u):
    if from_u == to_u: return value
    to_c = {"C": lambda x: x, "F": f_to_celsius, "K": k_to_celsius}
    from_c = {"C": lambda x: x, "F": celsius_to_f, "K": celsius_to_k}
    return from_c[to_u](to_c[from_u](value))

def main():
    if len(sys.argv) < 2: print("Usage: unit_convert.py <demo|test|value from to>"); return
    if sys.argv[1] == "test":
        assert abs(convert(1, "km", "m") - 1000) < 0.01
        assert abs(convert(1, "mi", "km") - 1.609) < 0.01
        assert abs(convert(1, "lb", "kg") - 0.4536) < 0.01
        assert abs(convert(1, "gal", "l") - 3.785) < 0.01
        assert convert(1, "GB", "MB") == 1024
        assert abs(convert_temp(100, "C", "F") - 212) < 0.01
        assert abs(convert_temp(32, "F", "C") - 0) < 0.01
        assert abs(convert_temp(0, "C", "K") - 273.15) < 0.01
        assert convert_temp(100, "C", "C") == 100
        assert convert(1, "km", "nonsense") is None
        print("All tests passed!")
    else:
        if len(sys.argv) == 5:
            v, f, t = float(sys.argv[2]), sys.argv[3], sys.argv[4]
            if f in "CFK" and t in "CFK": print(f"{v} {f} = {convert_temp(v, f, t):.4f} {t}")
            else:
                r = convert(v, f, t)
                print(f"{v} {f} = {r:.6f} {t}" if r else "Unknown units")

if __name__ == "__main__": main()
