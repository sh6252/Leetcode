class Solution:

    class Node:
        def __init__(self, left_char='', right_char='',
                     left_run=0, right_run=0,
                     best=0, length=0):

            self.left_char = left_char
            self.right_char = right_char

            self.left_run = left_run
            self.right_run = right_run

            self.best = best
            self.length = length


    def merge(self, left, right):

        # -------------------------
        # left_run
        # -------------------------

        if left.left_char == right.left_char:

            if left.left_run == left.length:
                left_run = left.length + right.left_run
            else:
                left_run = left.left_run

        else:
            left_run = left.left_run


        # -------------------------
        # right_run
        # -------------------------

        if left.right_char == right.right_char:

            if right.right_run == right.length:
                right_run = right.length + left.right_run
            else:
                right_run = right.right_run

        else:
            right_run = right.right_run


        # -------------------------
        # best
        # -------------------------

        best = max(left.best, right.best)

        # האם נוצר רצף שחוצה את הגבול?
        if left.right_char == right.left_char:
            cross = left.right_run + right.left_run
            best = max(best, cross)


        return self.Node(
            left_char=left.left_char,
            right_char=right.right_char,

            left_run=left_run,
            right_run=right_run,

            best=best,

            length=left.length + right.length
        )


    def build(self, s, node, l, r):

        # Leaf
        if l == r:

            self.tree[node] = self.Node(
                left_char=s[l],
                right_char=s[l],
                left_run=1,
                right_run=1,
                best=1,
                length=1
            )

            return


        mid = (l + r) // 2

        # Build left child
        self.build(s, node * 2, l, mid)

        # Build right child
        self.build(s, node * 2 + 1, mid + 1, r)

        # Merge children
        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )


    def update(self, s, node, l, r, index, char):

        # Leaf
        if l == r:

            s[l] = char

            self.tree[node] = self.Node(
                left_char=char,
                right_char=char,
                left_run=1,
                right_run=1,
                best=1,
                length=1
            )

            return


        mid = (l + r) // 2

        if index <= mid:
            self.update(
                s,
                node * 2,
                l,
                mid,
                index,
                char
            )

        else:
            self.update(
                s,
                node * 2 + 1,
                mid + 1,
                r,
                index,
                char
            )


        # Recalculate current node
        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )


    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)

        # Segment Tree
        self.tree = [
            None
        ] * (4 * n)

        # String -> list כדי שנוכל לשנות תווים
        s = list(s)

        # Build
        self.build(
            s,
            1,
            0,
            n - 1
        )

        answer = []

        for char, index in zip(
            queryCharacters,
            queryIndices
        ):

            # Update
            self.update(
                s,
                1,
                0,
                n - 1,
                index,
                char
            )

            # התשובה נמצאת ב-Root
            answer.append(
                self.tree[1].best
            )

        return answer