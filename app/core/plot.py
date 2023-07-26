from pathlib import Path

from matplotlib import pyplot as plt

from core.schemas import Result


def draw_plot(data: Result, path: Path) -> None:
    _, ax = plt.subplots(layout="constrained")

    for label, v in data.items():
        keys = []
        values = []
        for k, x in {
            k: x["value"] for k, x in v.items()
        }.items():
            keys.append(k)
            values.append(x)

        ax.plot(
            keys,
            values,
            label=label
        )

    ax.legend()
    ax.set_ylabel("Objects")
    plt.savefig(str(path))
