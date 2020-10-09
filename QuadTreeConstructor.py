class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid) -> 'Node':
        def quad(g):
            center = len(g) // 2
            tlg = [i[:center] for i in g[:center]]
            if not sum(i.count(1) for i in tlg) or not sum(
                    i.count(0) for i in tlg):
                tl = Node(tlg[0][0], 1)
            else:
                tl2, tr2, bl2, br2 = quad(tlg)
                tl = Node(1, 0, tl2, tr2, bl2, br2)
            trg = [i[center:] for i in g[:center]]
            if not sum(i.count(1) for i in trg) or not sum(
                    i.count(0) for i in trg):
                tr = Node(trg[0][0], 1)
            else:
                tl2, tr2, bl2, br2 = quad(trg)
                tr = Node(1, 0, tl2, tr2, bl2, br2)
            blg = [i[:center] for i in g[center:]]
            if not sum(i.count(1) for i in blg) or not sum(
                    i.count(0) for i in blg):
                bl = Node(blg[0][0], 1)
            else:
                tl2, tr2, bl2, br2 = quad(blg)
                bl = Node(1, 0, tl2, tr2, bl2, br2)
            brg = [i[center:] for i in g[center:]]
            if not sum(i.count(1) for i in brg) or not sum(
                    i.count(0) for i in brg):
                br = Node(brg[0][0], 1)
            else:
                tl2, tr2, bl2, br2 = quad(brg)
                br = Node(1, 0, tl2, tr2, bl2, br2)
            return tl, tr, bl, br

        if not sum(i.count(1) for i in grid) or not sum(
                i.count(0) for i in grid):
            return Node(grid[0][0], 1)
        else:
            tl, tr, bl, br = quad(grid)
            root = Node(1, 0, tl, tr, bl, br)
            return root