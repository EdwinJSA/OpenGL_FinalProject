import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def load_texture(image):
    # Load a texture from an image file.
    # Args:
    #     image (str): The path to the image file.
    # Returns:
    #     int: The ID of the generated texture.
    # This function loads an image file using Pygame's image loading functionality. It then converts the image surface
    # to a string of RGBA data. The width and height of the image surface are obtained.
    # Next, a texture ID is generated using OpenGL's `glGenTextures` function. The texture is bound using
    # `glBindTexture` with the generated texture ID. The texture parameters are set using `glTexParameteri` to enable
    # linear filtering.
    # The image data is loaded into the texture using `glTexImage2D` with the specified parameters.
    # Finally, the generated texture ID is returned.
    texture_surface = pygame.image.load(image)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", True)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    
    return texture_id

# Inicialización de Pygame y OpenGL
def init():

    # Initializes the Pygame and OpenGL libraries.
    # This function initializes the Pygame library and sets up the display window for OpenGL rendering. It creates a window with a specified width and height of 800x600 pixels. The window is set to use double buffering and OpenGL. The `glEnable` function is called to enable 2D texturing.
    # Parameters:
    #     None
    # Returns:
    #     None

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_TEXTURE_2D)

def draw_background(texture_id):
    # Draws a textured quad as the background using the given texture ID.
    # Args:
    #     texture_id (int): The ID of the texture to be used for the quad.
    # Returns:
    #     None
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(-1, -1)
    glTexCoord2f(1, 0)
    glVertex2f(1, -1)
    glTexCoord2f(1, 1)
    glVertex2f(1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(-1, 1)
    glEnd()
    
def draw_cubo():
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_QUADS)  # Comienza a dibujar un cuadrado
    glVertex2f(-0.5, -0.5)  # Vértice inferior izquierdo
    glVertex2f(0.5, -0.5)   # Vértice inferior derecho
    glVertex2f(0.5, 0.5)    # Vértice superior derecho
    glVertex2f(-0.5, 0.5)   # Vértice superior izquierdo
    glEnd()  # Termina de dibujar el cuadrado


def main():
    # The main function that initializes the Pygame and OpenGL libraries, sets up the display window for OpenGL rendering, and continuously renders the background texture.
    # This function does the following:
    # - Calls the `init()` function to initialize the Pygame and OpenGL libraries.
    # - Loads the background texture using the `load_texture()` function, passing the path to the image file as an argument.
    # - Enters an infinite loop to continuously render the background.
    # - Handles the events received by the Pygame window, exiting the loop and quitting the Pygame and OpenGL libraries if a QUIT event is received.
    # - Clears the color and depth buffers using `glClear()`.
    # - Calls the `draw_background()` function to render the background texture.
    # - Flips the display using `pygame.display.flip()`.
    # - Waits for 10 milliseconds using `pygame.time.wait()`.
    # Parameters:
    #   None
    # Returns:
    #   None
    init()
    background_texture = load_texture('./resource/fondo.png')  # Cambia esto a la ruta de tu imagen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_background(background_texture)
        draw_cubo()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()