"""
Week 1: Data Acquisition, Cleaning and Exploratory Analysis

This script reproduces the main analysis documented in the Word report.
The Iris dataset is loaded through scikit-learn's public representation.

The original Iris dataset has no missing values. Five missing values and
three additional duplicate records are introduced into a working copy
solely to demonstrate data-cleaning techniques required by the assignment.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "reports" / "figures"
PROCESSED_DIR = ROOT / "data" / "processed"

FIG_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def acquire_data() -> pd.DataFrame:
    """Load the public Iris dataset and return a standardized DataFrame."""
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()

    df.columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "target",
    ]

    df["species"] = df["target"].map(dict(enumerate(iris.target_names)))
    return df.drop(columns="target")


def simulate_quality_issues(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a controlled working copy containing missing values and
    additional duplicates for cleaning practice.
    """
    df = df.copy()

    missing_positions = {
        ("sepal_length", 5),
        ("sepal_width", 35),
        ("petal_length", 75),
        ("petal_width", 105),
        ("sepal_length", 125),
    }

    for column, index in missing_positions:
        df.loc[index, column] = np.nan

    # Three intentionally added duplicate records.
    df = pd.concat([df, df.iloc[[10, 60, 120]]], ignore_index=True)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Impute missing numeric values, remove duplicates, and standardize types."""
    numeric_cols = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]

    for column in numeric_cols:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df[column] = df[column].fillna(df[column].median())

    df = df.drop_duplicates().reset_index(drop=True)
    df["species"] = df["species"].astype("category")

    return df


def create_visualizations(df_raw: pd.DataFrame, df_clean: pd.DataFrame) -> None:
    """Generate and save four EDA visualizations."""

    numeric_cols = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]

    # 1. Missing values
    before = df_raw[numeric_cols].isna().sum()
    after = df_clean[numeric_cols].isna().sum()

    x = np.arange(len(numeric_cols))
    width = 0.36

    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.bar(x - width / 2, before.values, width, label="Before cleaning")
    ax.bar(x + width / 2, after.values, width, label="After cleaning")
    ax.set_xticks(x)
    ax.set_xticklabels(
        [c.replace("_", " ").title() for c in numeric_cols],
        rotation=20,
    )
    ax.set_ylabel("Missing values")
    ax.set_title("Missing Values Before vs. After Cleaning")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "01_missing_values.png", dpi=180)
    plt.close(fig)

    # 2. Class distribution
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    df_clean["species"].value_counts().sort_index().plot(kind="bar", ax=ax)
    ax.set_title("Iris Class Distribution")
    ax.set_xlabel("Species")
    ax.set_ylabel("Number of observations")
    ax.tick_params(axis="x", rotation=0)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "02_class_distribution.png", dpi=180)
    plt.close(fig)

    # 3. Petal scatter plot
    fig, ax = plt.subplots(figsize=(7.4, 5.2))
    for species in df_clean["species"].cat.categories:
        subset = df_clean[df_clean["species"] == species]
        ax.scatter(
            subset["petal_length"],
            subset["petal_width"],
            label=str(species),
            alpha=0.75,
        )

    ax.set_title("Petal Length vs. Petal Width")
    ax.set_xlabel("Petal length (cm)")
    ax.set_ylabel("Petal width (cm)")
    ax.legend(title="Species")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "03_petal_scatter.png", dpi=180)
    plt.close(fig)

    # 4. Correlation heatmap
    correlation = df_clean[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(7, 5.5))
    sns.heatmap(correlation, annot=True, fmt=".2f", square=True, ax=ax)
    ax.set_title("Correlation Matrix of Numeric Features")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "04_correlation_heatmap.png", dpi=180)
    plt.close(fig)


def main() -> None:
    df_source = acquire_data()
    df_working = simulate_quality_issues(df_source)
    df_clean = clean_data(df_working)

    print("=== Week 1 Iris EDA ===")
    print(f"Source shape:  {df_source.shape}")
    print(f"Working shape: {df_working.shape}")
    print(f"Clean shape:   {df_clean.shape}")
    print()
    print("Missing values before cleaning:")
    print(df_working.isna().sum())
    print()
    print(f"Duplicate rows before cleaning: {df_working.duplicated().sum()}")
    print(f"Duplicate rows after cleaning:  {df_clean.duplicated().sum()}")
    print()
    print("Summary statistics:")
    print(df_clean.describe())

    df_clean.to_csv(PROCESSED_DIR / "iris_cleaned.csv", index=False)
    create_visualizations(df_working, df_clean)

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
