from d02.solution import compare_box_ids, compute_checksum, find_correct_box_id


def test_part_a():
    box_ids = [
        'abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'
    ]

    assert compute_checksum(box_ids) == 12


def test_part_b():
    box_ids = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz'
    ]

    assert compare_box_ids('fghij', 'fguij') == 2
    assert compare_box_ids('abcde', 'fguij') is None
    assert find_correct_box_id(box_ids) == 'fgij'
