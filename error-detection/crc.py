from math import log, ceil


def CRC(dataword, generator):
    dword = int(dataword, 2)
    l_gen = len(generator)

    # append 0s to dividend
    dividend = dword << (l_gen - 1)

    # shft specifies the no. of least significant
    # bits not being XORed
    shft = ceil(log(dividend + 1, 2)) - l_gen

    # ceil(log(dividend+1 , 2)) is the no. of binary
    # digits in dividend
    generator = int(generator, 2)

    while dividend >= generator or shft >= 0:

        # bitwise XOR the MSBs of dividend with generator
        # replace the operated MSBs from the dividend with
        # remainder generated
        rem = (dividend >> shft) ^ generator
        dividend = (dividend & ((1 << shft) - 1)) | (rem << shft)

        # change shft variable
        shft = ceil(log(dividend + 1, 2)) - l_gen

    # finally, AND the initial dividend with the remainder (=dividend)
    codeword = dword << (l_gen - 1) | dividend
    print("Remainder:", bin(dividend).lstrip("-0b"))
    print("Codeword :", bin(codeword).lstrip("-0b"))


# Driver code
# dataword = "10011101"
# generator = "1001"
print("Code by : Sahil Kaling (20BCT0106)")
dataword = input("Enter the data word: ")
generator = input("Enter the generator: ")
CRC(dataword, generator)
