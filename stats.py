from typing import List
import math
from collections import Counter
from linear_algebra import sum_of_squares, subtract, dot

def mean(ds: List[float]) -> float:
    return sum(ds) / len(ds)

def _get_midpoint(ds: List[float]) -> int:
    return math.floor((len(ds) - 1) / 2)

def _median_odd(ds: List[float]) -> float:
    return sorted(ds)[_get_midpoint(ds)]

def _median_even(ds: List[float]) -> float:
    mid = _get_midpoint(ds)
    return mean(sorted(ds)[mid:mid + 2]) # add two b/c slice ends are exclusive

def median(ds: List[float]):
    return _median_even(ds) if len(ds) % 2 == 0 else _median_odd(ds)

def quantile(ds: List[float], p: float) -> float:
    if (p > 1) or (p < 0):
        raise ValueError('p must be in the range [0,1]')
    endpoint = math.ceil(len(ds) * p)
    return sorted(ds)[endpoint]

def mode(ds: List[float]) -> List[float]:
    counts = Counter(ds)
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]

def data_range(ds: List[float]) -> float:
    return max(ds) - min(ds)

def mean_diff(ds: List[float]) -> List[float]:
    avg = mean(ds)
    return [el - avg for el in ds]

def variance(ds: List[float]) -> float:
    if len(ds) < 2:
        raise ValueError("Dataset must have two or more elements")
    diff_vector = mean_diff(ds)
    return sum_of_squares(diff_vector) / (len(ds) - 1)

def standard_deviation(ds: List[float]) -> float:
    return math.sqrt(variance(ds))

def interquartile_range(ds: List[float]) -> float:
    return quantile(ds, 0.75) - quantile(ds, 0.25)
    
def covariance(ds1: List[float], ds2: List[float]) -> float:
    if len(ds1) != len(ds2):
        raise ValueError("Datasets must be same length")
    return dot(mean_diff(ds1), mean_diff(ds2)) / len(ds1) - 1
    

def correlation(ds1: List[float], ds2: List[float]) -> float: 
    sd1 = standard_deviation(ds1)
    sd2 = standard_deviation(ds2)
    if sd1 <= 0 or sd2 <= 0:
        return 0
    cov = covariance(ds1, ds2)
    return cov / (sd1 * sd2)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2
