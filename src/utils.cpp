#include "utils.h"
#include <random>
#include <cmath>

std::vector<float> generate_random_vector(int n) {
    std::vector<float> v(n);
    static std::mt19937 gen(42);
    static std::uniform_real_distribution<float> dist(0.0, 1.0);

    for (int i = 0; i < n; i++)
        v[i] = dist(gen);

    return v;
}

double compute_error(double approx, double truth) {
    return fabs(approx - truth);
}