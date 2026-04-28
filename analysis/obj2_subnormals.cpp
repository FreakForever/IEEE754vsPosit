#include <iostream>
#include <chrono>
#include <cmath>
extern "C" {
    #include "softposit.h"
}

int main() {
    float x = 1e-40; // subnormal
    float y = 1.1f;
    long iterations = 10000000;

    auto start_ieee = std::chrono::high_resolution_clock::now();
    for (long i = 0; i < iterations; i++) {
        volatile float res = x * y;
    }
    auto end_ieee = std::chrono::high_resolution_clock::now();
    std::cout << "IEEE time (" << iterations << " ops): "
              << std::chrono::duration<double>(end_ieee - start_ieee).count()
              << " s" << std::endl;

    posit32_t px = convertDoubleToP32(1e-40);
    posit32_t py = convertDoubleToP32(1.1);

    auto start_posit = std::chrono::high_resolution_clock::now();
    for (long i = 0; i < iterations; i++) {
        volatile posit32_t pres = p32_mul(px, py);
    }
    auto end_posit = std::chrono::high_resolution_clock::now();
    std::cout << "Posit time (" << iterations << " ops): "
              << std::chrono::duration<double>(end_posit - start_posit).count()
              << " s" << std::endl;
}