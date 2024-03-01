import random
# Şerif Burak Kalkan - 210315023
def weighted_srs(data, n, weights, with_replacement):
    if not with_replacement:
        raise ValueError("Weighted simple random sampling without replacement is not supported.")
    sample = []
    for _ in range(n):
        choice = random.choices(data, weights=weights)[0]
        sample.append(choice)
    return sample
