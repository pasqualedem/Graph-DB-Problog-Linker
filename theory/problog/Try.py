from problog.program import SimpleProgram, PrologString, LogicProgram, PrologFile
from problog.logic import Constant, Var, Term, AnnotatedDisjunction
from problog import get_evaluatable

true = Term('true')
ok = Term('ok')
query = Term('query')

p = PrologFile("Try.pl")
x = [p]
for i in range(0, 2):
    s = SimpleProgram()
    brand = Term('brand')
    ind = Term('ind')
    prop = Term('prop')
    query = Term('query')
    X = Var('X')
    ford = Term('ford')
    seat = Term('seat')
    suzuki = Term('suzuki')
    audi = Term('audi')
    fiat = Term('fiat')
    s = SimpleProgram()
    s += AnnotatedDisjunction([prop(ind, brand, ford, p=0.222222222222222), prop(ind, brand, seat, p=0.222222222222222),
                               prop(ind, brand, suzuki, p=0.222222222222222),
                               prop(ind, brand, audi, p=0.222222222222222),
                               prop(ind, brand, fiat, p=0.111111111111111)], true)
    if i == 1:
        q = PrologFile("TryQuery.pl")
        for clause in q:
            s += clause
    else:
        s += query(prop(ind, brand, X))
    x.append(s)

r = get_evaluatable().create_from(x[0]).evaluate()
print(r)
r = get_evaluatable().create_from(x[1]).evaluate()
print(r)
r = get_evaluatable().create_from(x[2]).evaluate()
print(r)

a1 = list(x[0].__iter__())[0]
a2 = list(x[1].__iter__())[0]
a3 = list(x[2].__iter__())[0]

q1 = list(x[0].__iter__())[1]
q2 = list(x[1].__iter__())[1]
q3 = list(x[2].__iter__())[1]

n = SimpleProgram()

for clause in x[0]:
    n += clause

r = get_evaluatable().create_from(x[2]).evaluate()
print(r)