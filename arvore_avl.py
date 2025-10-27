"""
# ---------- Remove ----------
def remove(self, key: Any) -> None:
self.root = self._remove(self.root, key)


def _remove(self, node: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
if not node:
return None
if key < node.key:
node.left = self._remove(node.left, key)
elif key > node.key:
node.right = self._remove(node.right, key)
else:
# delete this node
if not node.left:
return node.right
if not node.right:
return node.left
# two children: inorder successor
succ = self._min_node(node.right)
node.key, node.value = succ.key, succ.value
node.right = self._remove(node.right, succ.key)
node.height = 1 + max(_h(node.left), _h(node.right))
return self._rebalance(node)


def _min_node(self, n: AVLNode) -> AVLNode:
while n.left:
n = n.left
return n


# ---------- Rotations & Rebalance ----------
def _rebalance(self, z: AVLNode) -> AVLNode:
bf = _bf(z)
# Left heavy
if bf > 1:
if _bf(z.left) < 0:
z.left = self._rotate_left(z.left) # LR case
return self._rotate_right(z) # LL case
# Right heavy
if bf < -1:
if _bf(z.right) > 0:
z.right = self._rotate_right(z.right) # RL case
return self._rotate_left(z) # RR case
return z


def _rotate_left(self, x: AVLNode) -> AVLNode:
y = x.right
T2 = y.left if y else None
y.left = x
x.right = T2
x.height = 1 + max(_h(x.left), _h(x.right))
y.height = 1 + max(_h(y.left), _h(y.right))
return y


def _rotate_right(self, y: AVLNode) -> AVLNode:
x = y.left
T2 = x.right if x else None
x.right = y
y.left = T2
y.height = 1 + max(_h(y.left), _h(y.right))
x.height = 1 + max(_h(x.left), _h(x.right))
return x


# ---------- Traversals ----------
def inorder(self) -> Generator[Any, None, None]:
def _in(n: Optional[AVLNode]):
if n:
yield from _in(n.left)
yield n.value if n.value is not None else n.key
yield from _in(n.right)
yield from _in(self.root)


def preorder(self) -> Generator[Any, None, None]:
def _pre(n: Optional[AVLNode]):
if n:
yield n.value if n.value is not None else n.key
yield from _pre(n.left)
yield from _pre(n.right)
yield from _pre(self.root)


def postorder(self) -> Generator[Any, None, None]:
def _post(n: Optional[AVLNode]):
if n:
yield from _post(n.left)
yield from _post(n.right)
yield n.value if n.value is not None else n.key
yield from _post(self.root)
