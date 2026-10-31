
def read_matrix(n, m, label):
    print(f"Enter {label} matrix ({n} rows, {m} values each):")
    data = []

    for i in range(n):
        row = list(map(int, input(f"P{i}: ").split()))

        if len(row) != m or any(x < 0 for x in row):
            raise ValueError(
                f"{label}: each row needs {m} non-negative integers"
            )

        data.append(row)

    return data


def need_matrix(maximum, allocation):
    return [
        [maximum[i][j] - allocation[i][j]
         for j in range(len(maximum[0]))]
        for i in range(len(maximum))
    ]


def print_matrix(title, matrix):
    print("\n" + title)

    for i, row in enumerate(matrix):
        print(f"P{i}: " + " ".join(map(str, row)))


def safety_algorithm(allocation, maximum, available, show=True):
    n = len(allocation)
    m = len(available)

    need = need_matrix(maximum, allocation)
    work = available.copy()
    finish = [False] * n
    sequence = []

    if show:
        print_matrix("Need Matrix", need)
        print("\nBanker's Safety Check")
        print("Initial Work:", work)

    while True:
        progress = False

        for i in range(n):
            if not finish[i] and all(
                need[i][j] <= work[j] for j in range(m)
            ):
                if show:
                    print(f"P{i} can finish")

                work = [
                    work[j] + allocation[i][j]
                    for j in range(m)
                ]

                finish[i] = True
                sequence.append(i)
                progress = True

                if show:
                    print(f"After P{i}, Work = {work}")

        if not progress:
            break

    safe = all(finish)

    if show:
        if safe:
            print("\nSAFE STATE")
            print(
                "Safe Sequence:",
                " -> ".join(f"P{i}" for i in sequence)
            )
        else:
            print("\nUNSAFE STATE")
            print(
                "Processes unable to finish:",
                [f"P{i}" for i in range(n) if not finish[i]]
            )

    return safe, sequence, need


def detect_deadlock(allocation, request, available):
    n = len(allocation)
    m = len(available)

    work = available.copy()
    finish = [
        all(x == 0 for x in allocation[i])
        for i in range(n)
    ]

    sequence = []

    print("\nDeadlock Detection")
    print("Initial Work:", work)

    while True:
        progress = False

        for i in range(n):
            if not finish[i] and all(
                request[i][j] <= work[j]
                for j in range(m)
            ):
                print(f"P{i}: Request can be satisfied.")

                work = [
                    work[j] + allocation[i][j]
                    for j in range(m)
                ]

                finish[i] = True
                sequence.append(i)
                print(f"P{i} finishes; Work = {work}")

                progress = True

        if not progress:
            break

    remaining = [
        f"P{i}" for i in range(n) if not finish[i]
    ]

    if remaining:
        print("DEADLOCK DETECTED:", remaining)
    else:
        print("NO DEADLOCK DETECTED")
        print(
            "Completion order:",
            " -> ".join(f"P{i}" for i in sequence) or "None"
        )

    return remaining


def resource_request(pid, request, allocation, maximum, available):
    n = len(allocation)
    m = len(available)

    if pid < 0 or pid >= n:
        print("Invalid process number.")
        return allocation, available

    need = need_matrix(maximum, allocation)

    if any(request[j] > need[pid][j] for j in range(m)):
        print("DENIED: request exceeds remaining Need.")
        return allocation, available

    if any(request[j] > available[j] for j in range(m)):
        print("WAIT: resources are not currently available.")
        return allocation, available

    new_a = [row.copy() for row in allocation]
    new_v = available.copy()

    for j in range(m):
        new_a[pid][j] += request[j]
        new_v[j] -= request[j]

    safe, seq, _ = safety_algorithm(
        new_a, maximum, new_v, show=False
    )

    if safe:
        print("REQUEST GRANTED; system remains safe.")
        print("Safe Sequence:", " -> ".join(f"P{i}" for i in seq))
        return new_a, new_v

    print("REQUEST DENIED; state would become unsafe.")
    return allocation, available


def main():
    print("=" * 55)
    print("DEADLOCK DETECTION & AVOIDANCE SIMULATOR")
    print("Banker's Algorithm + Deadlock Detection")
    print("=" * 55)

    try:
        n = int(input("Number of processes: "))
        m = int(input("Number of resource types: "))

        if n <= 0 or m <= 0:
            raise ValueError("Counts must be positive.")

        allocation = read_matrix(n, m, "Allocation")
        maximum = read_matrix(n, m, "Maximum")

        available = list(map(
            int,
            input(f"Available vector ({m} values): ").split()
        ))

        if len(available) != m or any(x < 0 for x in available):
            raise ValueError("Invalid Available vector.")

        for i in range(n):
            for j in range(m):
                if allocation[i][j] > maximum[i][j]:
                    raise ValueError(
                        f"Allocation exceeds Maximum at P{i}, R{j}."
                    )

        safety_algorithm(allocation, maximum, available)

        print("\nEnter current outstanding Request matrix.")
        request = read_matrix(n, m, "Request")

        detect_deadlock(allocation, request, available)

        choice = input(
            "\nCheck an additional resource request? (y/n): "
        ).strip().lower()

        if choice == "y":
            pid = int(input(f"Process number (0 to {n-1}): "))

            req = list(map(
                int,
                input(f"Request vector ({m} values): ").split()
            ))

            if len(req) != m or any(x < 0 for x in req):
                raise ValueError("Invalid request vector.")

            resource_request(
                pid, req, allocation, maximum, available
            )

    except ValueError as e:
        print("Input Error:", e)


if __name__ == "__main__":
    main()

