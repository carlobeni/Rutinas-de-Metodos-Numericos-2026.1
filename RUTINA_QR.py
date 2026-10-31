m, n = M.shape
Q = np.eye(m)
R_mat = M.copy().astype(float)

for i in range(min(m, n)):
    v_x = R_mat[i:, i]
    norm_x = np.linalg.norm(v_x)
    
    if norm_x != 0:
        v = v_x.copy()
        signo = 1 if v_x[0] >= 0 else -1
        v[0] += signo * norm_x
        v = v / np.linalg.norm(v)

        R_mat[i:, i:] -= 2.0 * np.outer(v, np.dot(v, R_mat[i:, i:]))
        Q[:, i:] -= 2.0 * np.outer(np.dot(Q[:, i:], v), v)

c_qr = np.linalg.solve(R_mat[:n, :n], (Q.T @ b)[:n])
print("c_i:", c_qr)
