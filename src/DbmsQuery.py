from src.IGraphDBQuery import IGraphDBQuery

class DbmsQuery(IGraphDBQuery):
    def __init__(self, query):
        self.query = query

    def run_query(self):
        return

    def set_query(self, query):
        self.query = query
