import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set aesthetic style
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Inter', 'Roboto', 'Arial']

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "results.csv")
df = pd.read_csv(data_path)

# Create a multi-panel figure
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('IEEE 754 vs. Posit 32: Dot Product Benchmark Report', fontsize=22, fontweight='bold', y=0.95)

colors = {'IEEE64': '#4A90E2', 'IEEE32': '#50C878', 'Posit32': '#E67E22'}

# 1. Error Distribution (Histogram)
ax1 = axes[0, 0]
sns.histplot(df["ieee_error"], color=colors['IEEE64'], label="IEEE 64 (Double)", ax=ax1, kde=True, alpha=0.5)
sns.histplot(df["ieee32_error"], color=colors['IEEE32'], label="IEEE 32 (Float)", ax=ax1, kde=True, alpha=0.5)
sns.histplot(df["posit_error"], color=colors['Posit32'], label="Posit 32", ax=ax1, kde=True, alpha=0.5)
ax1.set_title('Absolute Error Distribution', fontsize=16)
ax1.set_xlabel('Absolute Error', fontsize=12)
ax1.set_ylabel('Frequency', fontsize=12)
ax1.legend()

# 2. Error Comparison (Log Scale)
ax2 = axes[0, 1]
ax2.hist(df["ieee_error"], bins=20, color=colors['IEEE64'], label="IEEE 64", alpha=0.5)
ax2.hist(df["ieee32_error"], bins=20, color=colors['IEEE32'], label="IEEE 32", alpha=0.5)
ax2.hist(df["posit_error"], bins=20, color=colors['Posit32'], label="Posit 32", alpha=0.5)
ax2.set_xscale('log')
ax2.set_title('Absolute Error (Logarithmic Scale)', fontsize=16)
ax2.set_xlabel('Error (Log)', fontsize=12)
ax2.set_ylabel('Frequency', fontsize=12)
ax2.legend()

# 3. Statistical Comparison (Boxplot - Error)
ax3 = axes[1, 0]
error_data = pd.melt(df[['ieee_error', 'ieee32_error', 'posit_error']], var_name='Format', value_name='Error')
error_data['Format'] = error_data['Format'].replace({'ieee_error': 'IEEE 64', 'ieee32_error': 'IEEE 32', 'posit_error': 'Posit 32'})
sns.boxplot(data=error_data, x='Format', y='Error', palette=[colors['IEEE64'], colors['IEEE32'], colors['Posit32']], ax=ax3, width=0.5)
ax3.set_yscale('log')
ax3.set_title('Statistical Error Distribution (Log Scale)', fontsize=16)
ax3.set_ylabel('Error Range', fontsize=12)

# 4. Statistical Comparison (Boxplot - Timing)
ax4 = axes[1, 1]
time_data = pd.melt(df[['ieee_time', 'ieee32_time', 'posit_time']], var_name='Format', value_name='Time')
time_data['Format'] = time_data['Format'].replace({'ieee_time': 'IEEE 64', 'ieee32_time': 'IEEE 32', 'posit_time': 'Posit 32'})
sns.boxplot(data=time_data, x='Format', y='Time', palette=[colors['IEEE64'], colors['IEEE32'], colors['Posit32']], ax=ax4, width=0.5)
ax4.set_title('Execution Time Comparison (Seconds)', fontsize=16)
ax4.set_ylabel('Time (s)', fontsize=12)

# Adjust layout and save
plt.tight_layout(rect=[0, 0.03, 1, 0.93])
report_path = os.path.join(script_dir, "benchmark_report.png")
plt.savefig(report_path, dpi=300)
print(f"Report saved to {report_path}")
