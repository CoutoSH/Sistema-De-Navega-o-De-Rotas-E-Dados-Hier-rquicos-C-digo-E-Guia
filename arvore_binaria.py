"""
Binary Search Tree (BST) with recursive traversals and removal.
Includes DSW (Day–Stout–Warren) global rebalancing.

Complexity (average):
- search/insert/remove: O(h) where h is tree height; expected ~O(log n) on random data
- traversals (inorder/preorder/postorder): O(n)
Worst-case (unbalanced):
- search/insert/remove: O(n)

DSW algorithm:
- Creates a backbone (vine) with right rotations: O(n)
- Performs a series of left rotations (compressions) to build a balanced tree: O(n)
- Total: O(n)

PT-BR resumo:
- Operações básicas em árvore binária custam O(h).
- No pior caso (degen.), h≈n. O DSW reequilibra em O(n).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Generator, Optional, Tuple


@dataclass
class BSTNode:
    key: Any
    value: Any | None = None
    left: Optional["BSTNode"] = None
    right: Optional["BSTNode"] = None


class BST:
    def __init__(self, key_fn: Callable[[Any], Any] | None = None):
        """
        key_fn: function mapping a record to an orderable key. If None, the record itself is the key.
        """
        self.root: Optional[BSTNode] = None
        self._key_fn = key_fn if key_fn else (lambda x: x)

    # ---------- Search ----------
    def search(self, key: Any) -> Optional[Any]:
        node = self.root
        while node:
            if key == node.key:
                return node.value if node.value is not None else node.key
            node = node.left if key < node.key else node.right
        return None

    # ---------- Insert ----------
    def insert(self, record: Any) -> None:
        key = self._key_fn(record)
        if self.root is None:
            self.root = BSTNode(key, record if record != key else None)
            return
        parent: Optional[BSTNode] = None
        node = self.root
        while node:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:  # update value
                node.value = record if record != key else None
                return
        new_node = BSTNode(key, record if record != key else None)
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    # ---------- Remove ----------
    def remove(self, key: Any) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node: Optional[BSTNode], key: Any) -> Optional[BSTNode]:
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # node to delete
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # two children: swap with inorder successor
            succ = self._min_node(node.right)
            node.key, node.value = succ.key, succ.value
            node.right = self._remove(node.right, succ.key)
        return node

    def _min_node(self, node: BSTNode) -> BSTNode:
        while node.left:
            node = node.left
        return node

    # ---------- Traversals ----------
    def inorder(self) -> Generator[Any, None, None]:
        def _in(n: Optional[BSTNode]):
            if n:
                yield from _in(n.left)
                yield n.value if n.value is not None else n.key
                yield from _in(n.right)
        yield from _in(self.root)

    def preorder(self) -> Generator[Any, None, None]:
        def _pre(n: Optional[BSTNode]):
            if n:
                yield n.value if n.value is not None else n.key
                yield from _pre(n.left)
                yield from _pre(n.right)
        yield from _pre(self.root)

    def postorder(self) -> Generator[Any, None, None]:
        def _post(n: Optional[BSTNode]):
            if n:
                yield from _post(n.left)
                yield from _post(n.right)
                yield n.value if n.value is not None else n.key
        yield from _post(self.root)

    # ---------- DSW Rebalancing ----------
    def dsw_balance(self) -> None:
        """Perform Day–Stout–Warren rebalancing in O(n)."""
        if self.root is None:
            return
        # 1) Create backbone (vine): right-rotate while left child exists
        pseudo = BSTNode(key=None)
        pseudo.right = self.root
        tail = pseudo
        rest = tail.right
        while rest:
            if rest.left:
                # right rotation
                temp = rest.left
                rest.left = temp.right
                temp.right = rest
                rest = temp
                tail.right = temp
            else:
                tail = rest
                rest = rest.right
        # 2) Count nodes in vine
        n = 0
        node = pseudo.right
        while node:
            n += 1
            node = node.right
        # 3) Compute largest m = 2^⌊log2(n+1)⌋ - 1
        m = 1
        while m <= n:
            m = (m << 1) + 1
        m = (m >> 1) - 1
        # 4) First compression: n - m left rotations
        self._compress(pseudo, n - m)
        # 5) Repeated compressions: halve until done
        while m > 1:
            m //= 2
            self._compress(pseudo, m)
        self.root = pseudo.right

    def _compress(self, pseudo: BSTNode, count: int) -> None:
        scanner = pseudo
        for _ in range(count):
            child = scanner.right
            if child is None:
                return
            grandchild = child.right
            if grandchild is None:
                return
            # left rotation at child
            child.right = grandchild.left
            grandchild.left = child
            scanner.right = grandchild
            scanner = grandchild
