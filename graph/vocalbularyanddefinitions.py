"""
Vertex:
    类似于Node with key and payload

Edge(arc):
    connects two vertices 单向或双向
    如果edges全部都是one-way，则成为有向图(directed graph or digraph)

Weight:
    Edges可能是加权 cuz there is a cost to go from one vertex to another

图的定义
G = (V, E):
    V 是一组vertices，E是一组edges
    每一条edge都是一个元组(v, w)   v,w ∈ V
    可以向edge元组中加入第三个元素，代表weight

path:

Cycle:
    A cycle in 有向图是指starts and ends at the same vertex
    有向无环图 Directed Acyclic graph DAG
"""
