"""
Input
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
Output
[null, null, 4, null, 6]

Explanation
Excel excel = new Excel(3, "C");
 // construct a 3*3 2D array with all zero.
 //   A B C
 // 1 0 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.set(1, "A", 2);
 // set mat[1]["A"] to be 2.
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
 // set mat[3]["C"] to be the sum of value at mat[1]["A"] and the values sum of the rectangle range whose top-left cell is mat[1]["A"] and bottom-right cell is mat[2]["B"].
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 4
excel.set(2, "B", 2);
 // set mat[2]["B"] to be 2. Note mat[3]["C"] should also be changed.
 //   A B C
 // 1 2 0 0
 // 2 0 2 0
 // 3 0 0 6
excel.get(3, "C"); // return 6
"""

import collections
class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.col = lambda c: ord(c) - ord('A')
        self.H, self.W = H, self.col(W) + 1
        self.values = collections.defaultdict(int)
        self.target = collections.defaultdict(lambda : collections.defaultdict(int))
        self.source = collections.defaultdict(lambda : collections.defaultdict(int))
        self.getIdx = lambda r, c: (r - 1) * self.W + self.col(c)
    
    def updateTgt(self, idx, delta):
        queue = [idx]
        while queue:
            first = queue.pop(0)
            for tgt in self.target[first]:
                self.values[tgt] += self.target[first][tgt] * delta
                queue.append(tgt)

    def removeSrc(self, idx):
        for src in self.source[idx]:
            del self.target[src][idx]
        del self.source[idx]

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        idx = self.getIdx(r, c)
        delta = v - self.values[idx]
        self.values[idx] = v
        self.removeSrc(idx)
        self.updateTgt(idx, delta)

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        return self.values[self.getIdx(r, c)]

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        idx = self.getIdx(r, c)
        self.removeSrc(idx)
        cval = self.values[idx]
        self.values[idx] = 0
        for src in strs:
            if ':' not in src:
                sc, sr = src[0], int(src[1:])
                sidx = self.getIdx(sr, sc)
                self.target[sidx][idx] += 1
                self.source[idx][sidx] += 1
                self.values[idx] += self.values[sidx]
            else:
                st, ed = src.split(':')
                for r in range(int(st[1:]), int(ed[1:]) + 1):
                    for c in range(self.col(st[0]), self.col(ed[0]) + 1):
                        sidx = (r - 1) * self.W + c
                        self.target[sidx][idx] += 1
                        self.source[idx][sidx] += 1
                        self.values[idx] += self.values[sidx]
        self.updateTgt(idx, self.values[idx] - cval)
        return self.values[idx]

# Your Excel object will be instantiated and called as such:
H = 3
W = 'C'
obj = Excel(H, W)

obj.set(1,'A',2)
#obj.sum(3,C',["A1","A1:B2"])
print(obj.sum(3, "C", ["A1", "A1:B2"]))
obj.set(4,'B',4)

print(obj.get(4,'B'))
#param_2 = obj.get(r,c)
#param_3 = obj.sum(r,c,strs) 