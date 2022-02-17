import arcade
arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color((227, 17, 14))

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, (250, 127, 5))

arcade.draw_lrtb_rectangle_filled(450, 460, 240, 190, (120, 44, 11))
arcade.draw_circle_filled(455, 245, 20, (247, 233, 35))
arcade.draw_lrtb_rectangle_filled(150, 156, 170, 150, (120, 44, 11))
arcade.draw_circle_filled(153, 175, 10, (247, 233, 35))
arcade.draw_lrtb_rectangle_filled(280, 296, 190, 70, (120, 44, 11))
arcade.draw_circle_filled(288, 225, 60, (247, 233, 35))


arcade.draw_line(100, 400, 200, 400, (122, 12, 113),3)
arcade.draw_line(150, 500, 200, 400, (122, 12, 113),3)
arcade.draw_line(100, 400, 150, 500, (122, 12, 113),3)

arcade.draw_polygon_filled(((500, 420),
                            (495, 380),
                            (450, 375),
                            (495, 370),
                            (470, 320),
                            (500, 360),
                            ),
                           (0, 0, 0))
arcade.draw_polygon_filled(((500, 420),
                            (505, 380),
                            (550, 375),
                            (505, 370),
                            (530, 320),
                            (500, 360),
                            ),
                           (0, 0, 0))


arcade.finish_render()

arcade.run()