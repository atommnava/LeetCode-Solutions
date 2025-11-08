class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        result = 0

        def dfs(r, c):
            if (r, c) in visited:
                return

            visited.add((r, c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1"):
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    result += 1

        return result



