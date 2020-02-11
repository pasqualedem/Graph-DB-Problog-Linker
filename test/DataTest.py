from src.Data import Data


class Test:
    dat = Data((('a', 'valore1'), ('b', 'valore2'), ('b', 'valore3'),('c', 'valore4'), ('c', 'valore4'),('c', 'valore4'),('c', 'valore1') ), 6)
    triple = dat.get_triples()
    print(triple)
    dic = dat.learn_tagging_probabilities()
    print(dic.keys())
    print(dic.values())
    print(dic)

