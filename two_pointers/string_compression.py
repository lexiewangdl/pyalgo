class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        # l is the length of resulting array, which is index where next modified element should go
        l = 0
        # r is used to traverse the array
        r = 1

        curr_char = chars[0]
        curr_count = 1

        while r < len(chars):
            if chars[r] == curr_char:
                curr_count += 1
            else:
                # update the modified part of array
                chars[l] = curr_char
                l += 1
                if curr_count > 1:  # if count of char is more than 1, store the count
                    count_str = str(curr_count)
                    for c in count_str:
                        chars[l] = c
                        l += 1

                # update current character
                curr_char = chars[r]
                curr_count = 1
            r += 1

        # finally, take care of last character
        if curr_count > 1:
            chars[l] = curr_char
            l += 1
            count_str = str(curr_count)
            for c in count_str:
                chars[l] = c
                l += 1
        else:
            chars[l] = curr_char
            l += 1

        return l
