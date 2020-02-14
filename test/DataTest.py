import unittest
from Data import Data
from problog import get_evaluatable
from problog.logic import Term, Var, Constant


class MyTestCase(unittest.TestCase):

    def test_to_examples(self):
        data_triples = [
            [('donato', 'smokes', True), ('giovanni', 'smokes', True), ('floriana', 'smokes', False)],
            [('donato', 'smokes', False), ('giovanni', 'smokes', True), ('floriana', 'smokes', True)],
            [('donato', 'smokes', True), ('giovanni', 'smokes', False), ('floriana', 'smokes', True)],
            [('donato', 'smokes', False), ('giovanni', 'smokes', True), ('floriana', 'smokes', True)],
        ]
        data = Data(data_triples, 12)
        examples = data.to_examples()
        print(examples)
        self.assertTrue(True)

    def test_parse(self):
        l = list()
        l.append([('marco', 'papa', 'giovanni')])
        l.append([('gianna', 'mamma', 'giovanni')])
        qp = Data(l, 6)
        pr = qp.parse()
        query = Term('query')
        x = Var('X')
        marco = Constant('marco')
        gianna = Constant('gianna')
        papa = Constant('papa')
        prop = Term('prop')
        mamma = Constant('mamma')
        pr += query(prop(gianna, mamma, x))
        pr += query(prop(marco, papa, x))
        r = get_evaluatable().create_from(pr).evaluate()
        print(r)
        assert True

    def test_distributions(self):
        dat = Data([[('c', 'a', 'valore1'), ('c', 'b', 'valore2'), ('c', 'b', 'valore3')], [('c', 'c', 'valore4'), ('c', 'c', 'valore4'),
                    ('c', 'c', 'valore4'), ('c', 'c', 'valore1')]], 6)
        triple = dat.get_data()
        print(triple)
        dic = dat.learn_distributions()
        print(dic.keys())
        print(dic.values())
        print(dic)

if __name__ == '__main__':
    unittest.main()
