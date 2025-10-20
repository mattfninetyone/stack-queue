import time

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from main import MattQueueLink, MattQueueLinkX2, MattStackArrAll

"""Performance comparison between different stack and queue implementations."""


def main() -> None:
    NUM_OPERATIONS = 1_000_000
    results = run_performance_tests(NUM_OPERATIONS)
    plot_results(results)


def run_performance_tests(num_operations: int) -> dict[str, tuple[list, list]]:
    models = [
        ("StackArrAll", MattStackArrAll(object)),
        ("QueueLink", MattQueueLink()),
        ("QueueLinkX2", MattQueueLinkX2()),
    ]

    check_interval = num_operations // 5  # record every 10%

    results = {}
    for name, ms in models:
        times = [0]
        vals = [0]

        start = time.time()
        last = start
        # times.append(start)

        for i in range(1, num_operations + 1):
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
    return results


def plot_results(results: dict[str, tuple[list, list]]) -> None:
    colors = ["#FFC267", "#1AA7E9", "#BEB7B7"]
    for (name, (vals, times)), color in zip(results.items(), colors):
        plt.plot(vals, times, label=name, color=color, linewidth=2, alpha=0.8)
    plt.title("Performance Comparison: Push/Enqueue Operations")
    plt.xlabel("Number of Operations")
    ax = plt.gca()
    ax.xaxis.set_major_formatter(
        mticker.FuncFormatter(lambda x, _: f"{x / 1_000_000:.1f}M")
    )
    plt.ylabel("Cumulative Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
