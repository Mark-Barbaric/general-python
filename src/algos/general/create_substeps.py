"""_summary_"""
def create_substeps(nums: list):
    index = 1
    sub_steps = []
    while len(nums) > 0:

        if len(nums) < index:
            return False
        else:
            sub_steps.append(nums[:index])

        nums = nums[index:]
        index += 1

    return sub_steps
