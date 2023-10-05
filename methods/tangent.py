from meta.meta import Resolver, Solution


class TangentSolution(Solution):
    def as_txt(self) -> str:
        out = [f'Функция вида f(x) = {self._raw["function"].view}']
        for i, (x0, x1, fx0, fx1, x2, e) in enumerate(self._raw['steps']):
            out.append(f'Итерация {i + 1}')
            out.append(f'x{i} = {x0}')
            out.append(f'x{i + 1} = {x1}')
            out.append(f'x{i + 2} = {self._raw["function"].template.format(x0)} = {x1}')
            out.append(f'e = {e}')
        return '\n'.join(out)


class TangentResolver(Resolver):
    @staticmethod
    def resolve(f: callable, x0: float, x1: float, eps: float = 0.000001, n: int = 100) -> TangentSolution:
        solution = {
            'steps': [],
            'function': f
        }
        stop = False
        while not stop and n > 0:
            x2 = x0 - f(x0) * (x1 - x0) / (f(x1) - f(x0))
            solution['steps'].append([x0, x1, f(x1), f(x1), x2, abs(x1 - x2)])
            if abs(x2 - x1) < eps:
                stop = True
            x0 = x1
            x1 = x2
            n -= 1

        return TangentSolution(solution)
