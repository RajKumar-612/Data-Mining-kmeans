# K-Means Clustering with SSE Plot

This project implements the K-Means clustering algorithm and plots the Sum of Squared Errors (SSE) for different values of K to help determine the optimal number of clusters.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. Download the project files and place them in your desired directory.

2. Navigate to the project directory:
    ```sh
    cd /path/to/your/project
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your data file in text format. Ensure the file is a space-separated values file where the last column represents the label which will be ignored.
2. Run the script with the path to your data file as an argument:
    ```sh
    python main.py /path/to/your/datafile.txt
    ```
3. The script will perform K-Means clustering for K values ranging from 2 to 10, print the SSE for each K, and plot the SSE against different values of K.


- **main.py**: Main script for performing K-Means clustering and plotting SSE.
- **requirements.txt**: List of required Python packages.
- **README.md**: This file.

## How It Works

1. **Initialization**:
    - Randomly initialize cluster centroids for a given K.

2. **Assign Points to Clusters**:
    - Calculate the Euclidean distance from each data point to each centroid.
    - Assign each data point to the nearest centroid.

3. **Update Cluster Centers**:
    - Calculate the mean of the data points in each cluster to get the new centroids.

4. **Calculate SSE (Sum of Squared Errors)**:
    - Compute the SSE for each K to measure the compactness of the clusters.

5. **Plotting**:
    - Plot the SSE values against different values of K to visualize the "elbow" point for optimal K.

## Dependencies

- Python 3.x
- numpy
- matplotlib

Install dependencies using:
```sh
pip install -r requirements.txt


