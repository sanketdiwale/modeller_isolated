import numpy

def translation(displacement):
    t = numpy.identity(4)
    t[0, 3] = displacement[0]
    t[1, 3] = displacement[1]
    t[2, 3] = displacement[2]
    return t


def scaling(scale):
    s = numpy.identity(4)
    s[0, 0] = scale[0]
    s[1, 1] = scale[1]
    s[2, 2] = scale[2]
    s[3, 3] = 1
    return s

def getDCM(q):
    '''provides DCM for quarternion'''
    return numpy.vstack((
            numpy.hstack((q[0]**2+q[1]**2-q[2]**2-q[3]**2,
                            2.*(q[1]*q[2]-q[3]*q[0]),2.*(q[1]*q[3]+q[2]*q[0]))),
            numpy.hstack((2.*(q[1]*q[2]+q[3]*q[0]),
                            q[0]**2-q[1]**2+q[2]**2-q[3]**2, 
                            2.*(q[2]*q[3]-q[1]*q[0]))),
            numpy.hstack((2.*(q[1]*q[3]-q[2]*q[0]),
                            2.*(q[2]*q[3]+q[1]*q[0]),
                            q[0]**2-q[1]**2-q[2]**2+q[3]**2))
            ));

def rotation(q):
    q = q/numpy.linalg.norm(q) # normalize for safety
    return numpy.array(getDCM(q))

def GraphicstoGroundRot():
    return numpy.array([[1.,0.,0.],[0,0,-1],[0,1,0]])

def GraphicstoGround(p):
    return (p[0],-p[2],p[1])

def GroundtoGraphics(p):
    return p[0],p[2],-p[1]

