import math
import numpy as np
import matplotlib.pyplot as plt

ieee_bits = 23

def posit32_fraction_bits(val):
    """Exact fraction bits for posit32 (nbits=32, es=2)."""
    if val == 0:
        return 0
    nbits, es = 32, 2
    k = math.floor(math.log2(abs(val)) / (2 ** es))
    regime_len = (k + 2) if k >= 0 else (-k + 1)
    remaining = nbits - 1 - regime_len
    if remaining <= 0:
        return 0
    exp_bits = min(es, remaining)
    return max(0, remaining - exp_bits)

x = np.logspace(-40, 40, 1000)
ieee_precision = np.full_like(x, ieee_bits)
posit_precision_vals = np.array([posit32_fraction_bits(v) for v in x])

plt.semilogx(x, ieee_precision, label="IEEE-754 (float32)")
plt.semilogx(x, posit_precision_vals, label="Posit32 (es=2)")
plt.xlabel("Value Magnitude")
plt.ylabel("Fraction Bits")
plt.title("Precision Distribution")
plt.legend()
plt.savefig("analysis/obj1_precision.png", dpi=300)
print("Plot saved to analysis/obj1_precision.png")
