'''
jobs to do:
check movement wont foul endstops (check position of head)
move head (make sure z_min is reached
report new position

'''

from standard_fuctions import g_code

def abs_move(url,x,y,z):
    command = "G01" + "x" + x +"y" + y +"z" + z
    g_code(url,command)
    return "ok"

def rel_move(url,x,y,z):
    command = "G01" + "x" + x +"y" + y +"z" + z