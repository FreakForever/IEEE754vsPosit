#include "benchmarks.h"
#include "ieee.h"
#include "posit.h"
#include "mpfr_ref.h"
#include "utils.h"

#include <fstream>
#include <chrono>
#include <iostream>
#include <iomanip>

void run_dot_product_benchmark() {
    std::ofstream file("data/results.csv");
    file << "ieee_error,ieee32_error,posit_error,ieee_time,ieee32_time,posit_time\n";

    double total_err_ieee = 0, total_err_ieee32 = 0, total_err_posit = 0;
    double total_time_ieee = 0, total_time_ieee32 = 0, total_time_posit = 0;
    const int num_trials = 100;

    std::cout << "Starting benchmark (" << num_trials << " trials of 1000-element dot products)..." << std::endl;

    for (int trial = 0; trial < num_trials; trial++) {
        auto a = generate_random_vector(1000);
        auto b = generate_random_vector(1000);

        // IEEE 64
        auto start = std::chrono::high_resolution_clock::now();
        double ieee = dot_ieee(a, b);
        auto end = std::chrono::high_resolution_clock::now();
        double ieee_time = std::chrono::duration<double>(end - start).count();

        // IEEE 32
        start = std::chrono::high_resolution_clock::now();
        double ieee32 = dot_ieee32(a, b);
        end = std::chrono::high_resolution_clock::now();
        double ieee32_time = std::chrono::duration<double>(end - start).count();

        // Posit 32
        start = std::chrono::high_resolution_clock::now();
        double posit = dot_posit(a, b);
        end = std::chrono::high_resolution_clock::now();
        double posit_time = std::chrono::duration<double>(end - start).count();

        // Ground truth (256-bit)
        double truth = dot_mpfr(a, b);

        double err_ieee = compute_error(ieee, truth);
        double err_ieee32 = compute_error(ieee32, truth);
        double err_posit = compute_error(posit, truth);

        file << err_ieee << "," << err_ieee32 << "," << err_posit << ","
             << ieee_time << "," << ieee32_time << "," << posit_time << "\n";

        total_err_ieee += err_ieee;
        total_err_ieee32 += err_ieee32;
        total_err_posit += err_posit;
        total_time_ieee += ieee_time;
        total_time_ieee32 += ieee32_time;
        total_time_posit += posit_time;

        if ((trial + 1) % 10 == 0) {
            std::cout << "Progress: " << (trial + 1) << "%" << std::endl;
        }
    }

    file.close();

    // Print Terminal Summary Table
    std::cout << "\n" << std::setfill('=') << std::setw(65) << "" << std::endl;
    std::cout << std::setfill(' ') << std::left << std::setw(15) << "Metric" 
              << std::setw(18) << "IEEE 754 (64)" 
              << std::setw(18) << "IEEE 754 (32)" 
              << std::setw(15) << "Posit 32" << std::endl;
    std::cout << std::setfill('-') << std::setw(65) << "" << std::endl;
    std::cout << std::setfill(' ') << std::left << std::setw(15) << "Avg Error" 
              << std::setw(18) << (total_err_ieee / num_trials) 
              << std::setw(18) << (total_err_ieee32 / num_trials) 
              << std::setw(15) << (total_err_posit / num_trials) << std::endl;
    std::cout << std::left << std::setw(15) << "Avg Time (s)" 
              << std::setw(18) << (total_time_ieee / num_trials) 
              << std::setw(18) << (total_time_ieee32 / num_trials) 
              << std::setw(15) << (total_time_posit / num_trials) << std::endl;
    std::cout << std::setfill('=') << std::setw(65) << "" << "\n" << std::endl;
}
double running_sum_ieee(const std::vector<float>& a) {
    float sum = 0;
    for (auto v : a) sum += v;
    return sum;
}
double horner_ieee(const std::vector<float>& coeffs, float x) {
    float result = 0;
    for (int i = coeffs.size() - 1; i >= 0; i--) {
        result = result * x + coeffs[i];
    }
    return result;
}