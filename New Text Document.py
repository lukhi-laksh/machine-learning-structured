import os
import json

BASE_DIR = "machine-learning-structured/01_Math_For_Data_Science"

EMPTY_NOTEBOOK = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Title\n\n",
                "## Introduction\n",
                "## Explanation\n",
                "## Formula\n",
                "## Example\n",
                "## Conclusion\n"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

STRUCTURE = {
    "Statistics/Descriptive": [
        "central_tendency.ipynb",
        "variability.ipynb",
        "shape_skewness.ipynb",
        "percentiles_quantiles.ipynb",
        "frequency_distribution.ipynb",
        "covariance_correlation.ipynb"
    ],
    "Statistics/Inferential": [
        "probability_clt.ipynb",
        "hypothesis_testing.ipynb",
        "z_test.ipynb",
        "t_test.ipynb",
        "chi_square_test.ipynb"
    ],
    "Linear_Algebra": [],
    "Probability": [],
    "Calculus": []
}

def create_notebook(path):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(EMPTY_NOTEBOOK, f, indent=2)

def main():
    for folder, notebooks in STRUCTURE.items():
        full_folder = os.path.join(BASE_DIR, folder)
        os.makedirs(full_folder, exist_ok=True)

        for nb in notebooks:
            create_notebook(os.path.join(full_folder, nb))

    print("✅ Math structure updated successfully")

if __name__ == "__main__":
    main()
