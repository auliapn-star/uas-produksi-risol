from scipy.optimize import linprog

def optimize_risol(c1, c2, A, b):
    # Koefisien fungsi objektif (maksimalkan → gunakan tanda negatif)
    c = [-c1, -c2]  

    # Menyelesaikan optimasi linier
    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    if res.success:
        x_opt, y_opt = res.x
        total_profit = c1 * x_opt + c2 * y_opt
        return x_opt, y_opt, total_profit
    else:
        return None, None, None
