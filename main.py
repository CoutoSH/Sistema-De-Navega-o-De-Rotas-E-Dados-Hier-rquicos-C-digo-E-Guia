g = city.graph
while True:
print(f"\nEditing graph of {city.name} (ID {city.city_id})")
print("1) Add district (node)")
print("2) Add road (edge)")
print("3) BFS")
print("4) DFS")
print("5) Dijkstra distances from a source")
print("6) Show nodes")
print("0) Back")
op = input("> ").strip()
if op == "1":
v = input("District name: ").strip()
g.add_node(v)
print("Added node.")
elif op == "2":
u = input("From: ").strip()
v = input("To: ").strip()
try:
w = float(input("Weight (distance): ").strip())
except ValueError:
print("Invalid weight.")
continue
undirected = input("Undirected? (y/n): ").strip().lower() != 'n'
g.add_edge(u, v, w, undirected=undirected)
print("Added edge.")
elif op == "3":
s = input("Start: ").strip()
print_complexity("BFS_DFS")
print("BFS order:", g.bfs(s))
elif op == "4":
s = input("Start: ").strip()
print_complexity("BFS_DFS")
print("DFS order:", g.dfs(s))
elif op == "5":
s = input("Source: ").strip()
print_complexity("DIJKSTRA")
dist = g.dijkstra(s)
for k, d in dist.items():
print(f" - {k}: {d}")
elif op == "6":
print("Nodes:", list(g.nodes()))
elif op == "0":
break
else:
print("Invalid.")




# ------------- Main Loop -------------


def main() -> None:
while True:
print("\nCity & Routes System (AVL + Graph)")
print("1) Add city")
print("2) Remove city")
print("3) Show traversals")
print("4) Manage a city's graph")
print("0) Exit")
op = input("> ").strip()
if op == "1":
add_city()
elif op == "2":
remove_city()
elif op == "3":
show_traversal()
elif op == "4":
edit_graph()
elif op == "0":
print("Bye!")
return
else:
print("Invalid option.")




if __name__ == "__main__":
main()
