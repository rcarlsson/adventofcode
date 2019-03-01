import sys


def compare(str1, str2):
    result = ""
    for idx in range(len(str1)):
        if str1[idx] == str2[idx]:
            result = result + str1[idx]
    return result


def find_best_match(boxIds):
    for idx1 in range(len(boxIds)):
        for idx2 in range(idx1+1, len(boxIds)):
            match = compare(boxIds[idx1], boxIds[idx2])
            if len(match) == len(boxIds[idx1])-1:
                return match                


def solve(file_name):
    boxIds = []
    with open(file_name) as f:
        for line in f:
            boxIds.append(line)
    matching = find_best_match(boxIds)
    return matching


def main():
    file_name = sys.argv[1]
    result = solve(file_name)
    print('{0}'.format(result))


if __name__ == "__main__":
    main()
