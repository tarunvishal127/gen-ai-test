import numpy as np
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def normalize_zero_mean_unit_var(X: np.ndarray) -> np.ndarray:
    """
    Normalize each column of X to zero mean and unit variance.
    X: shape (n_samples, n_features)
    Returns: normalized X of same shape.
    """
    if X.ndim != 2:
        logging.error("normalize_zero_mean_unit_var expects 2D array, got shape %s", X.shape)
        raise ValueError("X must be 2D")
    
    logging.info("Normalizing array of shape %s", X.shape)
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    std[std == 0] = 1.0
    X_norm = (X - mean) / std
    return X_norm


def scale_minmax(X: np.ndarray, feature_min: float = 0.0, feature_max: float = 1.0) -> np.ndarray:
    """
    Min-max scale each column of X to [feature_min, feature_max].
    """
    if X.ndim != 2:
        logging.error("scale_minmax expects 2D array, got shape %s", X.shape)
        raise ValueError("X must be 2D")
    
    logging.info("Min-max scaling array of shape %s to [%s, %s]", X.shape, feature_min, feature_max)
    X_min = X.min(axis=0)
    X_max = X.max(axis=0)
    range_ = X_max - X_min
    range_[range_ == 0] = 1.0
    X_scaled = (X - X_min) / range_
    X_scaled = X_scaled * (feature_max - feature_min) + feature_min
    return X_scaled


def pairwise_squared_distances(X: np.ndarray) -> np.ndarray:
    """
    Compute pairwise squared Euclidean distances between rows of X.
    X: shape (n_samples, n_features)
    Returns: D of shape (n_samples, n_samples), where
             D[i, j] = ||X[i] - X[j]||^2
    """
    if X.ndim != 2:
        logging.error("pairwise_squared_distances expects 2D array, got shape %s", X.shape)
        raise ValueError("X must be 2D")
    
    logging.info("Computing pairwise squared distances for array of shape %s", X.shape)
    norms = np.sum(X**2, axis=1)
    D = norms[:, None] + norms[None, :] - 2 * (X @ X.T)
    D = np.maximum(D, 0.0)
    return D
