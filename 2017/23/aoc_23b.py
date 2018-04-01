from math import sqrt


def main():
    b = 108400
    c = 108400 + 17000
    h = 0
    while b <= c:
        d = 2
        d_max = sqrt(b)
        while d <= d_max:
            if b % d == 0:
                h += 1
                break
            d += 1

        b += 17

    print('{0}'.format(h))


if __name__ == "__main__":
    main()
