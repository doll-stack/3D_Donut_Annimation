import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Configuration
WIDTH, HEIGHT = 800, 600
R, r = 5, 2.5       # Major and minor radii
NUM_POINTS = 120     # Density of the ring

def draw_torus(rotation_angle):
    glPointSize(2)  # Make particles look like stars/glow points
    glBegin(GL_POINTS)

    
    # Generate points using parametric equations
    for theta in np.linspace(0, 2 * np.pi, NUM_POINTS):
        for phi in np.linspace(0, 2 * np.pi, NUM_POINTS):
            # The Torus Math
            x = (R + r * np.cos(theta)) * np.cos(phi)
            y = (R + r * np.cos(theta)) * np.sin(phi)
            z = r * np.sin(theta)
            
            # Color effect: Slight gradient based on Z-depth
            brightness = (z + r) / (2 * r) 
            glColor3f(0.1, 0.7 * brightness + 0.3, 1.0) 
            
            glVertex3f(x, y, z)
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Python 3D Particle Donut")

    # Initialize 3D Perspective
    gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -18) # Move camera back to see the whole donut

    clock = pygame.time.Clock()
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Prepare the frame
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        
        # Apply Rotations (X, Y, and Z axes)
        glRotatef(angle, 1, 0.5, 0.2)
        
        draw_torus(angle)
        
        glPopMatrix()
        pygame.display.flip()
        
        angle += 1 # Speed of rotation
        clock.tick()

if __name__ == "__main__":
    main()
