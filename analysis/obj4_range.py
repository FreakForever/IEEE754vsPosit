import math

# IEEE float32
max_ieee = 3.4e38
min_ieee = 1.175e-38

range_ieee = max_ieee / min_ieee

# Posit32 (es=2)
useed = 2 ** (2 ** 2)  # = 16

maxpos = useed ** 30
minpos = 1 / maxpos

range_posit = maxpos / minpos

print(f"IEEE Range:  {range_ieee:.2e}")
print(f"Posit Range: {range_posit:.2e}")