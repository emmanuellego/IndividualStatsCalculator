from rand_gen import RandomGenerator
from calculator import Calculator
from desc_stats import DescStats
from scipy import stats


class PopSampling:

    def simple_random(a, b, n, o):
        list = RandomGenerator.random_list(a, b, n)
        return RandomGenerator.random_select(list, o)

    def systematic_sampling(a, b, n, f):
        nlist = []
        list = RandomGenerator.random_list(a, b, n)
        for i in range (1, b):
            if i * f < len(list):
                nlist.append(list[i * f])
        return nlist

    def confidence_interval(n, a, m, s):
        zval = Zscore.ZscoreCalculatorUsingAlpha(a)
        temp = round(zval * (s / Calculator.nthroot(2, n)), 2)
        return round((m - temp), 2), round(m), round((m + temp), 2)

    def margin_of_error(r, c = 0.95):
        n = len(r)
        s = DescStats.standard_deviation(DescStats, r)
        z_score = stats.norm.ppf((1-c)/2)
        z_score = abs(z_score)
        error = (z_score * s) / Calculator.nthroot(2, n)

        return error

    def cochrans_sample(self, r, p = 0.5, c = 0.95):

        e = self.margin_of_error(r, c)
        q = 1 - p
        z = DescStats.zscorealpha(c)

        result = (Calculator.power(z,2) * p * q)/Calculator.power(e, 2)

        return result

    def confidence_interval_std(c, s, e):
        zval = DescStats.zscorealpha(c)
        temp = (zval * s)/(e / 100)

        return round((Calculator.power(temp, 2)), 2)

    def confidence_interval_noStd(c, e, p = 0.5):
        zval = DescStats.zscorealpha(c)
        q = 1 - p
        pq = p * q
        temp = Calculator.power((zval/(e/100)), 2) * pq
        return round(temp, 2)