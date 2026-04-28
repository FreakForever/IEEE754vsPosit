import math

cases = [
    ("1/0", lambda: 1.0 / 0.0),
    ("0/0", lambda: 0.0 / 0.0),
    ("sqrt(-1)", lambda: math.sqrt(-1)),
]

for name, func in cases:
    try:
        print(name, func())
    except Exception as e:
        print(name, "Exception:", e)

print("\nIEEE produces multiple special values:")
print("NaN, Infinity, -0")

print("\nPosit:")
print("Only NaR (Not a Real)")