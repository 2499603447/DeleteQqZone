# 1.读取鼠标位置
# from pynput.mouse import Button, Controller
#
# mouse = Controller()
# print('The current pointer position is {0}'.format(mouse.position))
#
# # 设置鼠标位置
# mouse.position = (10, 20)
# print('Now, we have moved it to {0}'.format(mouse.position))
#
# # 鼠标相对于当前位置移动
# mouse.move(5, -5)
#
# # 鼠标点击和释放
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # 鼠标双击
# mouse.click(Button.left, 2)
#
# # 鼠标滚轮下滑
# mouse.scroll(0, 2)

# 2.监控鼠标事件
# 使用 pynput.mouse.Listener 监控鼠标事件
# from pynput import mouse
#
# def on_move(x, y):
#     print('Pointer moved to {0}'.format((x, y)))
#
# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
#     if not pressed:
#         # 停止监听
#         return False
#
# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
#
# # 收集鼠标事件直到释放
# with mouse.Listener(on_move = on_move, on_click = on_click, on_scroll = on_scroll) as listener:
#     listener.join()


# 3.控制键盘
# from pynput.keyboard import Key, Controller
# keyboard = Controller()
#
# # Space按下与释放
# keyboard.press(Key.space)
# keyboard.release(Key.space)
#
# # 输入小写a
# keyboard.press('a')
# keyboard.release('a')
#
# # 输入大写A
# keyboard.press('A')
# keyboard.release('A')
#
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')
#
# # 输入“Hello world”
# keyboard.type('Hello world')

# 4.监控键盘事件
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # 停止监听
        return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
