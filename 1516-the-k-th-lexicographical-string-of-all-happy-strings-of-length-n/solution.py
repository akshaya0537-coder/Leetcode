class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.result = ""
        
        def dfs(current_string):
            if self.result:  # Optimization: if result found, stop exploring
                return

            if len(current_string) == n:
                self.count += 1
                if self.count == k:
                    self.result = current_string
                return

            for char in ['a', 'b', 'c']:
                if not current_string or char != current_string[-1]:
                    dfs(current_string + char)
        dfs("")
        return self.result            
