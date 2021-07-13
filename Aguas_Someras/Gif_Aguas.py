import numpy as np
import pylab as pl
import matplotlib.animation as animation

h0 = np.loadtxt('h0.dat')
eta = np.loadtxt('eta.dat')
u = np.loadtxt('u.dat')

x= np.linspace(0, 2000, 101)



# First set up the figure, the axis, and the plot element we want to animate
fig = pl.figure()
ax = pl.axes(xlim=(0, np.max(x)), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
ax.grid()

# initialization function: plot the background of each frame
def init():
    pl.plot(x, -h0, 'k', lw=2)
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    y = eta[i, :]
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
ani = animation.FuncAnimation(fig, animate, range(1, np.size(eta, axis=0)),
                              interval=0.05*1000, blit=True, init_func=init)

#for i in range(0,np.size(eta, axis=0),10):
#    time = ['t=', 2*i, 'segundos']
#    texto = "".join(str(e) for e in time)
#    fofo= pl.figure(i/10)
#    pl.plot(x,-h0, 'k', lw=2)
#    pl.ylim([-2,2])
#    pl.plot(x,eta[i,:])
#    pl.text(80,1.5,texto)
#    new_frame= fofo
#    frames.append([new_frame])

#ani = animation.ArtistAnimation(fig, frames, renderer=fig.canvas.get_renderer())

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame

ani.save('Aguas_Someras.gif', dpi=80, writer='imagemagick')

pl.show()
