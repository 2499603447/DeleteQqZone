from pynput.mouse import Button, Controller
from pynput import keyboard
import time

# 控制鼠标
mouse = Controller()
isDeleting = True
i = 1

# 监听键盘按下事件
# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(key))
#
#
# def on_release(key):
#     print('{0} released'.format(key))
#     if key == keyboard.Key.esc:
#         # 停止监听
#         isDeleting = False
#         # return False
#
#
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

# 删除qq空间主页与我相关中的评论信息
while i > 0 and isDeleting:
    i = i - 1
    # 设置鼠标位置
    mouse.position = (145, 705.688)
    # print('Now, we have moved it to {0}'.format(mouse.position))
    # 模拟鼠标悬停效果，线程暂停500ms，此值自己定义
    time.sleep(0.5)
    # # 鼠标相对于当前位置向下移动到删除按钮区域
    mouse.move(0, 35)
    # 鼠标左键按下和释放
    mouse.press(Button.left)
    mouse.release(Button.left)

    # 鼠标移至弹出的删除与否确认对话框处的“确定”区域
    mouse.position = (610, 533.688)
    mouse.press(Button.left)
    mouse.release(Button.left)

# 删除qq空间相册板块左下角的访客记录
# while i > 0:
#     i = i - 1
#     # 设置鼠标位置
#     mouse.position = (145, 942.688)
#     # print('Now, we have moved it to {0}'.format(mouse.position))
#     # 模拟鼠标悬停效果，线程暂停500ms，此值自己定义
#     time.sleep(0.5)
#     # # 鼠标相对于当前位置向下移动到删除按钮区域
#     mouse.move(0, 1)
#     time.sleep(0.5)
#     mouse.move(20, 45)
#     # # 鼠标左键按下和释放
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     time.sleep(0.5)
#     # # 鼠标移至弹出的删除与否确认对话框处的“确定”区域
#     mouse.position = (630, 730.688)
#     mouse.press(Button.left)
#     mouse.release(Button.left)
