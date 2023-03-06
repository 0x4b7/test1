def custom_filter(some_list):
    res = [i for i in some_list if isinstance(i, int)]
    s = sum([j for j in res if j % 7 == 0])
    return s < 83


def main():
    some_list = [7, 14, 28, 32, 32, 56]

    print(custom_filter(some_list))


if __name__ == '__main__':
    main()
