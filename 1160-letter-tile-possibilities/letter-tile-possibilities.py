class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(tile_counter: Counter) -> int:
                    combinations_count = 0  
                    for tile, count in tile_counter.items():
                        if count > 0:
                            combinations_count += 1  
                            tile_counter[tile] -= 1 
                            combinations_count += dfs(tile_counter)
                            tile_counter[tile] += 1
                    return combinations_count

        tile_counter = Counter(tiles)
        return dfs(tile_counter)