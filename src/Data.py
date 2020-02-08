class Data:
    def __init__(self, triples, length):
        self.__triples = triples
        self.__length = length

    def set_triples(self, triples):
        self.__triples = triples

    def get_triples(self):
        return self.__triples