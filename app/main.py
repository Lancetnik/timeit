from pathlib import Path

from checks.test_true import measure_functions
from core.plot import draw_plot


DIR = Path(__file__).resolve().parent


if __name__ == "__main__":
    data = measure_functions(4)
    draw_plot(data, DIR / "true_condition.png")
