import math
from statistics import mean


def pearson(first, second):
    if len(first) != len(second) or len(first) < 2:
        raise ValueError("Expected equally sized samples with at least two values")
    n = len(first)
    first_mean = mean(first)
    second_mean = mean(second)
    covariance = 0
    first_variance = 0
    second_variance = 0
    for i in range(n):
        first_difference = first[i] - first_mean
        second_difference = second[i] - second_mean
        covariance += first_difference * second_difference
        first_variance += first_difference * first_difference
        second_variance += second_difference * second_difference
    first_deviation = math.sqrt(first_variance)
    second_deviation = math.sqrt(second_variance)
    denominator = first_deviation * second_deviation
    if denominator == 0:
        raise ValueError("Correlation is undefined for a constant sample")
    return covariance / denominator


def main():
    count = int(input())
    pairs = [tuple(map(float, input().split())) for _ in range(count)]
    if any(len(pair) != 2 for pair in pairs):
        raise ValueError("Expected two numbers per row")
    first_sample = [pair[0] for pair in pairs]
    second_sample = [pair[1] for pair in pairs]
    print(f"{pearson(first_sample, second_sample):.2f}")


if __name__ == "__main__":
    main()
