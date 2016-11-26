from OpenGL.GLUT import glutGet, glutInit, glutInitDisplayMode, \
                        glutInitWindowSize, glutMainLoop, \
                        GLUT_SINGLE, GLUT_RGB, GLUT_WINDOW_HEIGHT, GLUT_WINDOW_WIDTH,\
                        glutDestroyWindow,glutGetWindow
class Camera:
	def __init__(self, position=(0, 0, 10), target=(0, 0, 0), up=(0, 1, 0),
				fovy=70, aspect=1, near=0.1, far=1000):
		self.position = position
		self.target = target
		self.up = up
		self.fovy = fovy
		self.aspect = aspect
		self.near = near
		self.far = far
		self.point()
		
	def ViewportSetup(self):
		xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        aspect_ratio = float(xSize) / float(ySize)
        self.aspect = aspect_ratio
		# set up the projection matrix
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glViewport(0, 0, xSize, ySize)
		gluPerspective(self.fovy, self.aspect, self.near, self.far)
		# postcondition: matrix mode is modelview
		glMatrixMode(GL_MODELVIEW)

	def point(self):
		# postcondition: matrix mode is modelview
		# set up the modelview matrix
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(*self.position + self.target + self.up)
		