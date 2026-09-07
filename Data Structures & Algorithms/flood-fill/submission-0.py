class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, sr, sc, color, orgcol):
            if min(sr,sc) < 0 or sr ==len(image) or sc ==len(image[0]) or image[sr][sc] != orgcol or image[sr][sc] == color:
                return image
            image[sr][sc] = color

            image = dfs(image, sr + 1, sc, color, orgcol)
            image = dfs(image, sr - 1, sc, color, orgcol)
            image = dfs(image, sr, sc + 1, color, orgcol)
            image = dfs(image, sr, sc - 1, color, orgcol)

            return image

        return dfs(image, sr, sc, color, image[sr][sc])