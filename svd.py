import numpy as np

def svd_decomposition(X):
    """
    Performs Singular Value Decomposition on matrix X.
    Returns U, Sigma, Vt such that X = U @ Sigma @ Vt
    """
    # full_matrices=False returns the 'economy' SVD which is sufficient for H computation
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    
    return U, s, Vt

def compute_hat_matrix_svd(X):
    """
    Computes the Hat Matrix using the decomposition X = U @ Sigma @ Vt.
    This avoids calculating (X^T X)^-1 directly, which is numerically more stable.
    """
    # 1. Perform SVD: X = U @ Sigma @ Vt
    U, s, Vt = svd_decomposition(X)
    
    # 2. Identify non-zero singular values to determine rank (tolerance for float errors)
    tol = max(X.shape) * np.amax(s) * np.finfo(float).eps
    rank = np.sum(s > tol)
    
    # 3. Construct the Projection Matrix using U columns corresponding to non-zero sigma
    # H = U @ (U^T), but only for the subspace spanned by X
    if rank == 0:
        return np.zeros_like(X)
    
    # Slice U to keep only the first 'rank' columns (the basis of col space)
    U_r = U[:, :rank] 
    
    # Calculate H = U_r @ U_r^T
    # This effectively projects any vector onto the column space of X
    H = U_r @ U_r.T
    
    return H

def verify_hat_matrix(X):
    """
    Verifies the properties: Symmetry, Idempotence (H*H=H), and Projection.
    """
    print("\n--- Verification ---")
    
    # Compute using standard formula for comparison if needed, 
    # but we primarily use SVD method above for stability.
    H = compute_hat_matrix_svd(X)
    
    n_rows, n_cols = H.shape
    
    print(f"Matrix Dimensions: {H.shape}")
    
    # 1. Check Symmetry
    is_symmetric = np.allclose(H, H.T)
    print(f"Is Symmetric (H == H^T): {is_symmetric}")
    
    # 2. Check Idempotence (H * H == H)
    product = H @ H
    is_idempotent = np.allclose(product, H)
    print(f"Is Idempotent (H^2 == H): {is_idempotent}")
    
    # 3. Check Projection on Column Space of X
    # If we project any column of X using H, we should get the same column back.
    # Because X lies entirely within its own column space.
    reconstructed_X = H @ X 
    is_projection_valid = np.allclose(X, reconstructed_X)
    print(f"Projects X onto itself (X == H@X): {is_projection_valid}")

# Example Usage
if __name__ == "__main__":
    # Generate a random matrix (n x p)
    np.random.seed(42)
    n_samples = 50
    n_features = 10
    X = np.random.randn(n_samples, n_features)
    
    print(f"Original Matrix Shape: {X.shape}")
    
    # Perform Decomposition
    U, s, Vt = svd_decomposition(X)
    print("\n--- SVD Results ---")
    print(f"Shape of U: {U.shape}, Sigma (first 5): {s[:5]}")
    
    # Compute Hat Matrix
    H = compute_hat_matrix_svd(X)
    print(f"\nHat Matrix Shape: {H.shape}")
    
    # Verify Properties
    verify_hat_matrix(X)
