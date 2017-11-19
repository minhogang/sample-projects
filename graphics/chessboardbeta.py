from graphics import *
from math import hypot
win = GraphWin('test', 750, 750)
width = 600
length = 600
black_pieces = ["black rook.gif",
            "black knight.gif",
            "black bishop.gif",
            "black queen.gif",
            "black king.gif",
            "black bishop.gif",
            "black knight.gif",
            "black rook.gif"]
black_pawns = "black pawn.gif"
white_pieces = ["white rook.gif",
            "white knight.gif",
            "white bishop.gif",
            "white queen.gif",
            "white king.gif",
            "white bishop.gif",
            "white knight.gif",
            "white rook.gif"]
white_pawns = "white pawn.gif"

class square:

    def __init__(self, length):
        self.x = 0
        self.y = 0
        self.length = length
        self.offset = length / 2
        self.boardwidth = length * 8
        self.boardlength = length * 8
        self.color = [color_rgb(153, 102, 51), color_rgb(255, 204, 153)]
        self.rectangle_center_points = {}
        self.blackrook1x = 0
        self.blackrook1y = 0
        self.blackrook1 = Point(self.blackrook1x - self.offset+(self.length), self.blackrook1y+(self.offset))
        self.blackrook1image = Image(Point(self.blackrook1x - self.offset+(self.length), self.blackrook1y+(self.offset)), black_pieces[0])
        self.blackknight1x = self.length
        self.blackknight1y = 0
        self.blackknight1 = Point(self.blackknight1x - self.offset+(self.length), self.blackknight1y+(self.offset))
        self.blackknight1image = Image(Point(self.blackknight1x - self.offset+(self.length), self.blackknight1y+(self.offset)), black_pieces[1])
        self.blackbishop1x = self.length * 2
        self.blackbishop1y = 0
        self.blackbishop1 = Point(self.blackbishop1x - self.offset+(self.length), self.blackbishop1y+(self.offset))
        self.blackbishop1image = Image(Point(self.blackbishop1x - self.offset+(self.length), self.blackbishop1y+(self.offset)), black_pieces[2])
        self.blackqueenx = self.length * 3
        self.blackqueeny = 0
        self.blackqueen = Point(self.blackqueenx - self.offset+(self.length), self.blackqueeny+(self.offset))
        self.blackqueenimage = Image(Point(self.blackqueenx - self.offset+(self.length), self.blackqueeny+(self.offset)), black_pieces[3])
        self.blackkingx = self.length * 4
        self.blackkingy = 0
        self.blackking = Point(self.blackkingx - self.offset+(self.length), self.blackkingy+(self.offset))
        self.blackkingimage = Image(Point(self.blackkingx - self.offset+(self.length), self.blackkingy+(self.offset)), black_pieces[4])
        self.blackbishop2x = self.length * 5
        self.blackbishop2y = 0
        self.blackbishop2 = Point(self.blackbishop2x - self.offset+(self.length), self.blackbishop2y+(self.offset))
        self.blackbishop2image = Image(Point(self.blackbishop2x - self.offset+(self.length), self.blackbishop2y+(self.offset)), black_pieces[5])
        self.blackknight2x = self.length * 6
        self.blackknight2y = 0
        self.blackknight2 = Point(self.blackknight2x - self.offset+(self.length), self.blackknight2y+(self.offset))
        self.blackknight2image = Image(Point(self.blackknight2x - self.offset+(self.length), self.blackknight2y+(self.offset)), black_pieces[6])
        self.blackrook2x = self.length * 7
        self.blackrook2y = 0
        self.blackrook2 = Point(self.blackrook2x - self.offset+(self.length), self.blackrook2y+(self.offset))
        self.blackrook2image = Image(Point(self.blackrook2x - self.offset+(self.length), self.blackrook2y+(self.offset)), black_pieces[7])
        self.blackpawn1x = 0
        self.blackpawn1y = self.length * 1
        self.blackpawn1 = Point(self.blackpawn1x - self.offset+(self.length), self.blackpawn1y+(self.offset))
        self.blackpawn1image = Image(Point(self.blackpawn1x - self.offset+(self.length), self.blackpawn1y+(self.offset)), black_pawns)
        self.blackpawn2x = self.length * 1
        self.blackpawn2y = self.length * 1
        self.blackpawn2 = Point(self.blackpawn2x - self.offset+(self.length), self.blackpawn2y+(self.offset))
        self.blackpawn2image = Image(Point(self.blackpawn2x - self.offset+(self.length), self.blackpawn2y+(self.offset)), black_pawns)
        self.blackpawn3x = self.length * 2
        self.blackpawn3y = self.length * 1
        self.blackpawn3 = Point(self.blackpawn3x - self.offset+(self.length), self.blackpawn3y+(self.offset))
        self.blackpawn3image = Image(Point(self.blackpawn3x - self.offset+(self.length), self.blackpawn3y+(self.offset)), black_pawns)
        self.blackpawn4x = self.length * 3
        self.blackpawn4y = self.length * 1
        self.blackpawn4 = Point(self.blackpawn4x - self.offset+(self.length), self.blackpawn4y+(self.offset))
        self.blackpawn4image = Image(Point(self.blackpawn4x - self.offset+(self.length), self.blackpawn4y+(self.offset)), black_pawns)
        self.blackpawn5x = self.length * 4
        self.blackpawn5y = self.length * 1
        self.blackpawn5 = Point(self.blackpawn5x - self.offset+(self.length), self.blackpawn5y+(self.offset))
        self.blackpawn5image = Image(Point(self.blackpawn5x - self.offset+(self.length), self.blackpawn5y+(self.offset)), black_pawns)
        self.blackpawn6x = self.length * 5
        self.blackpawn6y = self.length * 1
        self.blackpawn6 = Point(self.blackpawn6x - self.offset+(self.length), self.blackpawn6y+(self.offset))
        self.blackpawn6image = Image(Point(self.blackpawn6x - self.offset+(self.length), self.blackpawn6y+(self.offset)), black_pawns)
        self.blackpawn7x = self.length * 6
        self.blackpawn7y = self.length * 1
        self.blackpawn7 = Point(self.blackpawn7x - self.offset+(self.length), self.blackpawn7y+(self.offset))
        self.blackpawn7image = Image(Point(self.blackpawn7x - self.offset+(self.length), self.blackpawn7y+(self.offset)), black_pawns)
        self.blackpawn8x = self.length * 7
        self.blackpawn8y = self.length * 1
        self.blackpawn8 = Point(self.blackpawn8x - self.offset+(self.length), self.blackpawn8y+(self.offset))
        self.blackpawn8image = Image(Point(self.blackpawn8x - self.offset+(self.length), self.blackpawn8y+(self.offset)), black_pawns)
        self.blackpawninitpositionstatus = {self.blackpawn1: 0,
                                            self.blackpawn2: 0,
                                            self.blackpawn3: 0,
                                            self.blackpawn4: 0,
                                            self.blackpawn5: 0,
                                            self.blackpawn6: 0,
                                            self.blackpawn7: 0,
                                            self.blackpawn8: 0}
        self.blackdictionary = {self.blackrook1: self.blackrook1image,
                                self.blackbishop1: self.blackbishop1image,
                                self.blackknight1: self.blackknight1image,
                                self.blackqueen: self.blackqueenimage,
                                self.blackking: self.blackkingimage,
                                self.blackbishop2: self.blackbishop2image,
                                self.blackknight2: self.blackknight2image,
                                self.blackrook2: self.blackrook2image,
                                self.blackpawn1: self.blackpawn1image,
                                self.blackpawn2: self.blackpawn2image,
                                self.blackpawn3: self.blackpawn3image,
                                self.blackpawn4: self.blackpawn4image,
                                self.blackpawn5: self.blackpawn5image,
                                self.blackpawn6: self.blackpawn6image,
                                self.blackpawn7: self.blackpawn7image,
                                self.blackpawn8: self.blackpawn8image}
        self.whiterook1x = 0
        self.whiterook1y = self.length * 7
        self.whiterook1 = Point(self.whiterook1x - self.offset+(self.length), self.whiterook1y+(self.offset))
        self.whiterook1image = Image(Point(self.whiterook1x - self.offset+(self.length), self.whiterook1y+(self.offset)), white_pieces[0])
        self.whiteknight1x = self.length
        self.whiteknight1y = self.length * 7
        self.whiteknight1 = Point(self.whiteknight1x - self.offset+(self.length), self.whiteknight1y+(self.offset))
        self.whiteknight1image = Image(Point(self.whiteknight1x - self.offset+(self.length), self.whiteknight1y+(self.offset)), white_pieces[1])
        self.whitebishop1x = self.length * 2
        self.whitebishop1y = self.length * 7
        self.whitebishop1 = Point(self.whitebishop1x - self.offset+(self.length), self.whitebishop1y+(self.offset))
        self.whitebishop1image = Image(Point(self.whitebishop1x - self.offset+(self.length), self.whitebishop1y+(self.offset)), white_pieces[2])
        self.whitequeenx = self.length * 3
        self.whitequeeny = self.length * 7
        self.whitequeen = Point(self.whitequeenx - self.offset+(self.length), self.whitequeeny+(self.offset))
        self.whitequeenimage = Image(Point(self.whitequeenx - self.offset+(self.length), self.whitequeeny+(self.offset)), white_pieces[3])
        self.whitekingx = self.length * 4
        self.whitekingy = self.length * 7
        self.whiteking = Point(self.whitekingx - self.offset+(self.length), self.whitekingy+(self.offset))
        self.whitekingimage = Image(Point(self.whitekingx - self.offset+(self.length), self.whitekingy+(self.offset)), white_pieces[4])
        self.whitebishop2x = self.length * 5
        self.whitebishop2y = self.length * 7
        self.whitebishop2 = Point(self.whitebishop2x - self.offset+(self.length), self.whitebishop2y+(self.offset))
        self.whitebishop2image = Image(Point(self.whitebishop2x - self.offset+(self.length), self.whitebishop2y+(self.offset)), white_pieces[5])
        self.whiteknight2x = self.length * 6
        self.whiteknight2y = self.length * 7
        self.whiteknight2 = Point(self.whiteknight2x - self.offset+(self.length), self.whiteknight2y+(self.offset))
        self.whiteknight2image = Image(Point(self.whiteknight2x - self.offset+(self.length), self.whiteknight2y+(self.offset)), white_pieces[6])
        self.whiterook2x = self.length * 7
        self.whiterook2y = self.length * 7
        self.whiterook2 = Point(self.whiterook2x - self.offset+(self.length), self.whiterook2y+(self.offset))
        self.whiterook2image = Image(Point(self.whiterook2x - self.offset+(self.length), self.whiterook2y+(self.offset)), white_pieces[7])
        self.whitepawn1x = 0
        self.whitepawn1y = self.length * 6
        self.whitepawn1 = Point(self.whitepawn1x - self.offset+(self.length), self.whitepawn1y+(self.offset))
        self.whitepawn1image = Image(Point(self.whitepawn1x - self.offset+(self.length), self.whitepawn1y+(self.offset)), white_pawns)
        self.whitepawn2x = self.length * 1
        self.whitepawn2y = self.length * 6
        self.whitepawn2 = Point(self.whitepawn2x - self.offset+(self.length), self.whitepawn2y+(self.offset))
        self.whitepawn2image = Image(Point(self.whitepawn2x - self.offset+(self.length), self.whitepawn2y+(self.offset)), white_pawns)
        self.whitepawn3x = self.length * 2
        self.whitepawn3y = self.length * 6
        self.whitepawn3 = Point(self.whitepawn3x - self.offset+(self.length), self.whitepawn3y+(self.offset))
        self.whitepawn3image = Image(Point(self.whitepawn3x - self.offset+(self.length), self.whitepawn3y+(self.offset)), white_pawns)
        self.whitepawn4x = self.length * 3
        self.whitepawn4y = self.length * 6
        self.whitepawn4 = Point(self.whitepawn4x - self.offset+(self.length), self.whitepawn4y+(self.offset))
        self.whitepawn4image = Image(Point(self.whitepawn4x - self.offset+(self.length), self.whitepawn4y+(self.offset)), white_pawns)
        self.whitepawn5x = self.length * 4
        self.whitepawn5y = self.length * 6
        self.whitepawn5 = Point(self.whitepawn5x - self.offset+(self.length), self.whitepawn5y+(self.offset))
        self.whitepawn5image = Image(Point(self.whitepawn5x - self.offset+(self.length), self.whitepawn5y+(self.offset)), white_pawns)
        self.whitepawn6x = self.length * 5
        self.whitepawn6y = self.length * 6
        self.whitepawn6 = Point(self.whitepawn6x - self.offset+(self.length), self.whitepawn6y+(self.offset))
        self.whitepawn6image = Image(Point(self.whitepawn6x - self.offset+(self.length), self.whitepawn6y+(self.offset)), white_pawns)
        self.whitepawn7x = self.length * 6
        self.whitepawn7y = self.length * 6
        self.whitepawn7 = Point(self.whitepawn7x - self.offset+(self.length), self.whitepawn7y+(self.offset))
        self.whitepawn7image = Image(Point(self.whitepawn7x - self.offset+(self.length), self.whitepawn7y+(self.offset)), white_pawns)
        self.whitepawn8x = self.length * 7
        self.whitepawn8y = self.length * 6
        self.whitepawn8 = Point(self.whitepawn8x - self.offset+(self.length), self.whitepawn8y+(self.offset))
        self.whitepawn8image = Image(Point(self.whitepawn8x - self.offset+(self.length), self.whitepawn8y+(self.offset)), white_pawns)
        self.whitepawninitpositionstatus = {self.whitepawn1: 0,
                                            self.whitepawn2: 0,
                                            self.whitepawn3: 0,
                                            self.whitepawn4: 0,
                                            self.whitepawn5: 0,
                                            self.whitepawn6: 0,
                                            self.whitepawn7: 0,
                                            self.whitepawn8: 0}
        self.whitedictionary = {self.whiterook1: self.whiterook1image,
                                self.whitebishop1: self.whitebishop1image,
                                self.whiteknight1: self.whiteknight1image,
                                self.whitequeen: self.whitequeenimage,
                                self.whiteking: self.whitekingimage,
                                self.whitebishop2: self.whitebishop2image,
                                self.whiteknight2: self.whiteknight2image,
                                self.whiterook2: self.whiterook2image,
                                self.whitepawn1: self.whitepawn1image,
                                self.whitepawn2: self.whitepawn2image,
                                self.whitepawn3: self.whitepawn3image,
                                self.whitepawn4: self.whitepawn4image,
                                self.whitepawn5: self.whitepawn5image,
                                self.whitepawn6: self.whitepawn6image,
                                self.whitepawn7: self.whitepawn7image,
                                self.whitepawn8: self.whitepawn8image}

        self.piece_inside_highlighted = None
    def draw_pieces(self):
        for images in self.blackdictionary.values():
            images.draw(win)

    def draw_board(self):
        for row in range(1, 9):
            for col in range(1, 9):
                rectangle = Rectangle(Point(self.x-self.length+(self.length*col), self.y), Point(self.x+(self.length*col), self.y+self.length))
                center_points = rectangle.getCenter()
                self.rectangle_center_points["row " + str(row) + " col " + str(col)] = center_points
                rectangle.setFill(self.color[col % 2])
                rectangle.draw(win)
            self.color = list(reversed(self.color))
            self.y += self.length

    def register_click(self):
        while True:
            clickcoords = win.getMouse()
            if clickcoords.x > self.boardwidth or clickcoords.y > self.boardlength:
                win.close()
                break
            smallest_difference = None
            nearest_coords = None
            for value in self.rectangle_center_points.values():
                diff = abs(hypot(value.x - clickcoords.x, value.y - clickcoords.y))
                if smallest_difference == None:
                    smallest_difference = diff
                    nearest_coords = list(self.rectangle_center_points.keys())[list(self.rectangle_center_points.values()).index(value)]
                elif diff < smallest_difference:
                    smallest_difference = diff
                    nearest_coords = list(self.rectangle_center_points.keys())[list(self.rectangle_center_points.values()).index(value)]

            def highlight_square(self):
                nearest_coords_points = self.rectangle_center_points[nearest_coords]
                x1 = nearest_coords_points.x - self.offset
                y1 = nearest_coords_points.y - self.offset
                x2 = nearest_coords_points.x + self.offset
                y2 = nearest_coords_points.y + self.offset
                highlightedrect = Rectangle(Point(x1, y1), Point(x2, y2))
                highlightedrect.setOutline("yellow")
                highlightedrect.draw(win)
                for i in self.blackdictionary.keys():
                    if i.x == highlightedrect.getCenter().x and i.y == highlightedrect.getCenter().y:
                        self.piece_inside_highlighted = i
                        break


                def register_click_and_move_piece(self):

                        clickcoords = win.getMouse()
                        if clickcoords.x > self.boardwidth or clickcoords.y > self.boardlength:
                            win.close()
                        smallest_difference = None
                        nearest_coords = None
                        for value in self.rectangle_center_points.values():
                            diff = abs(hypot(value.x - clickcoords.x, value.y - clickcoords.y))
                            if smallest_difference == None:
                                smallest_difference = diff
                                nearest_coords = list(self.rectangle_center_points.keys())[list(self.rectangle_center_points.values()).index(value)]
                            elif diff < smallest_difference:
                                smallest_difference = diff
                                nearest_coords = list(self.rectangle_center_points.keys())[list(self.rectangle_center_points.values()).index(value)]
                        nearest_coords_points = self.rectangle_center_points[nearest_coords]
                        if not self.piece_inside_highlighted == None:
                            coords = (self.piece_inside_highlighted.x, self.piece_inside_highlighted.y)
                            newcoords = (nearest_coords_points.x, nearest_coords_points.y)
                            dxdy = Point(nearest_coords_points.x - self.piece_inside_highlighted.x, nearest_coords_points.y - self.piece_inside_highlighted.y)
                            for i in [self.blackrook1, self.blackrook2]:
                                if self.piece_inside_highlighted == i:
                                    if dxdy.x != 0:
                                        if dxdy.y != 0:
                                            return
                                    if dxdy.y != 0:
                                        if dxdy.x != 0:
                                            return
                                    if dxdy.x == 0:
                                        if dxdy.y > 0:
                                            for key in self.blackdictionary.keys():
                                                if int(key.y) in range(int(i.y), int(i.y+dxdy.y)) and key.x == i.x:
                                                    if key == i:
                                                        continue
                                                    if dxdy.y + i.y > key.y:
                                                        return
                                        if dxdy.y < 0:
                                            for key in self.blackdictionary.keys():
                                                if int(key.y) in range(int(dxdy.y+i.y), int(i.y)) and key.x == i.x:
                                                    if dxdy.y + i.y < key.y:
                                                        return
                                    if dxdy.y == 0:
                                        if dxdy.x > 0:
                                            for key in self.blackdictionary.keys():
                                                if key == i:
                                                    continue
                                                if key.x in range(int(i.x), int(i.x + dxdy.x)) and key.y == i.y:
                                                    if dxdy.x + i.x > key.x:
                                                        return
                                        if dxdy.x < 0:
                                            for key in self.blackdictionary.keys():
                                                if key == i:
                                                    continue
                                                if key.x in range(int(dxdy.x + i.x), int(i.x)) and key.y == i.y:
                                                    if dxdy.x + i.x < key.x:
                                                        return
                            for i in [self.blackbishop1, self.blackbishop2]:
                                if self.piece_inside_highlighted == i:
                                    if dxdy.x == 0:
                                        return
                                    if dxdy.y == 0:
                                        return
                                    if abs(dxdy.x) != abs(dxdy.y):
                                        return
                                    if abs(dxdy.x) == abs(dxdy.y):
                                        for key in self.blackdictionary.keys():
                                            if key == i:
                                                continue
                                            if dxdy.x > 0 and dxdy.y > 0:
                                                if key.x in range(int(i.x)+1, int(dxdy.x + i.x)) and key.y in range(int(i.y)+1, int(i.y + dxdy.y)) and abs(key.x - i.x) == abs(key.y - i.y):
                                                    if i.x + dxdy.x > key.x:
                                                        return
                                            if dxdy.x > 0 and dxdy.y < 0:
                                                if key.x in range(int(i.x)+1, int(dxdy.x + i.x)) and key.y in range(int(dxdy.y + i.y)+1, int(i.y)) and abs(key.x - i.x) == abs(key.y - i.y):
                                                    if i.x + dxdy.x > key.x:
                                                        return
                                            if dxdy.x < 0 and dxdy.y > 0:
                                                if key.x in range(int(dxdy.x + i.x)+1, int(i.x)) and key.y in range(int(i.y)+1, int(dxdy.y + i.y)) and abs(key.x - i.x) == abs(key.y - i.y):
                                                    if i.y + dxdy.y > key.y:
                                                        return
                                            if dxdy.x < 0 and dxdy.y < 0:
                                                if key.x in range(int(i.x + dxdy.x)+1, int(i.x)) and key.y in range(int(dxdy.y + i.y)+1, int(i.y)) and abs(key.x - i.x) == abs(key.y - i.y):
                                                    if i.y + dxdy.y > key.y:
                                                        return
                            for i in [self.blackknight1, self.blackknight2]:
                                if self.piece_inside_highlighted == i:
                                    if abs(dxdy.x) + abs(dxdy.y) != self.length * 3:
                                        return
                            for i in [self.blackqueen]:
                                if self.piece_inside_highlighted == i:
                                    if dxdy.x != 0 and dxdy.y != 0:
                                        if abs(dxdy.x) != abs(dxdy.y):
                                            return
                                    if dxdy.x == 0:
                                        if dxdy.y > 0:
                                            for key in self.blackdictionary.keys():
                                                if key == i:
                                                    continue
                                                if key.y in range(int(i.y), int(i.y + dxdy.y)) and key.x == i.x:
                                                    if dxdy.y + i.y > key.y:
                                                        return
                                        if dxdy.y < 0:
                                            for key in self.blackdictionary.keys():
                                                if key == i:
                                                    continue
                                                if key.y in range(int(dxdy.y + i.y), int(i.y)) and key.x == i.x:
                                                    if dxdy.y + i.y < key.y:
                                                        return
                                    if dxdy.y == 0:
                                        if dxdy.x > 0:
                                            for key in self.blackdictionary.keys():
                                                if key == i:
                                                    continue
                                                if key.x in range(int(i.x), int(i.x + dxdy.x)) and key.y == i.y:
                                                    if dxdy.x + i.x > key.x:
                                                        return
                                        if dxdy.x < 0:
                                            for key in self.blackdictionary.keys():
                                                if key == i:
                                                    continue
                                                if key.x in range(int(dxdy.x + i.x), int(i.x)) and key.y == i.y:
                                                    if dxdy.x + i.x < key.x:
                                                        return
                                    if abs(dxdy.x) == abs(dxdy.y):
                                        for key in self.blackdictionary.keys():
                                            if key == i:
                                                continue
                                            if dxdy.x > 0 and dxdy.y > 0:
                                                if key.x in range(int(i.x)+1, int(dxdy.x + i.x)) and key.y in range(int(i.y)+1, int(i.y + dxdy.y)) and abs(key.x - i.x) == abs(key.y - i.y):
                                                    if i.x + dxdy.x > key.x:
                                                        return
                                            if dxdy.x > 0 and dxdy.y < 0:
                                                if key.x in range(int(i.x)+1, int(dxdy.x + i.x)) and key.y in range(int(dxdy.y + i.y)+1, int(i.y)) and abs(key.x - i.x) == abs(key.y - i.y):
                                                    if i.x + dxdy.x > key.x:
                                                        return
                                            if dxdy.x < 0 and dxdy.y > 0:
                                                if key.x in range(int(dxdy.x + i.x)+1, int(i.x)) and key.y in range(int(i.y)+1, int(dxdy.y + i.y)) and abs(key.x - i.x) == abs(key.y - i.y):
                                                    if i.y + dxdy.y > key.y:
                                                        return
                                            if dxdy.x < 0 and dxdy.y < 0:
                                                if key.x in range(int(i.x + dxdy.x)+1, int(i.x)) and key.y in range(int(dxdy.y + i.y)+1, int(i.y)) and abs(key.x - i.x) == abs(key.y - i.y):
                                                    if i.y + dxdy.y > key.y:
                                                        return
                            for i in [self.blackking]:
                                if self.piece_inside_highlighted == i:
                                    if abs(dxdy.x) > self.length or abs(dxdy.y) > self.length:
                                        return
                            for i in [self.blackpawn1, self.blackpawn2, self.blackpawn3, self.blackpawn4, self.blackpawn5, self.blackpawn6, self.blackpawn7, self.blackpawn8]:
                                if self.piece_inside_highlighted == i:
                                    if self.blackpawninitpositionstatus[i] == 0:
                                        if dxdy.x != 0:
                                            return
                                        if dxdy.y > self.length * 2:
                                            return
                                        for key in self.blackdictionary.keys():
                                            if key == i:
                                                continue
                                            if key.y in range(int(i.y), int(i.y + dxdy.y)) and key.x == i.x:
                                                if i.y + dxdy.y > key.y:
                                                    return
                                        self.blackpawninitpositionstatus[i] = 1
                                        break
                                    if self.blackpawninitpositionstatus[i] == 1:
                                        if dxdy.x != 0:
                                            return
                                        if dxdy.y > self.length * 1:
                                            return
                                        if dxdy.y < 0:
                                            return
                            image = self.blackdictionary[self.piece_inside_highlighted]
                            imageanchor = image.getAnchor()
                            for key in self.blackdictionary.keys():
                                if imageanchor.x + dxdy.x == key.x and imageanchor.y + dxdy.y == key.y:
                                    return
                            image.move(dxdy.x, dxdy.y)
                            anchor = image.getAnchor()
                            self.piece_inside_highlighted.x = anchor.x
                            self.piece_inside_highlighted.y = anchor.y
                            print(self.piece_inside_highlighted)
                register_click_and_move_piece(self)
                self.piece_inside_highlighted = None
                highlightedrect.undraw()
            highlight_square(self)


t = square(80)
t.draw_board()
t.draw_pieces()
t.register_click()

