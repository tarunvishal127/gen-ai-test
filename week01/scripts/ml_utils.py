from typing import List, Tuple
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def train_test_split_simple(
    X: List[List[float]],
    y: List[float],
    test_ratio: float = 0.2
) -> Tuple[List[List[float]], List[List[float]], List[float], List[float]]:
    """
    Simple deterministic train/test split.
    
    Uses the first portion as train, last portion as test.
    
    Returns:
        X_train, X_test, y_train, y_test
    """
    n = len(X)
    if n == 0:
        logging.warning("train_test_split_simple called with empty data")
        return [], [], [], []
    
    if len(y) != n:
        logging.error("X and y have different lengths: %d vs %d", n, len(y))
        raise ValueError("X and y must have the same length")
    
    n_test = int(n * test_ratio)
    n_train = n - n_test
    
    logging.info(
        "train_test_split_simple: n=%d, n_train=%d, n_test=%d",
        n, n_train, n_test
    )
    
    X_train = X[:n_train]
    X_test = X[n_train:]
    y_train = y[:n_train]
    y_test = y[n_train:]
    
    return X_train, X_test, y_train, y_test

def mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
    """Compute mean squared error between true and predicted values."""
    if len(y_true) != len(y_pred):
        logging.error("y_true and y_pred length mismatch: %d vs %d", len(y_true), len(y_pred))
        raise ValueError("y_true and y_pred must have the same length")
    
    n = len(y_true)
    mse = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n
    
    logging.info("mean_squared_error computed for %d samples; MSE = %s", n, mse)
    return mse