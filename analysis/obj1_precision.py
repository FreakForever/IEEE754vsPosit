import numpy as np
import matplotlib.pyplot as plt

# IEEE float32 precision = constant
ieee_bits = 23

x = np.logspace(-40, 40, 1000)

# IEEE: constant except subnormal
ieee_precision = np.full_like(x, ieee_bits)

# simulate posit tapered precision (approximation)
def posit_precision(val):
    if 0.5 <= val <= 2:
        return 27  # peak near 1
    elif val < 1:
        return max(5, int(27 + np.log2(val)))
    else:
        return max(5, int(27 - np.log2(val)))

posit_precision_vals = np.array([posit_precision(v) for v in x])

plt.semilogx(x, ieee_precision, label="IEEE-754")
plt.semilogx(x, posit_precision_vals, label="Posit (approx)")
plt.xlabel("Value Magnitude")
plt.ylabel("Fraction Bits")
plt.title("Precision Distribution")
plt.legend()
plt.savefig("analysis/obj1_precision.png", dpi=300)
print("Plot saved to analysis/obj1_precision.png")
# plt.show()