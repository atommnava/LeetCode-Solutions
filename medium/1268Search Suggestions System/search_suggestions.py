class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        left, right = 0, len(products) - 1
        result = []
        for i in range(len(searchWord)):
            search = searchWord[i]

            while left <= right and (len(products[left]) <= i or products[left][i] != search):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != search):
                right -= 1
            words_left = right - left + 1

            if words_left >= 3:
                # Earliest three letter in the alphabet
                result.append([products[left], products[left+1], products[left+2]])
            elif words_left == 2:
                result.append([products[left], products[left+1]])
            elif words_left == 1:
                result.append([products[left]])
            else:
                result.append([])
        return result
