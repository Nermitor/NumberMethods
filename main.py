from methods.dichotomy import DichotomyResolver
from methods.simple_iterations import SimpleIterationsResolver
from math import sin, pi

from methods.tangent import TangentResolver


def sample_func(x):
    sample_func.view = "x ** 2 - 6 * x - 25"
    sample_func.template = sample_func.view.replace('x', '{0}')
    return eval(sample_func.template.format(x))


def test():
    steps = DichotomyResolver.steps(sample_func, -10, 10).as_txt()
    print(steps)

    resolve = DichotomyResolver.resolve(sample_func, 8, 9, 0.001)
    print(resolve.as_txt())


if __name__ == '__main__':
    test()
