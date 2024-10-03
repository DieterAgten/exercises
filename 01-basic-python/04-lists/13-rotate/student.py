def rotate(xs, n):
    xs1 = xs[n:]
    xs2 = xs[:n]
    return [*xs1, *xs2]