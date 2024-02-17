def remove_zeroes(numbers: list[int]) -> int:
    non_zeros_count = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[non_zeros_count], numbers[i] = numbers[i], numbers[non_zeros_count]
            non_zeros_count += 1

    return non_zeros_count


nums = [0, 42, 21, 0, 100, 0, 5, 1, 0, 7, 3, 0, 404, 0]
new_len = remove_zeroes(nums)

assert new_len == 8
assert nums[:new_len] == [42, 21, 100, 5, 1, 7, 3, 404]

nums = [0]
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

nums = []
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

nums = [1,2,3,4]
new_len = remove_zeroes(nums)

assert new_len == 4
assert nums[:new_len] == [1,2,3,4]

nums = [1,2,3,4,0]
new_len = remove_zeroes(nums)

assert new_len == 4
assert nums[:new_len] == [1,2,3,4]

nums = [1,2,0,3,4]
new_len = remove_zeroes(nums)

assert new_len == 4
assert nums[:new_len] == [1,2,3,4]

nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

nums = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
new_len = remove_zeroes(nums)

assert new_len == 1
assert nums[:new_len] == [1]