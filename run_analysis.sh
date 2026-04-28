#!/bin/bash

echo "=== Running Analysis Suite ==="

# 1. Precision Distribution
echo "[1/5] Running Objective 1: Precision Distribution..."
python3 analysis/obj1_precision.py

# 2. Subnormals Performance
echo "[2/5] Compiling and Running Objective 2: Subnormals Performance..."
g++ -std=c++17 -Iinclude -Iexternal/SoftPosit/source/include analysis/obj2_subnormals.cpp external/SoftPosit/build/Linux-x86_64-GCC/softposit.a -o analysis/obj2_subnormals
./analysis/obj2_subnormals > analysis/obj2_results.txt
echo "Results saved to analysis/obj2_results.txt"

# 3. Exceptions
echo "[3/5] Running Objective 3: Exceptions..."
python3 analysis/obj3_exceptions.py > analysis/obj3_results.txt
echo "Results saved to analysis/obj3_results.txt"

# 4. Range
echo "[4/5] Running Objective 4: Range..."
python3 analysis/obj4_range.py > analysis/obj4_results.txt
echo "Results saved to analysis/obj4_results.txt"

# 5. Accuracy Boxplot
echo "[5/5] Running Objective 5: Accuracy Boxplot..."
python3 analysis/plot_obj5.py

echo "=== Analysis Suite Complete ==="
