"""
Source Author: John Silver
Source: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
Edited By: Mateo Bohorquez - Nickname: Milor123

Credits http://www.amazon.com/Problem-Solving-Algorithms-Structures-Python/dp/1590280539
Problem Solving with Algorithms and Data Structures Using Python
In addition to Code Fellows I learned a lot about linked lists from this book. It's very good and the above code was heavily inspired by their implementations.
"""


class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node  = prev_node
        self.index = None
        self.len = 0

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev_node

    def get_next(self):
        return self.next_node

    def get_index(self):
        return self.index

    def set_prev(self, prev):
        self.prev_node = prev

    def set_next(self, new_next):
        self.next_node = new_next

    def __len__(self):
        return self.len


class LinkedList(object):

        def __init__(self, head=None):
            self.head = head
            self.len = 0
            self.pulse = False

        def __str__(self):
            data = []
            node = self.head
            while node is not None:
                data.append(node.get_data())
                node = node.get_next()
            data = list(reversed(data))
            self.iterable = data
            data = ','.join(map(str, data))
            return '[{0}]'.format(data)

        def __getitem__(self, key):
            from itertools import islice
            self.__str__()
            if isinstance(key, int) and key >= 0:
                return list(islice(self.iterable, key, key + 1))
            elif isinstance(key, slice):
                if key.start>=(0 or None) and key.stop>=(0 or None):
                    return list(islice(self.iterable, key.start, key.stop, key.step))
                else:
                    # TODO make indexing object with negatives [:-1]
                    pass
            elif isinstance(key, int) and key < 0:
                key += 1
                key *= -1
                return list(islice(reversed(self.iterable), key, key + 1))
            else:
                raise KeyError("Key must be non-negative integer or slice, not {}"
                            .format(key))
        def append(self, data):
            new_node = Node(data)
            new_node.set_next(self.head)
            if self.head is None:
                self.tail = new_node
            else:
                new_node.set_prev(self.tail)
                self.tail = new_node
            if not self.pulse: # if not delete nodes
                new_node.index = self.len
                new_node.len = self.len + 1
                self.len += 1
            else: # if delete nodes before enter to this
                self.pulse = False
            self.head = new_node

        def insert(self,index, tobenode):
            new_node = Node(tobenode)
            from copy import deepcopy
            tmpcurrent = deepcopy(self.head)
            current = self.head
            previous = None
            found = False
            newvalue = None
            exist = False
            data = str
            # search in with tmp header and verify if exist
            while tmpcurrent and not exist:
                if tmpcurrent.get_index() == index:
                    exist = True
                    # obtain data for the next search because cant search by
                    # index because the index is reducing (in the next cycle)
                    data = tmpcurrent.get_data()
                else:
                    tmpcurrent = tmpcurrent.get_next()
            # end search
            # if exist this should changes index values for -1
            if exist:
                while current and found is False:
            # end rest
            # search and delete value
                    if current.get_data() == data:
                        #TODO Change data by index
                        found = True
                        self.head.len += 1
                        #self.pulse = True
                        current = current.get_next()
                        new_node.index = self.len
                        new_node.len =  current.index+1
                        new_node.set_next(current.get_next())
                        current.set_next(new_node)
                    else:
                        previous = current
                        current = current.get_next()
                if current is None:
                    raise ValueError("Data not in list")
                if previous is None:
                    #self.remakeindex(self.head, -1, newvalue)
                    self.head = current.get_next()
            # end search and delete
            self.reindex(self.head)

        def size(self):
            current = self.head
            count = 0
            while current:
                count += 1
                current = current.get_next()
            return count

        def search(self, data):
            current = self.head
            found = False
            while current and found is False:
                if current.get_data() == data:
                    found = True
                else:
                    current = current.get_next()
            if current is None:
                raise ValueError("Data not in list")
            return current

        def modify(self, data, newdata):
            current = self.head
            found = False
            while current and found is False:
                if current.get_data() == data:
                    found = True
                    current.data = newdata
                else:
                    current = current.get_next()
            if current is None:
                raise ValueError("Data not in list")
            return current

        def multiple_modify_condition(self, condition, newdata): # 'data1,data2,data3', 'replace1,replace2,replace3'
            current = self.head
            found = False
            import re
            exp = re.compile(r'>=|<=|>|<|==|')
            result = exp.search(condition)
            if result.group() is '':
                print ('Error: the "{}" is not a condition, you must add >= or = or <= or = at the beginning of the variable '.format(condition))
                exit()

            while current is not None:
                if eval(str(current.get_data()) + condition):
                    current.data = newdata
                current = current.get_next()


        def multiple_modify(self, data, newdata): # 'data1,data2,data3', 'replace1,replace2,replace3'
            current = self.head
            found = False
            data = data.split(',')
            data = map(int, data)
            newdata = newdata.split(',')
            newdata = map(int, newdata)

            while current is not None:
                for key, x in enumerate(data):
                    if current.get_data() == x:
                        current.data = newdata[key]
                current = current.get_next()


        def delete(self, data):
            from copy import deepcopy
            tmpcurrent = deepcopy(self.head)
            current = self.head
            previous = None
            found = False
            newvalue = None
            exist = False
            # search in with tmp header and verify if exist
            while tmpcurrent and not exist:
                if tmpcurrent.get_data() == data:
                    exist = True
                else:
                    tmpcurrent = tmpcurrent.get_next()
            # end search
            # if exist this should changes index values for -1
            if exist:
                while current and found is False:
                    current.index += -1
            # end rest
            # search and delete value
                    if current.get_data() == data:
                        found = True
                        self.pulse = True
                        self.head.len += -1
                    else:
                        previous = current
                        current = current.get_next()
                if current is None:
                    raise ValueError("Data not in list")
                if previous is None:
                    #self.remakeindex(self.head, -1, newvalue)
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            # end search and delete
        def remove(self, index):
            from copy import deepcopy
            tmpcurrent = deepcopy(self.head)
            current = self.head
            previous = None
            found = False
            newvalue = None
            exist = False
            data = str
            # search in with tmp header and verify if exist
            while tmpcurrent and not exist:
                if tmpcurrent.get_index() == index:
                    exist = True
                    # obtain data for the next search because cant search by
                    # index because the index is reducing (in the next cycle)
                    data = tmpcurrent.get_data()
                else:
                    tmpcurrent = tmpcurrent.get_next()
            # end search
            # if exist this should changes index values for -1
            if exist:
                while current and found is False:
                    current.index += -1
            # end rest
            # search and delete value
                    if current.get_data() == data:
                        found = True
                        self.head.len += -1
                        self.pulse = True

                    else:
                        previous = current
                        current = current.get_next()
                if current is None:
                    raise ValueError("Data not in list")
                if previous is None:
                    #self.remakeindex(self.head, -1, newvalue)
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            # end search and delete

        def remove_condition(self, condition): # codition must be str with condition '>=strtext'
            from copy import deepcopy
            tmpcurrent = deepcopy(self.head)
            current = self.head
            previous = None
            found = False
            newvalue = None
            exist = False
            data = str
            #################################3
            import re
            exp = re.compile(r'>=|<=|>|<|==|')
            result = exp.search(condition)
            if result.group() is '':
                print ('Error: the "{}" is not a condition, you must add >= or = or <= or = at the beginning of the variable '.format(condition))
                exit()
            # search in with tmp header and verify if exist
            while tmpcurrent and not exist:
                if eval(str(tmpcurrent.get_data()) + condition):
                    exist = True
                    # obtain data for the next search because cant search by
                    # index because the index is reducing (in the next cycle)
                else:
                    tmpcurrent = tmpcurrent.get_next()
            if exist:
                tmpstop = False
                putdata = False
                while current != None:
                    if eval(str(current.get_data()) + condition):
                        current.get_next().index += -1
                        self.head.len += -1 # for index
                        self.pulse = True
                        tmpstop = True
                    if not tmpstop:
                        putdata = True
                        previous = (current)
                        current = current.get_next()
                    if current is None:
                        break
                    if previous is None and tmpstop:
                        #self.remakeindex(self.head, -1, newvalue)
                        self.head = current.get_next()
                        if not putdata: # this is the fucking trick SSSOMG T_T
                            current = current.get_next()
                        tmpstop = False
                    elif previous is not None and tmpstop:
                        previous.set_next(current.get_next())
                        current = previous
                        tmpstop = False
                        if not putdata:
                            previous = (current)
                            current = current.get_next()
                    putdata = False
            self.reindex(self.head)

        def get_myindex(self, node, data):
            copy = node
            while copy is not None:
                if copy.get_data() == data:
                    return copy.index
                else:
                    copy = copy.get_next()
            # TODO: add raises

        def reprev(self, headnode):
            copy = headnode
            while copy is not None:
                copy.set_prev= copy
                copy = copy.get_next()

        def reindex(self, headnode):

            # re order index when is delted
            copy = headnode
            #print len(headnode)
            #print '================'
            for x in reversed(range(len(self.head))):
                #print x, copy.get_data()
                copy.index = int(x)
                copy = copy.get_next()
            #print '==============='
            # end re order

        def show(self, reverse=False, sorter=False):
            head = (self.head)
            while head:
                if reverse is False and sorter is False:
                    print head.index, head.get_data()
                if head.get_next() is None:
                    break
                head = head.get_next()
            if reverse:
                # TODO: fix prev bug in delete methods
                inverse = self[:]
                for index,x in enumerate(inverse):
                    print index, x
