from pynput.mouse import Button, Controller

mouse = Controller()
from pynput.mouse import Button, Controller

mouse = Controller()

# 读取鼠标位置
print('The current pointer position is {0}'.format(mouse.position))

# 设置鼠标位置
mouse.position = (10, 20)
print('Now, we have moved it to {0}'.format(mouse.position))

# 鼠标相对于当前位置移动
mouse.move(5, -5)

# 鼠标点击和释放

mouse.press(Button.left)
mouse.release(Button.left)

# 鼠标双击
mouse.click(Button.left, 2)

# 鼠标滚轮下滑
mouse.scroll(0, 2)
# 读取鼠标位置
print('The current pointer position is {0}'.format(mouse.position))

# 设置鼠标位置
mouse.position = (10, 20)
print('Now, we have moved it to {0}'.format(mouse.position))

# 鼠标相对于当前位置移动
mouse.move(5, -5)

# 鼠标点击和释放

mouse.press(Button.left)
mouse.release(Button.left)

# 鼠标双击
mouse.click(Button.left, 2)

# 鼠标滚轮下滑
mouse.scroll(0, 2)