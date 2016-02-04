class Man:

    def __init__(self, r, n, m, f, l):
        self._number = r
        self._name = n
        self._match = m
        self._free = f
        self._list = l
        self.count = []

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, n):
        self._number = n

    @number.deleter
    def number(self):
        del self._number
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, n):
        self._name = n

    @name.deleter
    def name(self):
        del self._name

    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, m):
        self._match = m

    @match.deleter
    def match(self):
        del self._match

    @property
    def free(self):
        return self._free

    @free.setter
    def free(self, f):
        self._free = f

    @free.deleter
    def free(self):
        del self._free

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, l):
        self._list = l

    @list.deleter
    def list(self):
        del self._list

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, a):
        self._count = a

    @count.deleter
    def count(self):
        del self._count

    def match_print(self):
        print(self.name, self.match)
    
    def add_count(self, name):
        self.count.append(name)
        print('{this} Proposal Attempts: {attempts}'.format(this = self.name, w = name, attempts = self.count))

    def choose_highest_unproposed(self):
        for woman in self.list:
            if woman not in self.count:
                return woman
        else:
            print('{man} has proposed to every woman'.format(man = self.name))
            return None
        
    def print_list(self):
        for name in self.list:
            print(name, end=' ')
        print()

class Woman:

    def __init__(self, r, n, m, f, l):
        self._number = r
        self._name = n
        self._match = m
        self._free = f
        self._list = l
        self.count = []

    @property
    def number(self):
        return self._number

    @number.setter
    def name(self, n):
        self._number = n

    @number.deleter
    def name(self):
        del self._number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @name.deleter
    def name(self):
        del self._name

    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, m):
        self._match = m

    @match.deleter
    def match(self):
        del self._match

    @property
    def free(self):
        return self._free

    @free.setter
    def free(self, f):
        self._free = f

    @free.deleter
    def free(self):
        del self._free
    
    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, m):
        self._match = m

    @match.deleter
    def match(self):
        del self._match

    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, l):
        self._list = l

    @list.deleter
    def list(self):
        del self._list
    
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, d):
        self._count = d

    @count.deleter
    def count(self):
        del self._count

    def add_count(self, m):
        self.count.append(m)

    def print_list(self):
        for name in self.list:
            print(name, end=' ')
        print()
        
    def print_favorite_man(self):
        print(self.m_list[0])
        
    def choose_highest_unproposed(self):
        for man in self.list:
            if man not in self.count:
                return man
        else:
            print('{woman} has proposed to every man'.format(woman = self.name))
            return None
    def match_print(self):
        print(self.name, self.match)
    
def free_man_exists(men, women):
    for m in men:
        if m.free == True:
            if more_possible_proposals(m, women):
                return (True, m)
    else:
        print('No Free men')
        return False

def more_possible_proposals(m, women):
    if len(m.count) != len(women):
        return True
    else:
        return False

def choose_man(men):
    for m in men:
        if m.free == True:
            return m
    
def engagement(m, w):
    w.free = False
    m.free = False
    m.add_count(w.name)
    w.add_count(m.name)
    m.match = w.name
    w.match = m.name
    engaged.append(m.name)
    engaged.append(w.name)
    print('Matched: ({m},{w})'.format(m = m.name, w = w.name))

def rekt(m, w):
    print('{name} remains free'.format(name = m.name))
    m.add_count(w.name)
    w.add_count(m.name)

def dumped(m, w, engaged):
    print('{m} is now free'.format(m = m.name))
    engaged.remove(m.name)
    engaged.remove(w.name)
    m.free = True
    w.free = True

if __name__ == "__main__":
    v = Man(1,'V', None, True, ['B','A','D','E','C'])
    w = Man(2,'W', None, True, ['D','B','A','C','E'])
    x = Man(3,'X', None, True, ['B','E','C','D','A'])
    y = Man(4,'Y', None, True, ['A','D','C','B','E'])
    z = Man(5,'Z', None, True, ['B','D','A','E','C'])

    a = Woman(1,'A', None, True, ['Z','V','W','Y','X'])
    b = Woman(2,'B', None, True, ['X','W','Y','V','Z'])
    c = Woman(3,'C', None, True, ['W','X','Y','Z','V'])
    d = Woman(4,'D', None, True, ['V','Z','Y','X','W'])
    e = Woman(5,'E', None, True, ['Y','W','Z','X','V'])

    #To have woman be the ones proposing just put them in the men array & men in women array
    #women = [v,w,x,y,z]
    men = [z,y,x,w,v]
    
    #men = [a,b,c,d,e]
    women = [a,b,c,d,e]
    for m in men:
        print(m.name, end=': ')
        m.print_list()
    print()
    for w in women:
        print(w.name, end = ': ')
        w.print_list()
    print()
    
    engaged = []
    wife = []
    husband = []
    # While there is still a free man who hasnt proposed to every girl
    while free_man_exists(men, women):
        # choose such a man m
        m = choose_man(men)
        # Let w be the highest-ranked woman in m's preference list to whom m has not yet proposed
        w = m.choose_highest_unproposed()
        # use w (name) to get the correct woman object
        for woman in women:
            if woman.name == w:
                w = woman

        print('{m} proposes to {w}'.format(m = m.name, w = w.name))
        # If w is free then (m,w) become engaged
        if w.free == True:
            engagement(m, w)
        # Else w is currently engaged to m_prime
        else:
            # assign m_prime as w's current match
            m_prime = w.match
            # if w prefers m_prime to m then m remains free
            if w.list.index(m_prime) < w.list.index(m.name):

                # m remains free
                rekt(m, w)
            # else w prefers m to m_prime
            else:
                for man in men:
                    if man.name == m_prime:
                        m_prime_obj = man
                        break
                dumped(m_prime_obj, w, engaged)
                engagement(m, w)
            
    for man in men:
        man.match_print()
