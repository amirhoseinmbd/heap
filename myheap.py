class MinHeap :

    def __init__ (self):
        self.hlist = [None]
        #finish

    def insert(self, input):
        self.hlist.append(input)
        if len(self.hlist) > 2 :
            self.hup(len(self.hlist)-1)
        #finish
        

    def hup(self, index):
        parent = index // 2
        if parent == 0 : 
            return
        
        if self.hlist[parent] > self.hlist[index] :
            self.hlist[parent] , self.hlist[index] = self.hlist[index] , self.hlist[parent]
            self.hup(parent)

        #print(self.hlist)
        
    def min(self):
        min = self.hlist[1]
        print(min)
        self.hlist[1] = self.hlist[-1]
        self.hlist.pop()
        self.hdown(1)

    def hdown(self,parent):
        lchild = parent * 2
        rchild = parent * 2 + 1
        

        if lchild > len(self.hlist) and rchild > len(self.hlist) :
            return


        if lchild < len(self.hlist) and rchild < len(self.hlist) :

            if self.hlist[lchild] <= self.hlist[rchild] :  
                if self.hlist[lchild] < self.hlist[parent] :
                    self.hlist[lchild] , self.hlist[parent] = self.hlist[parent] , self.hlist[lchild]
                    self.hdown(lchild)

            if self.hlist[rchild] < self.hlist[lchild] :
                if self.hlist[rchild] < self.hlist[parent] :
                    self.hlist[rchild] , self.hlist[parent] = self.hlist[parent] , self.hlist[rchild]
                    self.hdown(rchild)

        if lchild < len(self.hlist) :
            if self.hlist[lchild] < self.hlist[parent] :
                self.hlist[lchild] , self.hlist[parent] = self.hlist[parent] , self.hlist[lchild]
                self.hdown(lchild)

        
a = MinHeap()
a.insert(2)
a.insert(1)
a.insert(0)
a.insert(4)
a.insert(3)
a.insert(1)
a.insert(2)
a.insert(5)
a.insert(6)
a.insert(2)
a.insert(12)
a.insert(0)
a.insert(6)
a.min()
a.min()
a.min()
a.min()
a.min()
a.min()
a.min()
a.min()
a.min()
print(a.hlist)

