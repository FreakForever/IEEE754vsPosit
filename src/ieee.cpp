#include "ieee.h"

double dot_ieee(const std::vector<float>& a, const std::vector<float>& b) {
    double sum = 0.0;
    for (int i = 0; i < a.size(); i++) {
        sum += (double)a[i] * (double)b[i];
    }
    return sum;
}

double dot_ieee32(const std::vector<float>& a, const std::vector<float>& b) {
    float sum = 0.0f;
    for (int i = 0; i < a.size(); i++) {
        sum += a[i] * b[i];
    }
    return (double)sum;
}