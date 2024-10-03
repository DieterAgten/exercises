def drop_nth(xs, n):
    xs1 = xs[:n]
    xs2 = xs[n+1:]
    return [*xs1,*xs2]