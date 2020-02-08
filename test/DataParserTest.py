import unittest

from problog import get_evaluatable
from problog.logic import Term, Var, Constant

from DataParser import DataParser


class MyTestCase(unittest.TestCase):
    def test_parse(self):
        l = list()
        l.append(('marco', 'papa', 'giovanni'))
        l.append(('gianna', 'mamma', 'giovanni'))
        qp = DataParser(l)
        qp.parse()
        pr = qp.get_program()
        query = Term('query')
        x = Var('X')
        y = Var('Y')
        marco = Constant('marco')
        gianna = Constant('gianna')
        papa = Term('papa')
        mamma = Term('mamma')
        pr += query(papa(marco, x))
        #pr += query(mamma(gianna, y))
        r = get_evaluatable().create_from(pr).evaluate()
        print(r)
        assert True

    def test_parse_tagged(self):
        l = list()
        l.append(('marco', 'papa', 'giovanni', 0.7))
        l.append(('gianna', 'mamma', 'giovanni'))
        qp = DataParser(l)
        qp.parse()
        pr = qp.get_program()
        query = Term('query')
        x = Var('X')
        y = Var('Y')
        marco = Constant('marco')
        gianna = Constant('gianna')
        papa = Term('papa')
        mamma = Term('mamma')
        pr += query(papa(marco, x))
        #pr += query(mamma(gianna, y))
        r = get_evaluatable().create_from(pr).evaluate()
        print(r)
        print(*pr)
        assert True

    def test_pars_capital(self):
        l = list()
        l.append(('Marco', 'papa', 'Giovanni'))
        l.append(('Gianna', 'mamma', 'Giovanni'))
        qp = DataParser(l)
        qp.parse()
        pr = qp.get_program()
        query = Term('query')
        x = Var('X')
        y = Var('Y')
        marco = Constant('Marco')
        gianna = Constant('Gianna')
        papa = Term('papa')
        mamma = Term('mamma')
        pr += query(papa(marco, x))
        #pr += query(mamma(gianna, y))
        r = get_evaluatable().create_from(pr).evaluate()
        print(r)
        assert True


if __name__ == '__main__':
    unittest.main()
