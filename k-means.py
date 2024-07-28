import sys
import numpy as np
import matplotlib.pyplot as plt
import random

RANDOM_SEED = 1
random.seed(RANDOM_SEED)


def initialize_centroids(k, rows, data_matrix):
    centroids = []
    for _ in range(k):
        centroid_index = random.randint(1, rows)
        centroids.append(data_matrix[centroid_index])
    return centroids


def assign_points_to_clusters(data_matrix, centroids):
    distances = np.sqrt(((data_matrix[:, np.newaxis] - centroids) ** 2).sum(axis=2))
    cluster_ids = np.argmin(distances, axis=1)
    clusters = [np.where(cluster_ids == i)[0] for i in range(len(centroids))]
    return clusters


def update_cluster_centers(clusters, data_matrix):
    cluster_means = [np.mean(data_matrix[cluster], axis=0) for cluster in clusters]
    return np.array(cluster_means)


def calculate_sse(clusters, centroids, data_matrix):
    sse = 0
    for i, cluster in enumerate(clusters):
        cluster_center = centroids[i]
        for j in cluster:
            sse += np.sqrt(np.sum((data_matrix[j] - cluster_center) ** 2))
    return sse


def plotGraph(sse_errors):
    # Plot the SSE values against different values of K
    plt.plot(range(2, 11), sse_errors, "bo-")
    plt.title("SSE vs K Chart")
    plt.ylabel("SSE")
    plt.xlabel("K")
    plt.show()


if __name__ == "__main__":
    txt_File = sys.argv[1]
    data_matrix = np.loadtxt(txt_File)
    data_matrix = data_matrix[:, :-1]

    sse_errors = []

    for k in range(2, 11):
        rows, _ = data_matrix.shape

        centroids = initialize_centroids(k, rows, data_matrix)

        for _ in range(20):
            clusters = assign_points_to_clusters(data_matrix, centroids)
            centroids = update_cluster_centers(clusters, data_matrix)

        sse = calculate_sse(clusters, centroids, data_matrix)
        sse_errors.append(sse)
        print(f"For k = {k} After 20 iterations: SSE error = {sse:.4f}")
    plotGraph(sse_errors)
