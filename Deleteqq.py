from pynput.mouse import Button, Controller
import time
# 控制鼠标
mouse = Controller()

# 读取鼠标位置
i = 300
while i > 0:
    i = i - 1
    # 设置鼠标位置
    mouse.position = (790, 610.688)
    # print('Now, we have moved it to {0}'.format(mouse.position))
    # 模拟鼠标悬停效果，线程暂停500ms，此值自己定义
    time.sleep(0.5)
    # 鼠标相对于当前位置向下移动到删除按钮区域
    mouse.move(0, 35)
    #鼠标左键按下和释放
    mouse.press(Button.left)
    mouse.release(Button.left)

    # 鼠标移至弹出的删除与否确认对话框处的“确定”区域
    mouse.position = (610, 533.688)
    mouse.press(Button.left)
    mouse.release(Button.left)