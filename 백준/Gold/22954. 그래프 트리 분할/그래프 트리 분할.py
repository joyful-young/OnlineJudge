# 22954. 그래프 트리 분할
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N <= 2 or M < N - 2:
	print(-1)
else:	
	adjL = [[] for _ in range(N + 1)]
	for i in range(1, M+1):
		u, v = map(int, input().split())
		adjL[u].append([v, i])
		adjL[v].append([u, i])

	# print(adjL)

	visited = [False for _ in range(N + 1)]
	trees_node_list = []
	trees_edge_list = []
	leaf_nodes = []

	for i in range(1, N + 1):
		if not visited[i]:
			visited[i] = True
			nodes = [i]
			edges = []
			stack = [i]

			while stack:
				node = stack.pop()
				for next_node, edge_num in adjL[node]:
					if not visited[next_node]:
						visited[next_node] = True
						nodes.append(next_node)
						edges.append(edge_num)
						stack.append(next_node)
			
			leaf_nodes.append(node)
			trees_node_list.append(nodes)
			trees_edge_list.append(edges)

	if len(trees_node_list) > 2:
		print(-1)
	elif len(trees_node_list) == 2:
		if len(trees_node_list[0]) == len(trees_node_list[1]):
			print(-1)
		else:
			print(len(trees_node_list[0]), len(trees_node_list[1]))
			print(*trees_node_list[0])
			print(*trees_edge_list[0])
			print(*trees_node_list[1])
			print(*trees_edge_list[1])
	else:
		new_nodes = [node for node in trees_node_list[0] if node != leaf_nodes[0]]

		new_edges = []
		for edge in trees_edge_list[0]:
			for node_num, edge_num in adjL[leaf_nodes[0]]:
				if edge == edge_num:
					break
			else:
				new_edges.append(edge)

		print(len(new_nodes), 1)
		print(*new_nodes)
		print(*new_edges)
		print(leaf_nodes[0])
		print()