from math import floor

## implements recursive binary search for an array list
# @param: arr: the array where to search x
# @param: left: the first index of the array
# @param: right: the last index of the array
# @param: x: the value that as to be searched
# @returns: the index where x has been found, or where it should be inserted to keep ordering
from problog.logic import Constant, Term


def normalize_result(value):
    if type(value) is not str:
        return value

    if value.isnumeric():
        return float(value)

    if ':' in value and '/' in value or '(' in value or ')' in value:
        value = value.replace("/", "_")
        value = value.replace(":", "_")
        value = value.replace("-", "_")
        value = value.replace("(", "_")
        value = value.replace(")", "_")
        value = value.replace(".", "_")
    return value


def binary_search_rec(arr, left, right, x):
    if (right - left) < 1:
        if x <= arr[left]:
            return left
        else:
            return left + 1
    else:
        mid = floor((left + right) / 2)
        if x > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
        return binary_search_rec(arr, left, right, x)


## implements binary search for an array list
# @param: arr: the array where to search x
# @param: x: the value that as to be searched
# @returns: the index where x has been found, or where it should be inserted to keep ordering
def binary_search(arr, x):
    return binary_search_rec(arr, 0, len(arr) - 1, x)


## Finds and appropriated Problog class for a value
# @param: value: the value to be checked
# @returns: an object of type Constant if value is numeric else an object of type Term
def get_type(value):
    if type(value) is float or type(value) is int:
        return Constant(value)
    return Term(value)


##
# Builds a clause from a triple (subj, pred, obj) in prop(subj, pred, obj) format or pred(subj, obj) format
class ClauseBuilder:

    ## ClauseBuilder constructor
    # @param: triple_mode: if true atoms will be prop(subj, pred, obj) else will be pred(subj, obj)
    def __init__(self, triple_mode=True):
        if triple_mode:
            self.__prop = Term('prop')
            self.get_clause = self.get_prop_clause
        else:
            self.get_clause = self.get_pred_clause

    ## builds a clause in pred(subj, obj) format
    # @param: subj: the subject of the predicate
    # @param: obj: the object of the predicate
    # @param: prob: the probability of the clause
    def get_pred_clause(self, subj, pred, obj=None, prob=None):
        if type(pred) is not Term:
            if type(pred) is Constant:
                pred = Term(pred.functor())
            else:
                raise Exception
        if obj is None:
            return pred(subj)
        return pred(subj, obj, p=prob)

    ## builds a clause in prop(subj, pred, obj) format
    # @param: subj: the subject of the predicate
    # @param: pred: the predicate
    # @param: obj: the object of the predicate
    # @param: prob: the probability of the clause
    def get_prop_clause(self, subj, pred, obj=None, prob=None):
        if obj is None:
            return self.__prop(subj, pred, p=prob)
        return self.__prop(subj, pred, obj, p=prob)
