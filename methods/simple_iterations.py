from meta.meta import Resolver, Solution


class SimpleIterationsSolution(Solution):
    def as_txt(self) -> str:
        out = [f'Функция вида f(x) = {self._raw["function"].view}']
        for i, (x0, x1, eps) in enumerate(self._raw['steps']):
            out.append(f'Итерация {i + 1}')
            out.append(f'x{i} = {x0}')
            out.append(f'x{i + 1} = {self._raw["function"].template.format(x0)} = {x1}')
        return '\n'.join(out)


class SimpleIterationsResolver(Resolver):
    @staticmethod
    def resolve(f: callable, x0: float, eps: float = 0.000001, n: int = 100) -> SimpleIterationsSolution:
        solution = {
            'steps': [],
            'function': f
        }
        stop = False
        while not stop and n > 0:
            x1 = f(x0)
            solution['steps'].append([x0, x1, abs(x0 - x1)])
            if abs(x1 - x0) < eps:
                stop = True
            x0 = x1
            n -= 1

        return SimpleIterationsSolution(solution)
