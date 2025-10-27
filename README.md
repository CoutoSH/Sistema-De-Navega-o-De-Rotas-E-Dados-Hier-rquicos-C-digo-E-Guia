## 💡 Como executar

1. Salve os quatro arquivos na mesma pasta (conforme estrutura).
2. No terminal, execute:

```bash
python main.py
```

3. Use o menu para:
- Cadastrar/Remover cidades (AVL, O(log n))
- Visualizar percursos (pre/in/post-order, O(n))
- Entrar no grafo de uma cidade e rodar BFS/DFS/Dijkstra

---

## 📊 Saída de Complexidade (exemplos)

- Após inserir cidade: `[Complexity] AVL_insert: O(log n)`
- Após remover cidade: `[Complexity] AVL_remove: O(log n)`
- Ao mostrar percursos: `[Complexity] TRAVERSAL: O(n)`
- No grafo: `[Complexity] BFS_DFS: O(V + E)` ou `[Complexity] DIJKSTRA: O(E log V)`

---

## 🔧 Extensão (Desafio Extra: DSW)

- O **DSW** está implementado em `arvore_binaria.py` via `BST.dsw_balance()`.
- Você pode criar uma BST (sem AVL), inserir dados em ordem crescente (pior caso), e então chamar `dsw_balance()` para comparar o tempo de busca antes/depois (usando `time.perf_counter()`):

```python
from arvore_binaria import BST
import time

bst = BST(key_fn=lambda x: x)
for i in range(1, 5001):
    bst.insert(i)

# Busca antes do DSW
start = time.perf_counter()
for k in range(1, 5001, 10):
    bst.search(k)
print("Before DSW:", time.perf_counter() - start)

bst.dsw_balance()

# Busca depois do DSW
start = time.perf_counter()
for k in range(1, 5001, 10):
    bst.search(k)
print("After DSW:", time.perf_counter() - start)
```

---

## ✅ Observações de Projeto

- **Imutabilidade de chave**: cidades são indexadas por `city_id` (int). Nomes podem repetir, IDs não.
- **Pesos em Dijkstra**: use valores positivos (distâncias/tempos). Com arestas não ponderadas, mantenha peso 1.
- **Direção de arestas**: por padrão `undirected=True`; ajuste conforme o cenário viário.
- **Se quiser comparar BST vs AVL**: crie um `BST` paralelo (com as mesmas cidades) e avalie tempos/configurações.

---

## 📚 Referências (sugeridas)
- Cormen, T. H. et al. *Algoritmos: Teoria e Prática*.
- Szwarcfiter, J. L.; Markezon, L. *Estruturas de Dados e Seus Algoritmos*.
- Ziviane, N. *Projeto de Algoritmos*.

