# A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits,
# such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.
#
# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits,
# solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3],
# which should be interpreted as the word1 + word2 = word3 cryptarithm.
#
# If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution,
# becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a
# valid arithmetic solution, the answer is false.

def solution(crypt, solution):
    decrypted = ['', '', '']

    for i in range(0, len(crypt)):
        for j in range(0, len(crypt[i])):

            for p in range(0, len(solution)):

                if crypt[i][j] == solution[p][0]:
                    decrypted[i] += solution[p][1]

        if decrypted[i][0] == '0':
            return False

    return int(decrypted[0]) + int(decrypted[1]) == int(decrypted[2])


crypt1 = ["SEND",
          "MORE",
          "MONEY"]

solution1 = [["O", "0"],
             ["M", "1"],
             ["Y", "2"],
             ["E", "5"],
             ["N", "6"],
             ["D", "7"],
             ["R", "8"],
             ["S", "9"]]

print(solution(crypt1, solution1))
