from meta.meta import Resolver, Solution


class DichotomySolution(Solution):
    def as_txt(self) -> str:
        out = [f'Функция вида f(x) = {self._raw["function"].view}']
        for i, (a, b, c, eps) in enumerate(self._raw['steps']):
            out.append(f'Итерация {i + 1}')
            out.append(f'a = {a}')
            out.append(f'b = {b}')
            out.append(f"eps = {eps}")
            out.append(f'c = (a + b) / 2 = ({a} + {b}) / 2 = {c}')
            fc = self._raw["function"](c)
            out.append(f'f(c) = {fc}')
            if fc < 0:
                out.append(f'Знак f(c) равен знаку функции f(x) (-) в точке a. a = {c}')
            elif fc > 0:
                out.append(f'Знак f(c) равен знаку функции f(x) (+) в точке b. b = {c}')
        return '\n'.join(out)


class DichotomySteps(Solution):
    def as_txt(self) -> str:
        out = [f'Пройдёмся по числам на интервале [{self._raw["start"]}; {self._raw["end"]}]',
               f'Функция: {self._raw["function"].view}']
        for x, fx in self._raw['steps']:
            out.append(f'f(x) = f({x}) = {fx}')

        return '\n'.join(out)


class DichotomyResolver(Resolver):
    @staticmethod
    def resolve(f: callable, a: float, b: float, eps: float = 0.000001, n: int = 100) -> DichotomySolution:
        solution = {
            'steps': [],
            'function': f
        }
        while abs(b - a) > eps:
            c = (a + b) / 2
            solution['steps'].append([a, b, c, abs(b - a)])
            if f(c) * f(a) > 0:
                a = c
            else:
                b = c
        solution['steps'].append([a, b, c, abs(b - a)])

        return DichotomySolution(solution)

    @staticmethod
    def steps(f: callable, a: int, b: int, step=2):
        solution = {
            'steps': [],
            'function': f,
            'start': a,
            'end': b
        }

        for i in range(a, b + 1, step):
            solution['steps'].append((i, f(i)))

        return DichotomySteps(solution)
