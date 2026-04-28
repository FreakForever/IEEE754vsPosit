#include "mpfr_ref.h"
#include <mpfr.h>

double dot_mpfr(const std::vector<float>& a, const std::vector<float>& b) {
    mpfr_t sum, temp;
    mpfr_init2(sum, 256);
    mpfr_init2(temp, 256);

    mpfr_set_d(sum, 0.0, MPFR_RNDN);

    for (int i = 0; i < a.size(); i++) {
        mpfr_set_d(temp, a[i], MPFR_RNDN);
        mpfr_mul_d(temp, temp, b[i], MPFR_RNDN);
        mpfr_add(sum, sum, temp, MPFR_RNDN);
    }

    double result = mpfr_get_d(sum, MPFR_RNDN);

    mpfr_clear(sum);
    mpfr_clear(temp);

    return result;
}