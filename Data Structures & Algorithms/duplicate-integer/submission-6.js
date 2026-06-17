class Solution {

hasDuplicate(nums) {
    const seen = new Set();

    for (const num of nums) {
        if (seen.has(num)) {
            return true; // The loop stops here if a duplicate is found
        }
        seen.add(num);
    }

    // This line is only reached if the loop finishes completely.
    // If the loop finishes, it means no duplicates were found.
    return false; 
        }
}