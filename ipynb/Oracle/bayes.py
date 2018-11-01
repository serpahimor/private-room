def bayes(z):
    x_tr,t_tr=z[z.columns[1]].as_matrix(),z[z.columns[0]].as_matrix()
    def phi(x, M):
        return x[:,None] ** np.arange(M + 1)
    N=len(z)
    M = N-1
    alpha = 5e-3
    beta = 11.1
    lam = alpha / beta
    phi_x_tr = phi(x_tr, M)
    A_0 = phi_x_tr.T.dot(phi_x_tr) + lam * np.eye(M+1)
    y_0 = t_tr.dot(phi_x_tr)
    coeff = np.linalg.solve(A_0, y_0)[::-1]
    f = np.poly1d(coeff)
    xx = np.linspace(0, 1, 50)
    S = np.linalg.inv(A_0 * beta)
    m_xx = beta * phi(xx, M).dot(S).dot(y_0)
    s_xx = np.sqrt(1 / beta + phi(xx, M).dot(S).dot(phi(xx, M).T).diagonal())
    fig, ax = plt.subplots()
    ax.plot(x_tr, t_tr, 'co')
    ax.plot(xx, f(xx), 'r')
    ax.fill_between(xx, (m_xx-s_xx), (m_xx+s_xx), color="pink")
    plt.show()