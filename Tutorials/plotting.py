
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def diverging_bars(y, x, cmap='coolwarm'):
    cmap = matplotlib.cm.get_cmap(cmap)
    
    idx_zero = np.where(x > 0)[0][0]
    colors = np.r_[
        cmap(np.linspace(0, 0.5, idx_zero)),
        cmap(np.linspace(0.5, 1, y.shape[0] - idx_zero))
    ]

    plt.hlines(y, xmin=0, xmax=x, color=colors, lw=10)
