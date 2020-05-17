# In this file, fill in the ... parts with lines of code. Do not
# create new functions.

from random import seed, randrange
P=" ♟♜♝♞♛♚"; L,R,BL,TL="▌▐▄▀"
BonR=WonR=WonB=DonR=DonB=RonB=GonR=GonB=RonG='\033[1;m\033['
WonR+='7;31;47m' # For drawing a white piece on a red background
WonB+='7;30;47m' # For drawing a white piece on a black background
DonR+='2;37;41m' # For drawing a dark piece on a red background
DonB+='2;37;40m' # For drawing a dark piece on a black background
GonR+='2;33;41m' # For drawing gold on a red background
GonB+='2;33;40m' # For drawing gold on a black background
RonG+='2;31;43m' # For drawing red on a gold background
RonB+='7;30;41m' # For drawing red on a black background
BonR+='0;30;41m' # For drawing black on a red background

def Black(x,w,c):
    """A function to print a chess piece on a black background.
        Inputs:
         x: A single-character string indicating the value to put in
            this square. It will be one of the following: " ", "♟",
            "♜", "♝", "♞", "♛", or "♚". (Note that " " is one of the
            options, and is used for empty squares.)
         w: A boolean value indicating whether this is a white piece.
         c: An integer indicating the column of this square. (We need
            to know this because the leftmost square (c=0) has gold 
            on the left side, and the rightmost square (c=7) has gold
            on the right side.

       Outputs:
       -To begin, in the one case that c=0, 3 spaces are printed. 
       -Next, regardless of c's value, the one character passed in
        as x is printed, in the indicated color.
       -Finally, in the one case that c=7, a newline character is 
        printed.                                                  """
    ...
    ...
    ...

    
def Red(x,w,c):
    """A function to print a chess piece on a red background.
        Inputs: These are the same as the inputs for Black()
         x: A string indicating the value to put in this square. 
         w: A boolean value indicating whether this is a white piece.
         c: An integer indicating the column of this square. 

       Outputs:
       -To begin, in the one case that c=0, 3 spaces are printed. 
       -Next, regardless of c's value, three characters always print:
         1: A "▐" character that is red on its right side, and that 
            is either gold (if c=0) or black (otherwise) on its left
            side.
         2: The character passed in as x, in the indicated color.
         3: A "▌" character that is red on its left side and that is
            either gold (if c=7) or black (otherwise) on its right
            side.
       -Finally, in the one case that c=7, a newline is printed.
        But somethings needs to be understood here. First, you don't 
        really need to print a "\n", you can just NOT use an "end=''"
        when printing this last "▌" piece. Second, you also need to 
        change the color to GonB before going to the next line, to 
        prevent colored bars from drawing on the left.            """
    ...
    ...
    ...

    
def DrawBoard(B,W):
    """A function to draw a chess board with its pieces.
        Inputs:
         B: This is the board. It must be a list of 8 strings, which
            indicate the 8 rows of the chessboard. The 8 strings are
            each 8 characters wide, indicating the 8 rows of the
            chessboard. The individual characters in the strings are
            any of the following: " ","♟","♜","♝","♞","♛", or "♚".
         W: This is a list of 16 complex numbers. Each number encodes
            the row/column position of one of the 16 white pieces.
            (We don't need a similar list of dark pieces, because
            anything that is not white can print as dark.

       Outputs:
        The output is to print the eight rows of the board, along 
        with two more rows for the top and bottom gold border.    """

    def DrawRow(r,B,W):
        """A function to draw a single row of the chess board.
           Input:
            r: An integer indicating the row number.
            B: This is the board.
            W: This is a list of white piece locations.

           Outputs:
            The output is the printing of the indicated row.      """
        ...
        ...
        ...

    ...
    ...
    ...


def DrawAnInitialBoard():
    """A function to create and draw an initial board. This means the
       board is: ["♜♝♞♛♚♞♝♜","♟♟♟♟♟♟♟♟","        ","        ",
                  "        ","        ","♟♟♟♟♟♟♟♟","♜♝♞♛♚♞♝♜"].
       and it also means that the white pieces are in the last two 
       rows.

       But I have RULES for you to follow.
        1. You cannot use any string quotes and you cannot call the
           str function in your implementation. I am making this rule
           to give you experience with slicing and string operators.
           I want to point out that the P string holds the symbols
           that you need.
           (I also want to point out that you should *start* by using
           the above-provided 8 strings for your board. Only after
           you get that working should you then create again the list
           of strings, but this time without using quotes.)
        2: Try to use as few characters as possible to implement this
           function. I will grade on based on how few characters you
           use (ignoring spaces, tabs, and newlines). My solution
           uses 102 characters.                                   """
    ...
    ...
    ...

DrawAnInitialBoard()
    
def DrawRandomBoard():
    """A function to create and draw a board with all 32 pieces in
       random positions.                                          """
    def RandomPlacement(color,otherColor):
        """A function to randomly place the 16 pieces of one color.
            Inputs:
             color: An empty list that we'll add these 16 pieces to. 
             otherColor: The list for the other color. (This list 
                         will be empty on the fist call and full on
                         the second call.)

            Outputs:
             The color list will now contain 16 complex numbers, to
             indicate the row/column positions of these pieces. 
             These numbers must be unique, occurring only once in
             either color or otherColor.                          """
        ...
        ...
        ...

    seed(0) # Comment this line to make it run differently each time
    W=[];D=[];B=[] #This B object is the board. 
    RandomPlacement(W, D)
    RandomPlacement(D, W)
    # Now that we know where the pieces go, we need to create the
    # eight rows of the board, inserting pieces into those spots.
    # Here, it does not matter how you decide to map the 16 pieces
    # of each color to the 16 positions in the W or D lists.
    for i in range(8):
        B+=[""]
        ...
        ...
        ...

    DrawBoard(B,W)
DrawRandomBoard()
