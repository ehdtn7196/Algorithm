def create_circular_array(N):
    inner = [i for i in range(1, N+1)]
    outer = [i for i in range(N+1, 2*N+1)]
    return (inner, outer)

def find_adjacent_numbers_v2(circular_array, target):
    inner, outer = circular_array
    N = len(inner)
    adjacent_numbers = []

    if target in inner:
        index = inner.index(target)
        adjacent_numbers.extend([inner[(index - 1) % N], inner[(index + 1) % N], outer[index]])
    else:
        index = outer.index(target)
        adjacent_numbers.extend([outer[(index - 1) % N], outer[(index + 1) % N], inner[index]])

    return adjacent_numbers

def create_numbered_dict(N):
    numbered_dict = {i: [] for i in range(1, 2*N + 1)}
    return numbered_dict

def find_adjacent_values(circular_array, numbered_dict, target):
    adjacent_numbers = find_adjacent_numbers_v2(circular_array, target)
    adjacent_values = [numbered_dict[i][0] for i in adjacent_numbers]
    return adjacent_values

def remove_and_count_merged_lists(N, W, numbered_dict, circular_array):
    merged_count = 0
    used = set()
    for i in range(1, 2 * N + 1):
        if i not in used:
            adjacent_numbers = find_adjacent_numbers_v2(circular_array, i)
            adjacent_values = find_adjacent_values(circular_array, numbered_dict, i)
            for j, value in enumerate(adjacent_values):
                if sum([numbered_dict[i][0], value]) <= W:
                    if adjacent_numbers[j] not in used:
                        merged_count += 1
                        used.add(i)
                        used.add(adjacent_numbers[j])
                        break
    return 2 * N - merged_count


T = int(input())
for _ in range(T):
    N, W = map(int, input().split())

    if 1 <= N <= 10000 and 1 <= W <= 10000:

        circular_array = create_circular_array(N)

        numbered_dict = create_numbered_dict(N)

        inner_values = list(map(int, input().split()))
        outer_values = list(map(int, input().split()))

        for i in range(1, N + 1):
            numbered_dict[i].append(inner_values[i - 1])
            numbered_dict[i + N].append(outer_values[i - 1])

        remaining_lists = remove_and_count_merged_lists(N, W, numbered_dict, circular_array)
        print(remaining_lists)