# GravitySim
My first coding project, just for fun! It's written in Python, and uses the standard Tkinter graphics module. It's an interactive gravitational 3-body simulator, originally intended to be a simple calculation of trajectories and demonstration of chaotic systems for a computational physics class.

It uses the Euler-Cromer method to calculate the velocity and position of 3 different bodies based on the forces acting on each body due to the other 2 bodies. The Euler-Cromer method conserves the total momentum of the system regardless of how large the timestep is, it's also not very computationally expensive (looking at you, Runge-Kutta) and thus it's a great choice for a program that must calculate the trajectories in real time, on the fly.

# Program flow
- The state of the 3 body system is updated as fast as your CPU will allow, but is separate from the state of the screen. The physics globals are changing at something like 50,000 times per second, while the graphics only update at 120 times per second.
- Tests speed of user's cpu with speedtest(), which computes what variable 'refreshscale' will give 120 frames per second
- speedtest() finishes, then triggers car(), which is the interactivity environment without gravity turned on
- car() runs until start button is clicked, which triggers gameon()
- gameon() triggers Euler-Cromer calculations and runs until stop button is clicked (which triggers car())

- updatescreen() runs inside of both car() and gameon(). Runs at 120 Hz. Draws the bodies to the screen at the location of the global variables r1, r2, r3.

## Screenshot

![screenshot](https://cloud.githubusercontent.com/assets/18639528/14873539/75ba35c0-0cbd-11e6-85a2-75c36d3a1668.png)

# Instructions
Left-click on a circle and drag it to where ever you'd like. Right click and drag to set the velocity. Enter desired mass in the upper right text box. Click start to view the trajectories, stop to pause, and reset to return to default. The speed up and slow down buttons control viewing speed. 

