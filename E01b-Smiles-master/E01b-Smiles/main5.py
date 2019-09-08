#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800 #7&8 Describe window screen height and windth
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Smiley Face Example" #Title of window

class Faces(arcade.Window): #What type of program
    """ Our custom Window Class"""

    def __init__(self): #Initiates code and process
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) 

        # Show the mouse cursor
        self.set_mouse_visible(True)

        self.x = SCREEN_WIDTH / 2 #Screen width to be displayed and interacted within
        self.y = SCREEN_HEIGHT / 2 #Screen height to be displayed and interacted within
    
        arcade.set_background_color(open_color.white) #Sets color bckground

    def on_draw(self): #Draw face
        """ Draw the face """
        arcade.start_render() #Renders arcade mode
        face_x,face_y = (self.x,self.y) #displays face on coordinates
        smile_x,smile_y = (face_x + 0,face_y - 10) #Relation of smile to location to face
        eye1_x,eye1_y = (face_x - 30,face_y + 20) #Relation of eye 1 to face location
        eye2_x,eye2_y = (face_x + 30,face_y + 20) #Relation of eye 2 to face
        catch1_x,catch1_y = (face_x - 25,face_y + 25)  #Relation of pupil to face
        catch2_x,catch2_y = (face_x + 35,face_y + 25) #Relation of pupil 2 to face

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) #37 through 43 detail the shape and descrpincies of the face
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)


    def on_mouse_motion(self, x, y, dx, dy): #Main source code for mouse movement
        """ Handle Mouse Motion """
        self.x = x #X coordinate of face follows mouse x coordinate
        self.y = y #y coordinat of face follows y of mouse



window = Faces() #title program
arcade.run() #run program