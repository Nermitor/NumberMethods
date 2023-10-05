from math import sin, pi

from simple_iterations import SimpleIterationsResolver


def sample_func(x):
    sample_func.view = "2 * sin(x + pi / 6) ** 2 - 1"
    sample_func.template = sample_func.view.replace('x', '{0}')
    return eval(sample_func.template.format(x))


def test():
    resolve = SimpleIterationsResolver.resolve(sample_func, 1)
    print(resolve.as_txt())


if __name__ == '__main__':
    test()
