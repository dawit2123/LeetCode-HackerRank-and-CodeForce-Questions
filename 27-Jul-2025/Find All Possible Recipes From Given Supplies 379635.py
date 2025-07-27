# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook= {s:True for s in supplies}
        recipes_map={r:i for i, r in enumerate(recipes)}

        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            if r not in recipes_map:
                return False
            can_cook[r]=False
            for neighbour in ingredients[recipes_map[r]]:
                if not dfs(neighbour):
                    return False
            can_cook[r]=True
            return can_cook[r]
        return [recipe for recipe in recipes if dfs(recipe)]  