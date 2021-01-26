import time
import numpy as np
from maps import array
from maps import hash
from maps import BST
from maps import balancedBST


def get_map(s, max_n):
    if s == 'Array':
        return array.ArrayMap()
    elif s == 'Hash':
        return hash.HashMap(max_n // 10)
    elif s == 'BST':
        return BST.BSTMap()
    else:
        return balancedBST.BalancedBSTMap()


def get_op(map_type, s):
    if s == 'put':
        return map_type.put
    elif s == 'delete':
        return map_type.delete
    elif s == 'contains':
        return map_type.contains
    else:
        return map_type.get


def run(config, max_n, step_size):
    data = {}
    data['Randomly Ordered Keys'] = []
    data['Sorted Keys'] = []

    for i in range(step_size, max_n + 1, step_size):
        data['Randomly Ordered Keys'].append(np.random.permutation(i))  # slumpad ordning
        data['Sorted Keys'].append(np.arange(i))  # stigande ordning

    results = {}

    for map in config['maps']:
        results[map] = {}
        map_type = get_map(map, max_n)

        for key in data:
            results[map][key] = {}

            for init_op_list in config['operations']:
                results[map][key][init_op_list] = []

            for data_list in data[key]:
                if map == 'BST' and len(data_list) > 997:  # Recursion depth handling for BST.
                    break

                for op in config['operations']:
                    map_op = get_op(map_type, op)

                    start = time.time()
                    for j in data_list:
                        map_op(j)
                    end = time.time()
                    elapsed_time = end - start
                    results[map][key][op].append({"n": len(data_list), "time": elapsed_time})

    return results
