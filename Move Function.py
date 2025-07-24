'''
jobs to do:
check movement wont foul endstops (check position of head)
move head (make sure z_min is reached
report new position

'''

from standard_fuctions import g_code
safe_z_height = str(255) # Safe height for the head to move around at without the poker hitting bottles


def abs_move(url,type,x,y,z):
    if type == "rel":
        g_code(url,"G91") # Sets extruder mode to relative
        g_code(url,"m82") # Keeps the extruder in absolute mode
    if x==0 and y==0:
        command = "G01" + "x0" + "y0" +"z" + z
        g_code(url,command)

    else:
        g_code(url,"G01 Z"+safe_z_height)
        g_code(url,"G01" + "x"+ x + "y" + y +"z" + z)

    g_code(url, "g90") # Sets all axis to absolute
    return "ok"
