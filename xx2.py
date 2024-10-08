# from collections import defaultdict

# # def dfs(node, sz):
# #     if sz[node] > 0:
# #         return sz[node]
# #     for child in tree[node]:
# #         dfs(child, sz)
# #         sz[node] += sz[child] + 1
# #     return sz[node]

# # 主函数来处理每组测试数据
# def count_similar_nodes(n, tree):
#     if n==1:
#         return 0
#     sz = [0] * (n + 1)  # 存储每个节点的子节点数量
#     # dfs遍历树，计算每个节点的子节点数量
#     for i in range(1, n + 1):
#         # sz[i] = dfs(i, sz)
#     # for i in range(1, n + 1):
#         sz[i] = len(tree[i])
    
#     # 统计相似节点对的数量
#     size_count = {}
#     for size in sz[1:]:
#         size_count[size] = size_count.get(size, 0) + 1
#     print(size_count)
#     res = 0
#     for count in size_count.values():
#         if count > 1:
#             # 如果有多个节点的子节点数量相同，则从中选出两两配对的方式
#             res += count * (count - 1) // 2
    
#     return res

# T = int(input().strip())  # 测试组数

# for _ in range(T):
#     n = int(input().strip())  # 节点数量
#     tree = defaultdict(list)
#     for _ in range(n - 1):
#         u, v = map(int, input().split())
#         tree[u].append(v)
#     result = count_similar_nodes(n, tree)
#     print(result)
import json

dt = {
    "query": "你是谁",
    "response": "我是小智",
    "video": ["https://www.bilibili.com/video/BV1K44y1s7xv/"]
}

with open("data.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(dt, ensure_ascii=False) + "\n")

