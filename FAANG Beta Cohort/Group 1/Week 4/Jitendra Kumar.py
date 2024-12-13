#Number of Islands https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    # Time complexity O(number of cells)
    # Space complexity O(number of cells) worst case
  
    def num_islands(grid):
      if not grid or not grid[0]:
          return 0
      rows, cols = len(grid), len(grid[0])
      island_count = 0
      def bfs(r, c):
          queue = deque([(r, c)])
          directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
          while queue:
              row, col = queue.popleft()
              for dr, dc in directions:
                  nr, nc = row + dr, col + dc
                  if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                      grid[nr][nc] = '0'
                      queue.append((nr, nc))
      for r in range(rows):
          for c in range(cols):
              if grid[r][c] == '1':
                  island_count += 1
                  grid[r][c] = '0'
                  bfs(r, c)
      return island_count
      # Time complexity O(number of cells)
      # Space complexity O(number of cells) worst case
