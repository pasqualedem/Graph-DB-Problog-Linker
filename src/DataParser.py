from problog.program import SimpleProgram
from problog.logic import Constant, Var, Term, AnnotatedDisjunction


class DataParser:
    """
    Takes a list of triples or quadreples and generates a SimpleProgram object
    For every tuple:
    First: Subject
    Second: Predicate
    Third: Object
    Fourth: Prabability (Optional)
    """

    def __init__(self, query_data=None):
        self.__data = query_data  # List of triples/quadruples
        self.__program = None

    def set_data(self, query_data):
        self.__data = query_data

    def parse(self):
        """Parse a list of triples/quadruples into a SimpleProgram"""
        self.__program = SimpleProgram()
        term_dict = dict()
        const_dict = dict()
        for triple in self.__data:
            if term_dict.get(triple[1]) is None:
                term_dict[triple[1]] = Term(triple[1])
            if const_dict.get(triple[0]) is None:
                const_dict[triple[0]] = Constant(triple[0])
            if const_dict.get(triple[2]) is None:
                const_dict[triple[2]] = Constant(triple[2])
            pred = term_dict.get(triple[1])
            c1 = const_dict[triple[0]]
            c2 = const_dict[triple[2]]
            if len(triple) == 4:
                p = triple[3]
                self.__program += pred(c1, c2, p=p)
            else:
                self.__program += pred(c1, c2)

    def get_program(self):
        return self.__program
