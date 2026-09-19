def least_loaded_machine(machine_loads):
    return machine_loads.index(min(machine_loads))


def main():
    m, n = map(int, input().split())
    machine_loads = [0 for i in range(m)]
    tasks = []
    for i in range(n):
        tasks.append(int(input()))
    available_machine = 0
    tasks.sort(reverse=True)
    for task in tasks:
        machine_loads[available_machine] += task
        available_machine = least_loaded_machine(machine_loads)
    print(max(machine_loads))


if __name__ == "__main__":
    main()
