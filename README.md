*Deleteqq.py:（原始愚蠢暴力式删除）
删除QQ空间中相关信息，针对元素位置不发生变化的信息（鼠标的点击区域不发生变化），鼠标移动的位置请根据自生的显示器设定

安装必要的文件：pynput，可从pycharm的设置中安装，也可以通过pip命令安装：pip3 install pynput。
必要的环境安装完毕后

1.浏览器打开qq空间，切换至想要删除的信息栏，按下F12

2.查找对应的元素像素位置，如下拉箭头的位置（此值依据不同屏幕的分辨率不同而不同，比如我的位置为(790, 610.688)）

3.控制鼠标的点击事件


*deleteqqzone.js：
通过js代码删除qq空间中的说说信息

1.浏览器打开qq空间，切换至想要删除的信息栏，按下F12

2.切换至Console栏，将deleteqqzone.js中的代码复制到控制台，回车（具体的按照deleteqqzone.js中的注释）


*Mouse.py：
python控制鼠标及键盘，包括：

1.读取鼠标位置

2.监控鼠标事件

3.控制键盘

4.监控键盘事件
