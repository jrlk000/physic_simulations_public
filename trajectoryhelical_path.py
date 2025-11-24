"""Task 1: plot movement of fly"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Physical constants / parameters
G=9.81 #[m/s²]

def compute_trajectory(time: np.ndarray, radius1: float, radius2: float, omega: float, g: float = G,factor: float = 1/8) -> np.ndarray:
    """
    Compute 3D trajectory as an (N, 3) array.
    Columns: x(t), y(t), z(t).
    """
    r_t=np.empty((len(time), 3))
    r_t[:, 0] = radius1 * np.cos(omega * time)  # x_t
    r_t[:, 1] = radius2 * np.sin(omega * time)  # y_t
    r_t[:, 2] = (-g*factor) * time ** 2
    return r_t

def plot_trajectory(positions: np.ndarray) ->None:
    """
    Plot 3D trajectory
    :param positions: (N, 3) array of positions x, y, z in dimension[m]
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d", elev=30, azim=45)

    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], linewidth=0.7)

    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_zlabel("z [m]")
    ax.set_title("3D trajectory")

    #_set_equal_aspect_3d(ax) #optional aid methode

    plt.tight_layout()
    # Save as PDF in current working directory
    #plt.savefig("trajectory(r1!=r2).pdf")
    plt.show()

if __name__== "__main__":
    #given values
    radius = 1e-1#[m]
    omega = 1#[Hz] ~angle velocity
    #n full orbits
    n=4
    t_start=0.0
    t_end=n*(2*np.pi/omega)
    num_steps=200
    time_steps=np.linspace(t_start, t_end, num_steps)
    #compute and plot movement (r1=r2)
    #plot_trajectory(compute_trajectory(time_steps, radius, radius, omega))
    #compute and plot movement (10*r1=r2) 1[E]
    # -> elliptische Schraubenbahn wirkt wegen der verschiedenen Skalierung der x- und y-Achse aber noch kreisförmig
    plot_trajectory(compute_trajectory(time_steps, radius/4, radius, omega))