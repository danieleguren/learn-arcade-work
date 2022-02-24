import arcade
arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color((44, 230, 28))

arcade.start_render()


arcade.draw_lrtb_rectangle_filled(0, 600, 600, 450, (46, 154, 176))
arcade.draw_line(0, 450, 600, 450, (0, 0, 0))

#montañas
arcade.draw_triangle_filled(25, 580, -20, 400, 70, 400, (117, 55, 5))
arcade.draw_triangle_filled(25, 580, 20, 560, 30, 560, (255, 255, 255))
arcade.draw_line(25, 580, 70, 400, (0, 0, 0))
arcade.draw_line(25, 580, -20, 400, (0, 0, 0))

arcade.draw_triangle_filled(200, 525, 150, 420, 250, 420, (128, 71, 25))
arcade.draw_triangle_filled(200, 525, 189, 500, 211, 500, (255, 255, 255))
arcade.draw_line(200, 525, 150, 420, (0, 0, 0))
arcade.draw_line(200, 525, 250, 420, (0, 0, 0))

arcade.draw_triangle_filled(120, 560, 45, 370, 195, 370, (133, 78, 33))
arcade.draw_triangle_filled(120, 560, 104, 520, 136, 520, (255, 255, 255))
arcade.draw_line(120, 560, 45, 370, (0, 0, 0))
arcade.draw_line(120, 560, 195, 370, (0, 0, 0))


#sol
arcade.draw_circle_filled(525, 525, 40, (255, 247, 0))
arcade.draw_line(525, 590, 525, 460, (255, 247, 0),3)
arcade.draw_line(460, 525, 590, 525, (255, 247, 0),3)
arcade.draw_line(480, 480, 570, 570, (255, 247, 0),3)
arcade.draw_line(480, 570, 570, 480, (255, 247, 0),3)


#rio
arcade.draw_polygon_filled(((330, 450),
                            (-100, -10),
                            (300, -100),
                            (450, 450),
                            ),
                           (76, 222, 245))
arcade.draw_line(330, 450, -100, -10, (49, 68, 189),2)
arcade.draw_line(300, -100, 450, 450, (49, 68, 189),2)
arcade.draw_line(330, 450, 450, 450, (76, 222, 245),2)


#arboles
arcade.draw_lrtb_rectangle_filled(40, 60, 280, 190, (77, 53, 18))
arcade.draw_circle_filled(50, 320, 50, (92, 140, 38))
arcade.draw_lrtb_rectangle_filled(555, 561, 390, 360, (186, 152, 73))
arcade.draw_circle_filled(558, 400, 15, (36, 120, 6))



#persona
arcade.draw_circle_filled(440, 300, 23, (255, 215, 166))
arcade.draw_lrtb_rectangle_filled(429, 451, 278, 220, (255, 162, 0))
arcade.draw_circle_filled(430, 307, 3, (0, 0, 0))
arcade.draw_line(417, 295, 430, 295, (0, 0, 0),2)
arcade.draw_lrtb_rectangle_filled(429, 451, 234, 190, (227, 43, 23))
arcade.draw_lrtb_rectangle_filled(415, 451, 190, 180, (0, 0, 0))
arcade.draw_arc_filled(439, 315, 43, 46, (0, 0, 0), 0, 180)
arcade.draw_line(439, 316, 480, 316, (0, 0, 0),2)

arcade.draw_line(451, 278, 451, 190, (0, 0, 0))
arcade.draw_line(429, 278, 429, 190, (0, 0, 0))
arcade.draw_line(429, 278, 451, 278, (0, 0, 0))
arcade.draw_line(429, 190, 451, 190, (0, 0, 0))
arcade.draw_line(429, 234, 451, 234, (0, 0, 0))

arcade.draw_lrtb_rectangle_filled(436, 444, 269, 232, (255, 162, 100))
arcade.draw_lrtb_rectangle_filled(436, 444, 237, 227, (255, 215, 166))
arcade.draw_line(436, 269, 444, 269, (0, 0, 0))
arcade.draw_line(436, 269, 436, 227, (0, 0, 0))
arcade.draw_line(444, 269, 444, 227, (0, 0, 0))
arcade.draw_line(436, 227, 444, 227, (0, 0, 0))
arcade.draw_line(436, 237, 444, 237, (0, 0, 0))


#pez
arcade.draw_arc_filled(252, 60, 30, 18, (23, 56, 87), 90, 270)
arcade.draw_triangle_filled(280, 50, 280, 70, 265, 60, (23, 56, 87))
arcade.draw_triangle_filled(250, 50, 250, 70, 267, 60, (23, 56, 87))


#pajaro
arcade.draw_circle_filled(500, 350, 17, (203, 209, 31))
arcade.draw_triangle_filled(487, 340, 487, 350, 470, 345, (217, 144, 17))
arcade.draw_circle_filled(490, 354, 5, (250, 250, 250))
arcade.draw_circle_filled(490, 354, 3, (0, 0, 0))
arcade.draw_line(508, 350, 500, 350, (82, 76, 2),2)
arcade.draw_line(508, 347, 500, 347, (82, 76, 2),2)
arcade.draw_line(508, 344, 500, 344, (82, 76, 2),2)
arcade.draw_line(492, 362, 500, 370, (82, 76, 2),2)




arcade.finish_render()

arcade.run()
