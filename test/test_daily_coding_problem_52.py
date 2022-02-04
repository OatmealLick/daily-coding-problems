from problems.daily_coding_problem_52 import LeastRecentlyUsedCache


def test_should_remove_least_recently_used_only_set():
    cache_size = 2
    cache = LeastRecentlyUsedCache(cache_size)
    print(cache)
    cache.set(3, "asd")
    print(cache)
    cache.set(4, "ase")
    print(cache)
    cache.set(5, "asx")
    assert len(cache.references.keys()) == cache_size
    assert 4 in cache.references
    assert 5 in cache.references
    assert 3 not in cache.references


def test_should_replace_existing():
    cache_size = 3
    cache = LeastRecentlyUsedCache(cache_size)
    cache.set(3, "asd")
    cache.set(3, "ase")
    assert len(cache.references.keys()) == 1
    assert 3 in cache.references


def test_should_add_while_having_empty_space():
    cache = LeastRecentlyUsedCache(3)
    cache.set(1, "asd")
    cache.set(2, "agd")
    cache.set(3, "ash")
    assert len(cache.references.keys()) == 3


def test_should_put_node_as_most_recent_after_get():
    cache = LeastRecentlyUsedCache(3)
    cache.set(1, "asd")
    cache.set(2, "agd")
    cache.set(3, "ash")
    assert cache.head.key == 3
    assert cache.tail.key == 1
    cache.get(1)
    assert cache.head.key == 1
    assert cache.tail.key == 2
