## Raw Data

The official Iris dataset is publicly available from the **UCI Machine Learning Repository**:

**Dataset:** Iris
**UCI Dataset ID:** 53
**Source:** https://archive.ics.uci.edu/dataset/53/iris

The original dataset contains **150 observations**, **4 numerical features**, and **3 Iris species**.

For reproducibility, the analysis script loads the Iris dataset through **scikit-learn**, so users do not need to manually download and store the original raw dataset.

> **Data attribution:** The Iris dataset is attributed to the UCI Machine Learning Repository and its original authors.

### Reproducibility

The project intentionally creates a working copy of the dataset during the cleaning demonstration. Controlled missing values and duplicate records are introduced into this working copy to demonstrate the data-cleaning workflow.

The original UCI dataset remains unchanged.
