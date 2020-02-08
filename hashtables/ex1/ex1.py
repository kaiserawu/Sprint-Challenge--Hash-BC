#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    first_index = None
    second_index = None

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    
    for i in range(len(weights)):
        second_index = i
        first_index = hash_table_retrieve(ht, limit - weights[i])
        if first_index != None:
            return (first_index, second_index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
