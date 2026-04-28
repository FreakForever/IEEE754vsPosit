#include "posit.h"

extern "C" {
    #include "softposit.h"
}

double dot_posit(const std::vector<float>& a, const std::vector<float>& b) {
    posit32_t sum = convertDoubleToP32(0.0);

    for (int i = 0; i < a.size(); i++) {
        posit32_t pa = convertDoubleToP32(a[i]);
        posit32_t pb = convertDoubleToP32(b[i]);

        posit32_t prod = p32_mul(pa, pb);
        sum = p32_add(sum, prod);
    }

    return convertP32ToDouble(sum);
}