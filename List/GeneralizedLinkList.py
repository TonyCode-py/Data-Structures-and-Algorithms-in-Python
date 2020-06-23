class Node(object):
    """docstring for Node"""
    def __init__(self, category, value, next=None):
        """ category = 'head' or 'ver' or 'hor' or 'data' or 'spd' which respectively means head,
           vertical, horizontal, data and special data. """
        super(Node, self).__init__()
        self.category = category
        self.value = value
        self.next = next


class GeneralizedLinkList(object):
    """docstring for GeneralizedLinkList"""
    def __init__(self):
        super(GeneralizedLinkList, self).__init__()
        self.head = Node('head', '#')

    def display(self):
        self.show(self.head)

    def show(self, start):
        p = start.next
        while p:
            if p.category == 'data':
                print(p.value, end="")
            elif p.category == 'spd':
                print('(', end="")
                self.show(p.value)
                print(')', end="")
            p = p.next

    def get_tail(self):
        p = self.head.next
        q = p
        while p:
            q = p
            p = p.next
        return q

    def add_node(self, a):
        q = self.get_tail()
        q.next = a


def main():
    test_chain = GeneralizedLinkList()

    m = ['ver', 'data', 'data', 'spd', 'hor', 'data', 'data', 'data', 'data', 'data']
    x = [0, '3', '+', 0, 0, '6', '/', '2', '-', '1']

    a1 = Node(m[0], 0)
    a2 = Node(m[1], x[1])
    a3 = Node(m[2], x[2])
    a4 = Node(m[3], 0)
    a5 = Node(m[4], 0)
    a6 = Node(m[5], x[5])
    a7 = Node(m[6], x[6])
    a8 = Node(m[7], x[7])
    a9 = Node(m[8], x[8])
    a10 = Node(m[9], x[9])
    m = Node('data', '=')

    test_chain.head.next = a1

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.value = a5
    a5.next = a6
    a6.next = a7
    a7.next = a8
    a4.next = a9
    a9.next = a10

    test_chain.display()
    print("")

    test_chain.add_node(m)

    test_chain.display()
    print("")


if __name__ == "__main__":
    main()



