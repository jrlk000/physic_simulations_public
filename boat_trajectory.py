"""class visualizes the movement of a boat in a river with constant stream"""
import matplotlib as mpl
import numpy as np
import math as m
import matplotlib.pyplot as plt
import matplotlib.animation

def compute_movement(s_b0: (float, float), s_f: (float, float), v_river: (float, float), abs_v_boat:float)->[float]:
	"""
	computes the velocity and movement vector of the moving object
	:return:
	"""
	#start conditions
	dt=0.1
	v_river = np.array([[v_river[0], v_river[1]]])
	s_b_t = np.ndarray([s_b0[0], s_b0[1]])
	s_f_t= np.ndarray([s_f[0], s_f[1]]) #constant
	v_b_t = np.ndarray([[0, 0]])
	while True:
		#cuurently it is possible thet the boat loops through the finish line in a ever proceeding loop
		#but at the moment no solution (solutions: adjustment of speed so it gets smaller if it approaches the goal)
		distance_boat_finish = s_f_t-s_b_t
		distance_boat_finish_norm = np.linalg.norm(distance_boat_finish)
		if m.isclose(distance_boat_finish_norm, 0):
			break
		#adjust the direction of vector
		v_b_t.append(abs_v_boat * distance_boat_finish/distance_boat_finish_norm - v_river)
		#construct the movement of the boat and the finish line
		s_b_t.append(s_b_t[-1]+dt*v_b_t[-1])
		s_f_t.append[[s_f_t[0][0], s_f_t[0][1]]] #const pos.
	return s_b_t, s_f_t, v_b_t

#plot
fig = plt.figure
ax = fig.add_subplot(1, 1 ,1)
ax.set_xlabel("$length ~ x$ [m]")
ax.set_ylabel("$breadth ~ y$ [m]")
#
#
ax.grid()
#plot objects
plot_bahn_boat = ax.plot([], [])
plot_boat, = ax.plot([], [], "o", color="blue")
plot_finish, = ax.plot([], [], "o", color="orange")
#create arrows
style = mpl.patches.ArrowStyle.Simple(head_length=6, head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0, 0), (0, 0), color="blue", arrowstyle=style)
#add arrows to plot
ax.add_patch(arrow_v)

#define start conditions for simulation
r0_boat = (10, 7) #[m]
r0_finish = (0, 0) #[m]
v_river = (0, -2) #[m/s]
v_boat_abs = 2 #[m/s]
r_boat, r_finish, v_boat = compute_movement(r0_boat, r0_finish, v_river, v_boat_abs)

#haert of our animation
def update(n):
	"""Update the grafic at tze n-th time step"""
	arrow_v.set_positions(r_boat[n], r_boat[n]+v_boat[n])
	plot_boat.set_data(r_boat[n])
	plot_finish.set_data[r_finish[n]]
	#plot_bahn_boat.set_data(r_boat[:n+1, 0], r_boat[:n+1, 1]) Bedeutung des slicing
	return plot_bahn_boat, plot_boat, plot_finish
ani = mpl.animation.FuncAnimation(fig, update, frames#, interval, #, blit=true)
plt.show()