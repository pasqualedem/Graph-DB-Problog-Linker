import unittest

from problog.program import SimpleProgram, PrologString

from data import Data, PropertyMap, Property
from problog import get_evaluatable
from problog.logic import Term, Var, Constant

from Distribution import Multinomial, Discrete


class DataTest(unittest.TestCase):

    def test_to_examples(self):
        data_triples = [
            [('donato', 'smokes', True), ('giovanni', 'smokes', True), ('floriana', 'smokes', False)],
            [('donato', 'smokes', False), ('giovanni', 'smokes', True), ('floriana', 'smokes', True)],
            [('donato', 'smokes', True), ('giovanni', 'smokes', False), ('floriana', 'smokes', True)],
            [('donato', 'smokes', False), ('giovanni', 'smokes', True), ('floriana', 'smokes', True)],
        ]
        data = Data(data_triples, 12, True)
        examples = data.to_examples()
        print(examples)

    def test_parse(self):
        l = list()
        l.append([('marco', 'papa', 'giovanni')])
        l.append([('gianna', 'mamma', 'giovanni')])
        qp = Data(l, 6, True)
        pr = qp.parse()
        query = Term('query')
        x = Var('X')
        marco = Term('marco')
        gianna = Term('gianna')
        papa = Term('papa')
        prop = Term('prop')
        mamma = Term('mamma')
        pr += query(prop(gianna, mamma, x))
        pr += query(prop(marco, papa, x))
        r = get_evaluatable().create_from(pr).evaluate()
        print(r)


class PropertyTest(unittest.TestCase):

    def test_distributions(self):
        dat = Data([[('c', 'a', 'valore1'), ('c', 'b', 'valore2'), ('c', 'b', 'valore3')],
                    [('c', 'c', 'valore4'), ('c', 'c', 'valore4'),
                     ('c', 'c', 'valore4'), ('c', 'c', 'valore1')]], 6, True)
        triple = dat.get_data()
        print(triple)
        dic = dat.learn_distributions()
        print(dic.keys())
        print(dic.values())
        print(dic)

    def test_to_program(self):
        data = Data(
            [[(0, 'OWNS', 55), (0, 'brand', 'Ford'), (0, 'targa', '123'), (55, 'name', 'Luigi'), (55, 'age', 11)],
             [(1, 'OWNS', 17), (1, 'brand', 'Seat'), (1, 'targa', '124'), (17, 'name', 'Sergio'), (17, 'age', 18)],
             [(15, 'OWNS', 19), (15, 'name', 'Giuseppe'), (15, 'age', 19), (19, 'brand', 'Suzuki'),
              (19, 'targa', '143')],
             [(15, 'KNOWS', 55), (15, 'name', 'Giuseppe'), (15, 'age', 19), (55, 'name', 'Luigi'), (55, 'age', 11)],
             [(15, 'KNOWS', 17), (15, 'name', 'Giuseppe'), (15, 'age', 19), (17, 'name', 'Sergio'), (17, 'age', 18)],
             [(15, 'KNOWS', 16), (15, 'name', 'Giuseppe'), (15, 'age', 19), (16, 'name', 'Pasquale'), (16, 'age', 17)],
             [(16, 'OWNS', 21), (16, 'name', 'Pasquale'), (16, 'age', 17), (21, 'brand', 'Audi'), (21, 'targa', '127')],
             [(16, 'KNOWS', 15), (16, 'name', 'Pasquale'), (16, 'age', 17), (15, 'name', 'Giuseppe'), (15, 'age', 19)],
             [(16, 'KNOWS', 17), (16, 'name', 'Pasquale'), (16, 'age', 17), (17, 'name', 'Sergio'), (17, 'age', 18)],
             [(17, 'OWNS', 1), (17, 'name', 'Sergio'), (17, 'age', 18), (1, 'brand', 'Seat'), (1, 'targa', '124')],
             [(17, 'KNOWS', 15), (17, 'name', 'Sergio'), (17, 'age', 18), (15, 'name', 'Giuseppe'), (15, 'age', 19)],
             [(17, 'KNOWS', 16), (17, 'name', 'Sergio'), (17, 'age', 18), (16, 'name', 'Pasquale'), (16, 'age', 17)],
             [(18, 'KNOWS', 55), (18, 'name', 'Roberto'), (18, 'age', 15), (55, 'name', 'Luigi'), (55, 'age', 11)],
             [(19, 'OWNS', 15), (19, 'brand', 'Suzuki'), (19, 'targa', '143'), (15, 'name', 'Giuseppe'),
              (15, 'age', 19)],
             [(20, 'brand', 'Fiat'), (20, 'targa', '125')],
             [(21, 'OWNS', 16), (21, 'brand', 'Audi'), (21, 'targa', '127'), (16, 'name', 'Pasquale'), (16, 'age', 17)],
             [(55, 'OWNS', 0), (55, 'name', 'Luigi'), (55, 'age', 11), (0, 'brand', 'Ford'), (0, 'targa', '123')],
             [(55, 'KNOWS', 15), (55, 'name', 'Luigi'), (55, 'age', 11), (15, 'name', 'Giuseppe'), (15, 'age', 19)],
             [(55, 'KNOWS', 18), (55, 'name', 'Luigi'), (55, 'age', 11), (18, 'name', 'Roberto'), (18, 'age', 15)],
             [(56, 'KNOWS', 57), (56, 'name', 'Matteo'), (57, 'name', 'Francesco')],
             [(57, 'KNOWS', 56), (57, 'name', 'Francesco'), (56, 'name', 'Matteo')]], 21, True)

        property_map = PropertyMap()
        property_map["brand"] = Property("brand", Multinomial(), "car")

        property_map = data.learn_distributions(property_map)
        s = property_map.to_simple_program(triple_mode=True)
        s += list(PrologString("query(prop(car, brand, X)).").__iter__())[0]
        r = get_evaluatable().create_from(s).evaluate()
        print(r)

    def test_basic_query(self):
        data = Data(
            [[(0, 'brand', 'Ford')],
             [(1, 'brand', 'Seat')],
             [(19, 'brand', 'Suzuki')],
             [(21, 'brand', 'Audi')],
             [(1, 'brand', 'Seat')],
             [(19, 'brand', 'Suzuki')],
             [(20, 'brand', 'Fiat')],
             [(21, 'brand', 'Audi')],
             [(0, 'brand', 'Ford')]
             ], 9, True)

        property_map = PropertyMap()
        property_map["brand"] = Property("brand", Multinomial())

        property_map = data.learn_distributions(property_map)
        s = property_map.to_simple_program(triple_mode=True)
        s += list(PrologString("query(prop(_generic_individual_, brand, X)).").__iter__())[0]

        r = get_evaluatable().create_from(s).evaluate()
        print(r)

    def test_inference_pred_format(self):
        data = Data(
            [[('donato', 'father', 'annalisa')],
             [('michelangelo', 'father', 'corrado')],
             [('annalisa', 'mother', 'corrado')]
             ], 9, triple_mode=False)

        s = data.parse()

        s += list(PrologString("child(A,B) :- father(B,A).").__iter__())[0]
        s += list(PrologString("child(A,B) :- mother(B,A).").__iter__())[0]
        s += list(PrologString("query(child(A,annalisa)).").__iter__())[0]

        r = get_evaluatable().create_from(s).evaluate()
        print(r)


if __name__ == '__main__':
    unittest.main()
