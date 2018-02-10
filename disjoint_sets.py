
class Node:
    '''
    A simple node class which stores rank and parent, for use in Disjoint Sets.
    By default, the parent is set to itself, unless a new parent is added.
    '''
    def __init__(self, rnk, par, ind):
        self.rank = rnk
        self.index = ind
        self.parent = self

class DisjointSet:
    '''
    A disjoint set datastructure, for implementing union find operations.
    '''

    def __init__(self):
        self.members = []

    def make_set(self, val):
        n = Node(0, len(self.members))
        members.append(n)

    def find(self):
        #

    def union(self):
        #
