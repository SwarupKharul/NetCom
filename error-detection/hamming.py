def calcRedundantBits(m):

    for i in range(m):
        if 2**i >= m + i + 1:
            return i


def posRedundantBits(data, r):

    # Redundancy bits are placed at the positions
    # which correspond to the power of 2.
    j = 0
    k = 1
    m = len(data)
    res = ""

    # If position is power of 2 then insert '0'
    # Else append the data
    for i in range(1, m + r + 1):
        if i == 2**j:
            res = res + "0"
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    # The result is reversed since positions are
    # counted backwards. (m + r+1 ... 1)
    return res[::-1]


def calcParityBits(arr, r):
    n = len(arr)

    # For finding rth parity bit, iterate over
    # 0 to r - 1
    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            # If position has 1 in ith significant
            # position then Bitwise OR the array value
            # to find parity bit value.
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1 * j])
                # -1 * j is given since array is reversed

        # String Concatenation
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
        arr = arr[: n - (2**i)] + str(val) + arr[n - (2**i) + 1 :]
    return arr


# Enter the data to be transmitted
print("Code by : Swarup Kharul (20BCT0073)")
data = input("Enter the data: ")
# data = '1011001'

# Calculate the no of Redundant Bits Required
m = len(data)
r = calcRedundantBits(m)

# Determine the positions of Redundant Bits
arr = posRedundantBits(data, r)

# Determine the parity bits
arr = calcParityBits(arr, r)

# Data to be transferred
print("Generated Code Word is " + arr)
