from OpenGL.GL import glMatrixMode,GL_MODELVIEW,GL_PROJECTION,glLoadIdentity,\
glViewport
from OpenGL.GLU import gluPerspective, gluUnProject, gluLookAt
from OpenGL.GLUT import glutGet, glutInit, glutInitDisplayMode, \
                        glutInitWindowSize, glutMainLoop, \
                        GLUT_SINGLE, GLUT_RGB, GLUT_WINDOW_HEIGHT, GLUT_WINDOW_WIDTH,\
                        glutDestroyWindow,glutGetWindow
from IPython import embed
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
		self.relvec = (0,-3,-5);
		self.CameraMode = 'LookAt'
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

	def follow(self):
		# embed()
		self.position = (self.target[0] + self.relvec[0],
			self.target[1] + self.relvec[1],
			self.target[2] + self.relvec[2])

	def point(self):
		# postcondition: matrix mode is modelview
		# set up the modelview matrix
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(*self.position + self.target + self.up)
