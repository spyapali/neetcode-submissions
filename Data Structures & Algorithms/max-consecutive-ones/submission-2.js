class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    // nums = [1,1,0,1,1,1]
    // consecutive_ones = 2
    // max_consecutive_ones = 3

    //            j 
    //          s 
    // [1,1,0,1,1,1]

    // max_count = 2 
    // count = 3

    findMaxConsecutiveOnes(nums) {
        let max_consecutive_ones = 0 
        let local_count = 0 
        for (let j = 0; j < nums.length; j++) {
            let value = nums[j]
            if (value === 1) {
                local_count += 1;
            } else if (value === 0) {
                max_consecutive_ones = Math.max(local_count, max_consecutive_ones)
                local_count = 0;
            }
        }
        return Math.max(max_consecutive_ones, local_count)
    }
}
