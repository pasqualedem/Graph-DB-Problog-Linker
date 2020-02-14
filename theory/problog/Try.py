from problog.program import SimpleProgram
from problog.logic import Constant,Var,Term,AnnotatedDisjunction
from problog import get_evaluatable

prop, query = Term('prop'), Term('query')
X = Var('X')
p = SimpleProgram()
marco = Constant('marco')
papa = Constant('papa')
giovanni = Constant('giovanni')
p += prop(marco, papa, giovanni)
p += prop(Constant('maria'),Constant('mamma'), Constant('giovanni'))
p += query(prop(Constant('maria'), Constant('mamma'), X))

r = get_evaluatable().create_from(p).evaluate()
print(r)

model = """
prop(marco, papa, giovanni).
prop(maria, mamma, giovanni).

query(prop(marco,papa,X)).
"""

r = get_evaluatable().create_from(model).evaluate()
print(r)