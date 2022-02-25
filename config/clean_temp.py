from utils.jsonio import JsonIO


def main():
    data = JsonIO("temp.json")
    data['last_level'] = 1
    data['unlocked_levels'] = [1]


if __name__ == '__main__':
    main()
