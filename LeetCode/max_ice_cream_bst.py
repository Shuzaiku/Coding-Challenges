# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Defining class
        class Node_BST:
            def __init__(self, cost):
                self.cost = cost
                self.right = None
                self.left = None
                self.existences = 1

            def add_child(self, child_cost):
                if child_cost > self.cost:
                    if self.right:
                        self.right.add_child(child_cost)
                    else:
                        self.right = Node_BST(child_cost)
                elif child_cost < self.cost:
                    if self.left:
                        self.left.add_child(child_cost)
                    else:
                        self.left = Node_BST(child_cost)
                else:
                    self.existences += 1

            def get_max_bars(self, curr_bars, curr_coins) -> Tuple[int, int]:
                # visit left tree
                if self.left:
                    curr_bars, curr_coins = self.left.get_max_bars(curr_bars, curr_coins)

                # visit curr node
                x = min(curr_coins // self.cost, self.existences)
                curr_coins = curr_coins - self.cost * x
                if curr_coins >= 0:
                    curr_bars += 1 * x
                    print(f"Curr bars: {curr_bars} | Curr coins: {curr_coins}")
                else:
                    return curr_bars, curr_coins

                # visit right tree
                if self.right:
                    curr_bars, curr_coins = self.right.get_max_bars(curr_bars, curr_coins)
                
                # return vals
                return curr_bars, curr_coins

        # Executing class
        root = Node_BST(coins)
        root.existences = 0
        for cost in costs:
            root.add_child(cost)
        
        max_bars, _ = root.get_max_bars(0, coins)
        return max_bars
