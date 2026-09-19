def sort_dict(mapping):
    sorted_by_priority = sorted(mapping.items(), key=lambda entry: entry[1])
    converted_dict = dict(sorted_by_priority)

    return converted_dict


def output(response):
    for completion in response:
        print(completion)


def solver(count):
    time_dict = {}
    length_dict = {}
    current_time = 0

    for i in range(count):
        line = input()

        data = list(map(int, line.split()))
        time_dict[i] = data[0]
        length_dict[i] = data[1]

    response = [0] * (count + 1)
    sorted_time_dict = sort_dict(time_dict)

    for index in sorted_time_dict:
        if not current_time or current_time < sorted_time_dict[index]:
            current_time = sorted_time_dict[index]

        current_time += length_dict[index]
        response[index] = current_time

    response[count] = current_time

    output(response)


if __name__ == "__main__":
    count = int(input())
    solver(count)
