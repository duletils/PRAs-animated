from manim import *

class AboutPRAs(Scene):
    def construct(self):
        pra_long = Text("Page Replacement Algorithms", color=BLACK)
        pra_short = Text("PRAs", color=BLACK)
        
        self.play(Write(pra_long, run_time=1))
        self.wait(1)
        self.play(Transform(pra_long, pra_short))
        self.wait(2)
        self.play(FadeOut(pra_long))

        random_pra = Text("Random PRA", color=BLACK)
        self.play(FadeIn(random_pra))
        self.wait(2)
        self.play(FadeOut(random_pra))

        time_cells = VGroup()

        for n in range(1, 17):
            number = Text(f"{n}", color=BLACK).scale(0.5)
            square = Square(side_length=0.5).set_stroke(width=0.5, color=BLACK)
            number.move_to(square.get_center())

            cell = VGroup(number, square)
            time_cells.add(cell)
        
        time_cells.arrange(RIGHT, buff=0)
        time_cells.move_to(3 * UP)
        time_step = Text("Time step:", color=BLACK).scale(0.4).move_to(time_cells.get_left() + 0.75 * LEFT)

        time_arrow = Arrow(time_cells.get_left() + 0.25 * LEFT, time_cells.get_right() + 0.25 * RIGHT, 
                           color=BLACK, stroke_width=1, max_tip_length_to_length_ratio=0.015) 
        time_arrow.move_to(time_cells.get_center() + 0.4 * DOWN)
        time_arrow_text = Text("Time", color=BLACK).scale(0.3).move_to(time_arrow.get_center() + 0.15 * DOWN)

        access_cells = VGroup()

        access_stream_numbers_array = [5, 2, 0, 7, 6, 7, 3, 1, 7, 6, 2, 7, 0, 5, 4, 3]

        for number in access_stream_numbers_array:
            number = Text(f"{number}", color=BLACK).scale(0.5)
            square = Square(side_length=0.5).set_stroke(color=BLACK, width=0.5)
            number.move_to(square.get_center())

            cell = VGroup(square, number)
            access_cells.add(cell)

        access_cells.arrange(RIGHT, buff=0)
        access_cells.move_to(time_cells.get_center() + DOWN)
        access_step = Text("Access stream:", color=BLACK).scale(0.4).move_to(access_cells.get_left() + 1.05 * LEFT)

        self.play(FadeIn(time_cells, time_step, time_arrow, time_arrow_text))
        self.wait(2)
        self.play(FadeIn(access_cells, access_step))
        self.wait(2)

        ram_grid = VGroup(VGroup())

        for row in range(0, 4):
            cell_row = VGroup()
            for column in range(0, 17):
                question_mark = Text("?", color=BLACK).scale(0.5)
                square = Square(side_length=0.5).set_stroke(width=0.5, color=BLACK)
                question_mark.move_to(square.get_center())

                cell = VGroup(question_mark, square)
                cell_row.add(cell)
            
            cell_row.arrange(RIGHT, buff=0)
            ram_grid.add(cell_row)

        ram_grid.arrange(DOWN, buff=0).move_to(access_cells.get_center() + 0.25 * LEFT + 2 * DOWN)
        ram_time_arrow = time_arrow.copy()
        ram_time_arrow.move_to(ram_grid.get_bottom() + 0.15 * DOWN + 0.2 * RIGHT)
        ram_time_arrow_text = time_arrow_text.copy()
        ram_time_arrow_text.move_to(ram_time_arrow.get_center() + 0.15 * DOWN)

        self.play(FadeIn(ram_grid, ram_time_arrow, ram_time_arrow_text))
        self.wait(1)

        ram_label = Text("RAM", color=BLACK).scale(0.5).rotate(PI/2).move_to(ram_grid.get_left() + 0.25 * LEFT)

        self.play(FadeIn(ram_label))
        self.wait(2)

        disk_array = VGroup()
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for letter_index in range(0, 8):
            rectangle = Rectangle(height=0.5, width=1).set_stroke(width=0.5, color=BLACK)
            letter = Text(f"{letters[letter_index]}", color=BLACK).scale(0.5).move_to(rectangle.get_center())
            number = Text(f"{letter_index}", color=BLACK).scale(0.25).move_to(rectangle.get_bottom() + 0.15 * UP + rectangle.get_left() + 0.2 * RIGHT)
            cell = VGroup(rectangle, letter, number)
            disk_array.add(cell)

        disk_array.arrange(UP, buff=0).move_to(ram_grid.get_right() + 1.5 * RIGHT)
        disk_array[0][0].set_fill(PURPLE_C, opacity=1.0)
        disk_array[1][0].set_fill(MAROON_A, opacity=1.0)
        disk_array[2][0].set_fill(GREEN_A, opacity=1.0)
        disk_array[3][0].set_fill(PURE_GREEN, opacity=1.0)
        disk_array[4][0].set_fill(YELLOW_A, opacity=1.0)
        disk_array[5][0].set_fill(LIGHT_GRAY, opacity=1.0)
        disk_array[6][0].set_fill(RED, opacity=1.0)
        disk_array[7][0].set_fill(ORANGE, opacity=1.0)

        disk_label = Text("Disk", color=BLACK).scale(0.5).move_to(disk_array.get_top() + 0.25 * UP)

        self.play(FadeIn(disk_array, disk_label))
        self.wait(2)

        stepping_arrow = Arrow(ram_grid.get_left() + 0.25 * RIGHT + 1.85 * UP, 
                               ram_grid.get_left() + 0.25 * RIGHT + 0.9 * UP,
                               color=BLACK, stroke_width=1, max_tip_length_to_length_ratio=0.3)

        stepping_arrow_step_length = 0.5 * RIGHT 

        self.play(FadeIn(stepping_arrow))
        self.wait(2)

        occupied_cells = VGroup()

        for letter_index in range(0, 8):
            rectangle = Square(side_length=0.5).set_stroke(width=0.5, color=BLACK)
            letter = Text(f"{letters[letter_index]}", color=BLACK).scale(0.5).move_to(rectangle.get_center())
            number = Text(f"{letter_index}", color=BLACK).scale(0.25).move_to(rectangle.get_bottom() + 0.1 * UP + rectangle.get_left() + 0.08 * RIGHT)
            cell = VGroup(rectangle, letter, number)
            occupied_cells.add(cell)

        occupied_cells[0][0].set_fill(PURPLE_C, opacity=1.0)
        occupied_cells[1][0].set_fill(MAROON_A, opacity=1.0)
        occupied_cells[2][0].set_fill(GREEN_A, opacity=1.0)
        occupied_cells[3][0].set_fill(PURE_GREEN, opacity=1.0)
        occupied_cells[4][0].set_fill(YELLOW_A, opacity=1.0)
        occupied_cells[5][0].set_fill(LIGHT_GRAY, opacity=1.0)
        occupied_cells[6][0].set_fill(RED, opacity=1.0)
        occupied_cells[7][0].set_fill(ORANGE, opacity=1.0)

        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length))

        self.wait(1)

        self.play(access_cells[0][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        transformation_cells = [occupied_cells[5].copy().move_to(ram_grid[4][1])]

        self.play(FadeIn(transformation_cells[0]))
        self.wait(1)

        transformation_cells = [occupied_cells[5].copy().move_to(ram_grid[4][2]),
                        occupied_cells[2].copy().move_to(ram_grid[3][2])]

        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]))

        self.wait(1)

        self.play(access_cells[1][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[1]))
        self.wait(1)

        transformation_cells = [occupied_cells[5].copy().move_to(ram_grid[4][3]),
                        occupied_cells[2].copy().move_to(ram_grid[3][3]),
                        occupied_cells[0].copy().move_to(ram_grid[4][3]),]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[1]))

        self.wait(1)

        self.play(access_cells[2][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[2]))
        self.wait(1)

        transformation_cells = [occupied_cells[0].copy().move_to(ram_grid[4][4]),
                        occupied_cells[2].copy().move_to(ram_grid[3][4]),
                        occupied_cells[7].copy().move_to(ram_grid[1][4])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[1]))

        self.wait(1)

        self.play(access_cells[3][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[2]))
        self.wait(1)

        transformation_cells = [occupied_cells[0].copy().move_to(ram_grid[4][5]),
                        occupied_cells[2].copy().move_to(ram_grid[3][5]),
                        occupied_cells[7].copy().move_to(ram_grid[1][5]),
                        occupied_cells[6].copy().move_to(ram_grid[4][5])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[1]),
                  FadeIn(transformation_cells[2]))

        self.wait(1)

        self.play(access_cells[4][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[3]))
        self.wait(1)

        transformation_cells = [occupied_cells[2].copy().move_to(ram_grid[3][6]),
                        occupied_cells[7].copy().move_to(ram_grid[1][6]),
                        occupied_cells[6].copy().move_to(ram_grid[4][6])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[1]),
                  FadeIn(transformation_cells[2]))

        self.wait(1)

        self.play(access_cells[5][0].animate.set_fill(GREEN, opacity=1))
        self.wait(1)
        
        transformation_cells = [occupied_cells[2].copy().move_to(ram_grid[3][7]),
                        occupied_cells[7].copy().move_to(ram_grid[1][7]),
                        occupied_cells[6].copy().move_to(ram_grid[4][7]),
                        occupied_cells[3].copy().move_to(ram_grid[4][7])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[1]),
                  FadeIn(transformation_cells[2]))

        self.wait(1)

        self.play(access_cells[6][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(ram_grid[4][7], transformation_cells[3]))
        self.wait(1)

        transformation_cells = [occupied_cells[2].copy().move_to(ram_grid[3][8]),
                        occupied_cells[7].copy().move_to(ram_grid[1][8]),
                        occupied_cells[3].copy().move_to(ram_grid[4][8]),
                        occupied_cells[1].copy().move_to(ram_grid[1][8])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[1]),
                  FadeIn(transformation_cells[2]))

        self.wait(1)

        self.play(access_cells[7][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(ram_grid[1][8], transformation_cells[3]))
        self.wait(1)

        transformation_cells = [occupied_cells[2].copy().move_to(ram_grid[3][9]),
                        occupied_cells[3].copy().move_to(ram_grid[4][9]),
                        occupied_cells[1].copy().move_to(ram_grid[1][9]),
                        occupied_cells[7].copy().move_to(ram_grid[1][9])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[2]),
                  FadeIn(transformation_cells[1]))

        self.wait(1)

        self.play(access_cells[8][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[3]))
        self.wait(1)

        transformation_cells = [occupied_cells[2].copy().move_to(ram_grid[3][10]),
                        occupied_cells[3].copy().move_to(ram_grid[4][10]),
                        occupied_cells[7].copy().move_to(ram_grid[1][10]),
                        occupied_cells[6].copy().move_to(ram_grid[1][10])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[2]),
                  FadeIn(transformation_cells[1]))

        self.wait(1)

        self.play(access_cells[9][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[3]))
        self.wait(1)

        transformation_cells = [occupied_cells[2].copy().move_to(ram_grid[3][11]),
                        occupied_cells[3].copy().move_to(ram_grid[4][11]),
                        occupied_cells[6].copy().move_to(ram_grid[1][11])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[2]),
                  FadeIn(transformation_cells[1]))

        self.wait(1)

        self.play(access_cells[10][0].animate.set_fill(GREEN, opacity=1))
        self.wait(1)

        transformation_cells = [occupied_cells[2].copy().move_to(ram_grid[3][12]),
                        occupied_cells[3].copy().move_to(ram_grid[4][12]),
                        occupied_cells[6].copy().move_to(ram_grid[1][12]),
                        occupied_cells[7].copy().move_to(ram_grid[3][12])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[2]),
                  FadeIn(transformation_cells[1]))

        self.wait(1)

        self.play(access_cells[11][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[3]))
        self.wait(1)

        transformation_cells = [occupied_cells[3].copy().move_to(ram_grid[4][13]),
                        occupied_cells[6].copy().move_to(ram_grid[1][13]),
                        occupied_cells[7].copy().move_to(ram_grid[3][13]),
                        occupied_cells[0].copy().move_to(ram_grid[4][13])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[2]),
                  FadeIn(transformation_cells[1]))

        self.wait(1)

        self.play(access_cells[12][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[3]))
        self.wait(1)

        transformation_cells =[occupied_cells[6].copy().move_to(ram_grid[1][14]),
                        occupied_cells[7].copy().move_to(ram_grid[3][14]),
                        occupied_cells[0].copy().move_to(ram_grid[4][14]),
                        occupied_cells[5].copy().move_to(ram_grid[2][14])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[2]),
                  FadeIn(transformation_cells[1]))

        self.wait(1)

        self.play(access_cells[13][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[3]))
        self.wait(1)

        transformation_cells =[occupied_cells[6].copy().move_to(ram_grid[1][15]),
                        occupied_cells[7].copy().move_to(ram_grid[3][15]),
                        occupied_cells[0].copy().move_to(ram_grid[4][15]),
                        occupied_cells[5].copy().move_to(ram_grid[2][15]),
                        occupied_cells[4].copy().move_to(ram_grid[2][15])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[2]),
                  FadeIn(transformation_cells[1]),
                  FadeIn(transformation_cells[3]))

        self.wait(1)

        self.play(access_cells[14][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[4]))
        self.wait(1)

        transformation_cells =[occupied_cells[6].copy().move_to(ram_grid[1][16]),
                        occupied_cells[7].copy().move_to(ram_grid[3][16]),
                        occupied_cells[0].copy().move_to(ram_grid[4][16]),
                        occupied_cells[4].copy().move_to(ram_grid[2][16]),
                        occupied_cells[3].copy().move_to(ram_grid[2][16])]
        
        self.play(stepping_arrow.animate.shift(stepping_arrow_step_length), 
                  FadeIn(transformation_cells[0]),
                  FadeIn(transformation_cells[2]),
                  FadeIn(transformation_cells[1]),
                  FadeIn(transformation_cells[3]))

        self.wait(1)

        self.play(access_cells[15][0].animate.set_fill(RED_B, opacity=1))
        self.wait(1)

        self.play(FadeIn(transformation_cells[4]))
        self.wait(1)

        hits_text = Text("Just 2 hits, and 14 misses!", color=BLACK).shift(2 * DOWN).scale(0.35)

        we_can_do_better_text = Text("We can do better!", color=BLACK).scale(0.5)
        we_can_do_better_text.move_to(hits_text.get_center() + 0.5 * DOWN)

        self.play(FadeIn(hits_text))
        self.wait(2)
        self.play(FadeIn(we_can_do_better_text))
        self.wait(2)

