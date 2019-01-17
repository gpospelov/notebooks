from matplotlib import pyplot as plt
from matplotlib import colors

def plot_in_logs(data):
    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(10,4))
    im1 = ax1.imshow(data)
    cb = plt.colorbar(im1, ax=ax1, pad=0.025)
    norm=colors.LogNorm(1e1, 1e8)
    im2 = ax2.imshow(data, norm=norm)
    cb = plt.colorbar(im2, ax=ax2, pad=0.025)    
