from collections import Counter
from calculator import Calculator
from numpy import absolute
from scipy import stats


class DescStats:

    def mean(r):
        return Calculator.addsums(r) / len(r)

    def median(r):
        r.sort()
        if len(r) % 2 == 0:
            return (r[len(r) // 2] + r[len(r) // 2 - 1]) / 2
        return r[len(r) // 2]

    def mode(r):
        n = Counter(r)
        get_mode = dict(n)
        m = [k for k, v in get_mode.items() if v == max(list(n.values()))]

        if len(m) == len(r):
            return -1
        else:
            get_mode = int(''.join(map(str, m)))
        return get_mode

    def standard_deviation(self, r):
        n = []
        r.sort()
        mean = self.mean(r)
        for i in r:
            n.append(Calculator.power((i - mean), 2))
        s = Calculator.addsums(n)

        return Calculator.nthroot(2, Calculator.divide(s, len(r)))

    def zscore(self, r):
        n = []
        for i in r:
            temp = (i - self.mean(r)) / self.standard_deviation(self, r)
            n.append(temp)
        return n

    def zscorealpha(ci):
        z = stats.norm.ppf((1 - ci) / 2)
        z = abs(z)
        return round(z, 2)

    def variance(self, r):
        return Calculator.power(self.standard_deviation(self, r), 2)

    def quart(self, r):
        mid = self.median(r)
        first = mid / 2
        second = mid + first

        return [first, mid, second]

    def skew(self, r):
        mean = self.mean(r)
        median = self.median(r)
        s = self.standard_deviation(self, r)

        sk = (3 * (mean - median)) / s

        return sk

    def sample_correlation(a, b):
        if (len(a) == len(b)):
            n = len(a)
            sum_a = float(Calculator.addsums(a))
            sum_b = float(Calculator.addsums(b))
            sum_a_sq = sum(map(lambda x: pow(a, 2), a))
            sum_b_sq = sum(map(lambda x: pow(a, 2), b))
            psum = sum(map(lambda x, y: x * y, a, b))
            num = psum - (sum_a * sum_b / n)
            den = pow((sum_a_sq - pow(sum_a, 2) / n) * (sum_b_sq - pow(sum_b, 2) / n), 0.5)
            if den == 0:
                return 0
            else:
                return -1
            return num / den

    def population_correlation(self, a, b):
        m = 0
        n = 0
        if len(a) == len(b):
            for x,y in zip(a,b):
                n += 1
                if (((x - self.mean(a)) < 0) or ((y - self.mean(b) < 0)) and (not ((x - self.mean(a) < 0 and (y - self.mean(b)) < 0)))):
                    m -= int(x - self.mean(a)) * int(y - self.mean(b))
                else:
                    m += int(x - self.mean(a)) * int(y - self.mean(b))
                    abs(m)

        else:
            return -1

        result = m / (self.standard_deviation(self, a) * (self.standard_deviation(self, b)))
        result = result / (n - 1)

        return result

    def meanabsdev(self, r):
        s = 0

        for i in range(len(r)):
            d = absolute(r[i] - self.mean(r))
            s += d

        return sum/len(r)