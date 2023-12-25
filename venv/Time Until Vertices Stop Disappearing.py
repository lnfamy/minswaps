"""
returns the number of seconds until vertices stop disappearing from the graph
returns 0 if no vertices are going to disappear at all

N - number of vertices in the graph
A - array 1 for vertices connected by edges
B - array 2 for vertices connected by edges
such that for every index i in range of arrays A and B (which are of the same length), A[i] and B[i] are
connected by an edge
"""
import collections


def solution(N, A, B):
    # create an adjacency list
    graph = collections.defaultdict(list)
    # for each pair of 'neighbours' A[i] and B[i], add them to each others' adjacency lists
    for i in range(len(A)):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])

    # initialize a queue of vertices that are going to disappear
    q = []
    for v in range(N):
        # len(graph[v]) <= 1 == if graph[v] has one or less edges connected to it
        if len(graph[v]) <= 1:
            q.append(graph[v])

    # now the counting
    secs = 0
    while q:
        secs += 1
        v = q.pop(0)

        # now remove the popped vertex form the graph, along with all its edges
        for neighbor in graph[v]:
            graph[neighbor].remove(v)
            # if removing the popped vertex from its neighbors adjacency list made the neighbor also qualify for
            # deletion, add it to the deletion queue
            if len(graph[neighbor]) <= 1:
                q.append(neighbor)

    # we reached here. if the queue was never populated to begin with, that means that there were never any vertices
    # in the graph that qualified for deletion and therefore the number of seconds taken to delete them all is
    # obviously 0. otherwise, if the queue was populated, we iterated through it and removed every qualifying vertex
    # and its edges and counted the seconds, which means we'll return here the number of seconds it took for the
    # vertices to stop disappearing
    return secs