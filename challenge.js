// Print out all of the numbers in the following array that are divisible by 3:
// [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
// The expected output for the above input is:
// 27
// 81
// 9
// 27
// 99
// 63
// 42

var nums = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]


function divbythree(nums) {
    var threes = []
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] % 3 === 0) {
            threes.push(nums[i])
        }
    }
    return threes
}

console.log(divbythree(nums))