#                 while not head.index == len(head)-1 and head:
                    # print head.index, head.get_data()
                    # if head.get_prev() is None:
                        # break
                    # head = head.get_prev()
            if sorter:
                datatuple = zip(self[:],range(len(self[:])))# (value, index_key)
                sortitem = sorted(datatuple, key=lambda x: x[0]) # sort by [0] = value
                for x in (sortitem):
                    print x[1], x[0]


if __name__ == "__main__":
    lista = LinkedList()
    lista.append(23)
    lista.append(50)
    lista.append(1)
    lista.append(-2)
    lista.append(3)
    lista.append(-9)
    lista.append(0)
    lista.append(5)
    lista.append(-1)
    lista.append(777)
    lista.append(99)
    lista.remove(0) # by index, the 0 is the number 23
    lista.delete(50) # by data
    lista.remove_condition('<1') # by condition
    lista.multiple_modify('5,3','999,999') # search 5 and 3, then replace by 999, 999 according to case
    lista.multiple_modify_condition('==999',111) # replaces all equivalent numbers to 999, by 111
    lista.insert(1,'4444')
    lista.show()
    print '=========Invertido============='
    lista.show(reverse=True)
    print '=========Ordenado============='
    lista.show(reverse=False, sorter=True)
    print '**********'
    print lista, 'all data order by index'
    print lista[0], 'index 0'
    print lista[-1], 'reversing, ultimate value of index'
    print lista[0:3],'values in range 0 , 3' # warning no supports negative index in multiple slices
