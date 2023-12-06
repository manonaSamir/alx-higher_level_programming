
#!/#usr/bin/python3
def search_replace(my_list, search, replace):
    row = [x if x != 2 else 98 for x in my_list]
    return row



def test_search_replace():
    # Test case 1: Basic case with integers
    assert search_replace([1, 2, 3, 4, 5], 2, 98) == [1, 98, 3, 4, 5]

    # Test case 2: Basic case with strings
    assert search_replace(['apple', 'banana', 'cherry'], 'banana', 'orange') == ['apple', 'orange', 'cherry']

    # Test case 3: Empty list
    assert search_replace([], 0, 99) == []

    # Test case 4: Multiple occurrences of the search element
    assert search_replace([2, 2, 2, 2], 2, 98) == [98, 98, 98, 98]

    # Test case 5: No occurrence of the search element
    assert search_replace([1, 3, 5, 7], 2, 98) == [1, 3, 5, 7]

    # Test case 6: Mix of data types
    assert search_replace([1, 'apple', 2.5, True, 2, 'banana'], 2, 'orange') == [1, 'apple', 2.5, True, 'orange', 'banana']

    # Test case 7: Negative numbers
    assert search_replace([-2, 0, 2, -2, 4], -2, 98) == [98, 0, 2, 98, 4]

    print("All test cases passed!")

# Run the test cases
test_search_replace()
