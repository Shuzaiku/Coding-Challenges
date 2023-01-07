class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        left_products = [1] * num_len
        total_products = [1] * num_len

        # get left products of each index
        product_left = 1
        for i in range(num_len):
            left_products[i] = product_left
            product_left *= nums[i]

        # get right products of each index and build result
        product_right = 1
        for i in range(num_len-1, -1, -1):
            total_products[i] = left_products[i] * product_right
            product_right *= nums[i]

        return total_products
        
