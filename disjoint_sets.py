
class Node:
    '''
    A simple node class which stores rank and parent, for use in Disjoint Sets.
    By default, the parent is set to itself, unless a new parent is added.
    '''
    def __init__(self, rnk, d):
        self.rank = rnk
        self.parent = self
        self.data = d


class DisjointSet:
    '''
    A disjoint set datastructure, for implementing union find operations.
    '''

    def __init__(self):
        '''
        The members dictionary hashes the value to the corresponding node
        '''
        self.members = dict()

    def make_set(self, val):
        if val not in members:
            # The rank is initially 0 since it is a new set
            members[val] = Node(0, val)

    '''
    Takes input of a given node in the members dictionary.
    Returns the root of its set.
    '''
    def find(self, n):
        if n.parent != n:
            self.members[n.data].parent = find(n.parent)
        return n.parent

    def union(self, n1, n2):
        root_n1 = self.find(n1)
        root_n2 = self.find(n2)

        if root_n1 == root_n2:
            return True
        else:
            if root_n1.rank > root_n2.rank:
                self.members[root_n2.data].parent = root_n1
            elif root_n1.rank < root_n2.rank:
                self.members[root_n1.data].parent = root_n2
            else:
                self.members[root_n2.data].parent = root_n1
                self.members[root_n1.data].rank = root_n1.rank+1
