from main import MattQueueLink, MattQueueLinkX2, MattStackArrAll

if __name__ == "__main__":
    # PERFORMANCE COMPARISON
    import time
    import matplotlib.pyplot as plt

    models = [
        ("StackArrAll", MattStackArrAll(object)),
        ("QueueLink", MattQueueLink()),
        ("QueueLinkX2", MattQueueLinkX2()),
    ]

    num = 10  # _000_000  # ten million
    check_interval = num // 5  # record every 10%

    results = {}
    for name, ms in models:
        times = [0]
        vals = [0]

        start = time.time()
        last = start
        # times.append(start)

        for i in range(1, num + 1):
            if hasattr(ms, "push"):
                ms.push(1)
            else:
                ms.enqueue(1)

            if i % check_interval == 0:
                now = time.time()
                interval = now - last
                print(f"{name}: interval {interval:.3f}s at i={i}")
                last = now
                times.append(now - start)  # time since start
                vals.append(i)

        total = time.time() - start
        print(f"{name}: total time {total:.3f}s")
        results[name] = (vals, times)

    for name, (vals, times) in results.items():
        plt.plot(vals, times, label=name)
    plt.title("Performance Comparison: Push/Enqueue Operations")
    plt.xlabel("Number of Operations")
    plt.ylabel("Cumulative Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
