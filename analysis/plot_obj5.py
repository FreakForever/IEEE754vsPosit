import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure we can run from root or analysis dir
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "results.csv")
df = pd.read_csv(data_path)

plt.figure(figsize=(10, 6))
plt.boxplot([df["ieee_error"], df["ieee32_error"], df["posit_error"]],
            labels=["IEEE 64", "IEEE 32", "Posit 32"])
plt.yscale('log')
plt.title("Numerical Accuracy Comparison (Log Scale)")
plt.ylabel("Absolute Error")
plt.grid(True, which="both", ls="-", alpha=0.5)

output_path = os.path.join(script_dir, "obj5_accuracy_boxplot.png")
plt.savefig(output_path, dpi=300)
print(f"Plot saved to {output_path}")
