#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
from functools import reduce

output_list = [[] for _ in range(5)]
path_set = [[] for _ in range(5)]


def sort_list(path):
    sorted_path = path[path.index(min(path)):] + path[:path.index(min(path))]
    return sorted_path


def main():
    input_array = np.loadtxt('./test_data.txt', dtype=np.uint32, delimiter=',')
    path_dict = {}
    for i in range(len(input_array)):
        if path_dict.__contains__(input_array[i][0]):
            path_dict[input_array[i][0]].append(input_array[i][1])
        else:
            path_dict[input_array[i][0]] = [input_array[i][1]]

    for local_account_id in path_dict.keys():
        global path_set
        temp_queue = [[local_account_id]]
        while temp_queue:
            path = temp_queue.pop(0)
            end_id = path[-1]
            if len(path) > 2 and end_id in path[:-1] and path[-3] != end_id:
                output_path = path[path.index(end_id):-1]
                path_length_index = len(output_path)-3
                if set(output_path) not in path_set[path_length_index]:
                    output_list[path_length_index].append(sort_list(output_path))
                    path_set[path_length_index].append(set(output_path))
            elif len(path) <= 7:
                for peer_account_id in path_dict.get(end_id, []):
                    new_path = []
                    new_path += path
                    new_path.append(peer_account_id)
                    temp_queue.append(new_path)
            else:
                continue
    print(reduce(lambda x, y: x+y, map(len, path_set)))
    for path_list in output_list:
        path_list = sorted(path_list, key=lambda x: (x[:]))
        for path in path_list:
            print((''.join(str(path)))[1:-1])


if __name__ == '__main__':
    main()
