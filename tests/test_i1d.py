import numpy as np
from i1d import intersect_1d

size = 10_000
iters = 20

a1k = np.random.choice(10_000, size=1_000, replace=False)
a100k = np.random.choice(1_000_000, size=100_000, replace=False)
a1m = np.random.choice(5_000_000, size=1_000_000, replace=False)

b1k = np.random.choice(10_000, size=1_000, replace=False)
b100k = np.random.choice(1_000_000, size=100_000, replace=False)
b1m = np.random.choice(5_000_000, size=1_000_000, replace=False)


def test_same_as_numpy():

    for _ in range(iters):
        a = np.random.choice(size * 10, size=size, replace=False)
        b = np.random.choice(size * 10, size=size, replace=False)

        i1, j1 = intersect_1d(a, b)
        i2, j2 = np.intersect1d(a, b, return_indices=True, assume_unique=True)[1:]

        assert np.all(np.equal(np.sort(i1), np.sort(i2)))
        assert np.all(np.equal(np.sort(j1), np.sort(j2)))


def test_1k_i1d(benchmark):
    benchmark(intersect_1d, a1k, b1k)


def test_1k_i1d_par(benchmark):
    benchmark(intersect_1d, a1k, b1k, parallel=True)


def test_1k_numpy(benchmark):
    benchmark(np.intersect1d, a1k, b1k, return_indices=True, assume_unique=True)


def test_100k_i1d(benchmark):
    benchmark(intersect_1d, a100k, b100k)


def test_100k_i1d_par(benchmark):
    benchmark(intersect_1d, a100k, b100k, parallel=True)


def test_100k_numpy(benchmark):
    benchmark(np.intersect1d, a100k, b100k, return_indices=True, assume_unique=True)


def test_1m_i1d(benchmark):
    benchmark(intersect_1d, a1m, b1m)


def test_1m_i1d_par(benchmark):
    benchmark(intersect_1d, a1m, b1m, parallel=True)


def test_1m_numpy(benchmark):
    benchmark(np.intersect1d, a1m, b1m, return_indices=True, assume_unique=True)
