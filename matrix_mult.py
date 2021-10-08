#This is a template code. Please save it in a proper .py file.
import rtmaps.types
import numpy as np
import rtmaps.core as rt 
import rtmaps.reading_policy 
from rtmaps.base_component import BaseComponent # base class 


# Python class that will be called from RTMaps.
class rtmaps_python(BaseComponent):
    def __init__(self):
        BaseComponent.__init__(self) # call base class constructor

    def Dynamic(self):
        self.add_input("in1", rtmaps.types.MATRIX) # define input
        self.add_input("in2", rtmaps.types.MATRIX) # define input
        self.add_input("in3", rtmaps.types.FLOAT64) # define input
        self.add_input("in4", rtmaps.types.ANY) # define input
        self.add_output("out", rtmaps.types.MATRIX) # define output

# Birth() will be called once at diagram execution startup
    def Birth(self):
        pass

# Core() is called every time you have a new input
    def Core(self):
# definition of the input variables
        ioeltin1 = self.inputs["in1"].ioelt
        ioeltin2 = self.inputs["in2"].ioelt
        ioeltin3 = self.inputs["in3"].ioelt
        ioeltin4 = self.inputs["in4"].ioelt
        matrix1 = ioeltin1.data
        matrix2 = ioeltin2.data
        matrix3 = ioeltin3.data
        matrix4 = ioeltin4.data
# definition of the output variable        
        ioelt_out = rtmaps.types.Ioelt()
        ioelt_out.data = rtmaps.types.Matrix()
        ioelt_out.ts = ioeltin1.ts
# to write X(k+1) = A*X(k) + B*U
    v = 109
    dt = 1
# with A = [1, 0, -v*dt*sin(phi); 0, 1, v*dt*cos(phi); 0, 0, 1]
#    A = np.array([1, 0, -v*dt*sin(ioeltin3)], [0, 1, v*dt*cos(ioeltin3)], [0, 0, 1])
# with B = [cos(phi)*dt, 0; sin(phi)*dt, 0; tan(delta)/l*dt, v*dt/(l*cos^2(delta))]
#    B = np.array([cos(ioeltin3)*dt, 0; sin(ioeltin3)*dt], [tan(ioeltin4)/l*dt, v*dt/(l*cos^2(ioeltin4))])
                ioelt_out.data.matrix_data = matrix1.matrix_data.add(matrix2.matrix_data)  #dot
       
        self.outputs["out"].write(ioelt_out) # and write it to the output

# Death() will be called once at diagram execution shutdown
    def Death(self):
        pass
