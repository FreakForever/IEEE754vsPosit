# IEEE 754 vs. Posit Arithmetic Benchmark

This project provides a comprehensive comparative analysis of the **IEEE 754 standard** (32-bit and 64-bit) and the **Posit 32** arithmetic format. It evaluates both numerical accuracy (using 256-bit MPFR as ground truth) and execution performance for vector dot product operations.

## Features
- **Accuracy Benchmarking**: Compares IEEE 64, IEEE 32, and Posit 32 against high-precision MPFR.
- **Performance Profiling**: Measures execution time for hardware-accelerated IEEE vs. software-emulated Posit.
- **Tapered Precision Analysis**: Visualizes the precision distribution of Posits across different magnitudes.
- **Dynamic Range Evaluation**: Compares the representable span of both formats.
- **Subnormal Stress Testing**: Profiles performance when handling extremely small values.

## Prerequisites
To build and run this project, you need:
- **C++ Compiler**: GCC or Clang (supporting C++17).
- **Python 3**: For data visualization (requires `pandas`, `matplotlib`, and `seaborn`).
- **MPFR & GMP Libraries**: For high-precision ground truth.
  - macOS: `brew install mpfr gmp`
  - Linux: `sudo apt-get install libmpfr-dev libgmp-dev`

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/FreakForever/IEEE745vsPosit.git
cd IEEE745vsPosit
```

### 2. Setup External Libraries
Since the project relies on the **SoftPosit** library (which is excluded from this repository for size), you must set it up manually:

```bash
mkdir -p external
git clone https://gitlab.com/cerlane/SoftPosit.git external/SoftPosit

# Build SoftPosit (Architecture dependent)
# For most 64-bit systems:
make -C external/SoftPosit/build/Linux-x86_64-GCC
```

### 3. Build the Project
```bash
make
```

## Running the Benchmarks

### Primary Benchmark
Run the dot product precision and performance comparison:
```bash
mkdir -p data
./main
```
This generates `data/results.csv` and prints a summary table to the terminal. The `data/` directory must exist beforehand or the CSV will silently not be written.

### Primary Benchmark Report
Generate the multi-panel benchmark report (`analysis/benchmark_report.png`) from the CSV:
```bash
python3 analysis/plot.py
```

### Analysis Suite
To run the extended analysis objectives (Precision distribution, Dynamic range, Exceptions, etc.):
```bash
bash run_analysis.sh
```
This will generate diagnostic plots and text results in the `analysis/` directory.

## Visualizations
The project generates several visualizations:
- `analysis/benchmark_report.png`: Primary comparison report.
- `analysis/obj1_precision.png`: Tapered precision visualization.
- `analysis/obj5_accuracy_boxplot.png`: Statistical error distribution.

## License
This project is for educational and research purposes. SoftPosit is licensed under its own terms (see `external/SoftPosit/LICENSE`).
