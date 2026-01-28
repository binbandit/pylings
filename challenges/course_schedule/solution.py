"""
# Course Schedule

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.
"""

from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # TODO: Detect Cycle in Directed Graph (DFS/BFS Topological Sort)
    pass
