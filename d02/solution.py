from collections import Counter, defaultdict

from functools import reduce


def compute_checksum(box_ids):
    box_counters = defaultdict(int)

    for box_id in box_ids:
        found = [v for k, v in Counter(list(box_id)).most_common()
                 if v in (2, 3)]
        found_set = set(found)
        if not any(found):
            continue

        if len(found_set) == 1:
            box_counters[found[0]] += 1
        elif len(found_set) == 2:
            for num in found_set:
                box_counters[num] += 1

    checksum = reduce(lambda x, y: x * y, box_counters.values())
    return checksum


def compare_box_ids(box_id_a, box_id_b):
    if box_id_a == box_id_b or len(box_id_a) != len(box_id_b):
        return False

    found_count, found_index = 0, None

    for i in range(len(box_id_a) - 1):
        if box_id_a[i] != box_id_b[i]:
            found_count += 1
            found_index = i
            if found_count > 2:
                return None

    if found_count == 1:
        return found_index
    else:
        return None


def find_correct_box_id(box_ids):
    for box_id_a in box_ids:
        for box_id_b in box_ids:
            found_idx = compare_box_ids(box_id_a, box_id_b)
            if found_idx:
                result = [i for idx, i in enumerate(box_id_a)
                          if idx != found_idx]
                return ''.join(result)
    return None


def main():
    # Part 1
    box_ids = [l.strip() for l in open('input.txt').readlines()]
    checksum = compute_checksum(box_ids)
    print(f'Checksum : {checksum:,}')

    # Part 2
    correct_box_ids = find_correct_box_id(box_ids)
    print(f'Correct Box IDs: {correct_box_ids}')


if __name__ == '__main__':
    main()
