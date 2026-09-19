from pathlib import Path
import runpy
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SEMESTER = ROOT / "semester7/machine-learning"


def main():
    avocado = runpy.run_path(str(SEMESTER / "lab9/data.py"))
    train, test, labels, expected, classes = avocado["load_data"]()
    assert len(train) == len(labels) and len(test) == len(expected)
    assert np.allclose(train.mean(axis=0), 0, atol=1e-10)
    assert np.isfinite(train).all() and np.isfinite(test).all()
    assert len(classes) == 2
    descent = runpy.run_path(str(SEMESTER / "lab3/main.py"))["gradient_descent"]
    features = np.column_stack((np.ones(5), np.arange(5)))
    theta, history = descent(np.zeros(2), features, 2 + 3 * np.arange(5), 0.1, 1e-12)
    assert np.allclose(theta, [2, 3], atol=1e-4)
    assert history[-1] < history[0]
    project = runpy.run_path(str(SEMESTER / "project/main.py"))
    data = pd.DataFrame(
        {
            "HouseType": ["Apartment", "House"] * 30,
            "Size": ["S", "L"] * 30,
            "Balcony": ["yes", "no", None] * 20,
            "Locality": ["Zurich", "Bern", "Geneva"] * 20,
            "Price": [100.0, 200.0, np.nan] * 20,
        }
    )
    train, test, labels, expected = project["prepare_data"](data)
    assert np.isfinite(train).all() and np.isfinite(test).all()
    assert train.shape[0] == 48 and test.shape[0] == 12
    with tempfile.TemporaryDirectory() as temporary:
        dataset = Path(temporary) / "houses.csv"
        data.to_csv(dataset, index=False)
        result = subprocess.run(
            [
                sys.executable,
                str(SEMESTER / "project/main.py"),
                str(dataset),
                "--skip-neural-network",
            ],
            text=True,
            capture_output=True,
            check=True,
            timeout=60,
        )
        assert result.stdout.count("Accuracy:") == 3, result
    for script in [
        "lab1/matrix_inverse.py",
        "lab1/least_squares.py",
        "lab2/1/scatter_plot.py",
        "lab2/2/function_plot.py",
        "lab2/3/surface_plot.py",
        "lab3/main.py",
        "lab4/main.py",
        "lab5/main.py",
        "lab7/main.py",
        "lab8/main.py",
    ]:
        subprocess.run(
            [sys.executable, str(SEMESTER / script)],
            stdout=subprocess.DEVNULL,
            check=True,
            timeout=60,
        )
    print(
        "Semester 7 checks passed; neural-network training requires TensorFlow or PyTorch"
    )


if __name__ == "__main__":
    main()
