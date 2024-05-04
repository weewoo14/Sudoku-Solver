from settings import *
numpad_layout = []
numpad_color = {1: BLUE, 0:LIGHT_BLUE}
for row in range(NUMPAD_LENGTH):
    row_rect = []
    for col in range(NUMPAD_WIDTH):
        row_rect.append((100 * col + NUMPAD_OFFSET,100 * row + BOARD_OFFSET, BOX_WIDTH,BOX_LENGTH))
    numpad_layout.append(row_rect)
numpad_layout.append([[1200,350,BOX_WIDTH,BOX_LENGTH]])
numpad_text = []
current_number = 0
for row in range(NUMPAD_LENGTH):
    text_row = []
    for col in range(NUMPAD_WIDTH):
        current_number += 1
        rect_xpos,rect_ypos = numpad_layout[row][col][0]+TEXT_OFFSET,numpad_layout[row][col][1]+TEXT_OFFSET
        text_row.append([(rect_xpos,rect_ypos,BOX_WIDTH,BOX_LENGTH),str(current_number),WHITE])
    numpad_text.append(text_row)
numpad_text.append([[(1200+TEXT_OFFSET,350+TEXT_OFFSET,BOX_WIDTH,BOX_LENGTH),'D',WHITE]])
selected_number = []