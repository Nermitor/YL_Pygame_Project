from utils.jsonio import JsonIO


def main():
    """Очищает временные данные"""
    data = JsonIO("temp.json")
    data['last_level'] = 1
    data['unlocked_levels'] = [1]
    data['best_time'] = {}


if __name__ == '__main__':
    main()
