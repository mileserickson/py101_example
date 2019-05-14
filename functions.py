import scipy.stats

def f(x):
    return x+1


def can_haz_data(n):
    dist = scipy.stats.norm()
    return dist.rvs(size=n)