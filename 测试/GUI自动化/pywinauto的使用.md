
## 为什么要做GUI自动化

在软件测试过程中，有许多重复性的测试用例需要执行，例如对软件的各种基本功能进行验证。如果手动测试，测试人员需要不断地重复相同的操作步骤，这不仅耗时而且容易出错。而 GUI 自动化测试工具可以在短时间内快速执行大量重复的测试用例，并且能够始终按照预设的逻辑和步骤进行操作，从而极大地提高了测试效率

通过 GUI 自动化测试，可以减少对人力的依赖。原本需要多名测试人员花费数小时甚至数天才能完成的测试工作，现在只需编写好自动化测试脚本，由自动化测试工具在规定时间内完成，这样可以将测试人员从繁琐的重复性工作中解放出来，在一定程度上降低了人力成本。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/570af5719bfd43358ee35f905e091f8e.png#pic_center)

### 适用场景

GUI自动化适用于各种需要对图形用户界面进行重复性、一致性测试的场景，尤其在验证软件功能的稳定性、正确性和用户体验方面发挥着重要作用。

在软件开发的各个阶段，从集成测试到验收测试，它都可以帮助测试人员快速发现潜在问题，如界面元素是否正常显示、交互是否流畅、功能是否按预期工作等，从而确保软件质量

GUI自动化可以模拟不同用户环境下的操作，测试其兼容性和稳定性。此外，在进行大规模测试时，它能显著提高测试效率，减少人力成本，快速提供反馈，支持持续集成和持续交付，加速软件开发周期。

总之，GUI自动化适用于需要高效、准确、重复测试GUI应用程序的各种场景，有助于提升软件质量、用户满意度和开发效率。需要注意的是，尽管GUI自动化适用于上述场景，但其成功依赖于界面元素的稳定性——若UI频繁变动或涉及复杂交互，维护成本可能陡增。

## 为什么选择pywinauto

Pywinauto是⼀款基于Python的跨平台GUI⾃动化库，专⻔针对Windows桌⾯应⽤程序设计，其核⼼能⼒在于通过模拟⽤⼾交互⾏为（如⿏标点击、键盘输⼊）实现对窗⼝、对话框及内部控件的精准定位与操作，适⽤于⾃动化测试、批量任务处理及⽇常办公流程优化等场景。
 该库通过两种底层技术（backend="win32"和backend="uia"）适配不同框架开发的应⽤程序：


 - win32模式适⽤于传统MFC、VB6等旧架构
 - uia模式则⽀持现代WinForms、WPF、Qt5及浏览器等应⽤

### pywinauto的优势

• 基于Python：Python语⾔简洁易学，适合快速开发和维护。
• 跨平台⽀持：⽀持Windows 7及以上版本，兼容性良好。
• 丰富的控件⽀持：⽀持Windows原⽣控件（如按钮、⽂本框、表格）以及第三⽅控件（如WPF、
Qt）。
• 动态查找机制：⾃动等待控件加载完成，⽆需显式等待。
• 强⼤的调试⼯具：提供 pywinauto.findwindows 模块，⽅便定位控件。
• 社区活跃：开源项⽬，持续更新，⽂档和⽰例丰富。

### pywinauto的局限性

仅⽀持Windows：⽆法⽤于Mac或Linux平台。对⾮标准控件⽀持有限：某些⾃定义控件可能需要额外处理

## pywinauto的常见操作

### 打开程序

#### 打开应用程序

`start(self, cmd_line......)`

部分参数
cmd_line ：这是启动应⽤程序的命令⾏字符串。它必须包含应⽤程序的路径和名称，还可以包含启动参数

```python
Application(backend='uia').start('D:\\sublime\\Sublime Text\\sublime_text.exe')
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b7b9cac8eb0b436f947086b00afa1213.png#pic_center)

#### 连接已经打开的应用程序

`connect(self, **kwargs)`
process ：目标的进程ID
handle ：目标的窗口句柄

注意：连接到已在运行的进程，该动作仅根据一个参数执行
比如，打开sublime_text程序
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/47c1009788354aaa8601bd2f8c6152ee.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/757cb6f4c9d24a7ab5aa3560c13b60b9.png#pic_center)

### 定位窗口

#### 通过高级pywinauto API提供的window方法来定位

`app.window(title='',...)`
参数说明（参数可以组合使用）：
title : 文本为指定值的元素。
title_re : 文本匹配指定正则表达式的元素。
best_match : 标题与指定值相似的元素。
class_name : 窗口类为指定值的元素。
class_name_re : 类名匹配指定正则表达式的元素。

```python
#start参数换成Sublime Text的目标路径
app = Application(backend='uia').start("D:\software\Sublime Text
3\sublime_text.exe")
win = app.window(title_re='.*Sublime Text.*')
#title--精确匹配
win = app.window(title="untitled • - Sublime Text (UNREGISTERED)")
#title_re-正则匹配
win = app.window(title_re=".*Sublime.*")
#best_match-模糊匹配
win = app.window(best_match="untitled • - Sublime Text")
#class_name--精确匹配
win = app.window(class_name="PX_WINDOW_CLASS")
#class_name--正则匹配
win = app.window(class_name_re=".*WINDOW_CLASS")
win.print_control_identifiers()
```

print_control_identifiers() 方法用于打印窗口及其子控件的标识符信息，帮助用户识别控件
**输出内容**
◦ 控件的类名、标题、位置（左、上、右、下边界的坐标值）、控制类型等信息。
◦ 每个控件的“best match”名称列表，这些名称可以用于引用控件。

#### 通过动态解析对象属性定位

```python
#不推荐
app.“best_match”名称

win = app.Dialog
#上面写法等价于
win = app.window(best_match='Dialog')
```

Python通过动态解析对象属性简化了创建窗口规范。但是属性名与任何变量名都有相同的限制：没有空格、逗号和其他特殊符号，因此这是不推荐写法。
若存在空格或者其他特殊字符等，可采用类似字典的方式访问，如

```python
win = app['untitled • - Sublime Text (UNREGISTERED)']
#上面写法等价于
win = app.window(best_match="untitled • - Sublime Text (UNREGISTERED)")
```

最简单的定位窗口方法是询问top_window() ，例如 win = app.top_window()
需要注意，这是目前相当未经测试的，所以不确定它会返回正确的窗口。 它绝对是应用程序的顶级窗口 - 它可能不是Z-Order中最高的窗口，但不一定是我们想要的窗口

### 窗口操作

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/9fcbd77049824da89f9d52ad83030b7b.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2ec8ca74577c4fb3b7a8f2c655bd62d9.png#pic_center)

```python
import time
from pywinauto import Application

app = Application(backend='uia').connect(process=28560)
win = app.window(title_re='.*Sublime Text.*')
# 添加等待
# win.wait('visible')
win.wait('exists')
# time.sleep(3)
# 对窗口的操作

# 窗口的最大化和最小化
win.maximize()
print("max result: ",win.is_maximized())
time.sleep(2)
win.minimize()
print("min result: ",win.is_minimized())
time.sleep(2)
win.restore()
print("restore result: ",win.is_normal())
print("get_show_state:",win.get_show_state())
# 关闭窗口
win.close()
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/34ab946b84a34365b3185324c200e359.png#pic_center)

 ### 定位控件

 桌面应用程序客户端的控件和层级结构是GUI自动化测试的基础。理解控件的分类、特性和层级关系，能够帮助测试人员更高效地定位和操作控件，实现自动化测试。在实际测试中，结合控件的属性和事件，可以编写灵活且可靠的测试脚本
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/00f08f7a7baf431bb13d803699ef90da.png#pic_center)
常见控件示例
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a801143b6a09466f8e5d9ea0fe36e1c0.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e4ec3330c8d844f484e27e5ad47bbf2b.png#pic_center)
通过合理的分类和说明，可以更清晰地理解控件的功能和用途，便于在GUI自动化测试中进行操作和定位

在使用 pywinauto 进行自动化操作时，程序启动后，首先需要定位到目标窗口。窗口是所有控件的容
器，只有成功定位到窗口，才能进一步操作窗口内的控件。控件是窗口功能的具体体现，包括按钮、文本框、列表等，对控件的操作是自动化任务的核心。然而，在对控件进行操作之前，必须先完成控件的定位。定位控件是确保操作准确性的关键步骤，也是自动化流程的基础

定位控件，需要借助前面学到的rint_control_identifiers() 方法，打印窗口及其子控件的标识符信息

#### 动态解析

基于best_match标题来定位

sublime Text工具的菜单栏

```python
from pywinauto import Application
# 创建Application对象，连接到正在运行的Sublime Text进程
app = Application(backend='uia').connect(process=38544)
# 获取与Sublime Text相关的窗口对象，使用正则表达式匹配窗口标题
win = app.window(title_re='.*Sublime Text.*')
# 等待窗口变为可见状态，确保窗口已经加载完成
win.wait("visible")
# 通过窗口的标题获取菜单对象
menu = win['应用程序']
# 打印菜单项的列表，查看菜单中包含的所有选项
print(menu.items())
```

#### child_window

child_window() 和定位窗口的方法window() 参数一样，可以通过标题或者类名进行精确匹配、模糊匹配等，在这里额外拓展几个进行控件定位时需要用到的参数：
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a89626a0ad974d53bb95dec5e6c55f1d.png#pic_center)
控件之间存在父子关系，可通过children() 方法获取控件的子类，也可通过parent() 方法获取控件的父类

### 等待

GUI应用程序行为通常不稳定，脚本需要等待，直到出现新窗口/隐藏现有窗口。pywinauto可以隐式灵活的等待对话框初始化，或者明确的使用专用方法/函数来帮助你使用代码更容易和更可靠

#### wait/wait_not（）

`wait(self, wait_for, timeout=None, retry_interval=None)`
`wait_not(self, wait_for_not, timeout=None, retry_interval=None)`
参数说明：
• wait_for ：表示选择的窗口状态
◦ exists ：表示窗口是一个有效的句柄
◦ visible ：表示窗口不隐藏，可以看到
◦ enable ：表示窗口未被禁用，可操作
◦ ready ：表示窗口可见且已启用
◦ active ：表示窗口处于活动状态
• timeout ：表示超时
• retry_interval ：表示重试时间间隔，单位为秒s
wait_not 与wait() 类似， wait 是等待处于某种状态，而 wait_not 是等待不处于某种状态，这里以wait为例说明

**"exists" 和"visible"**

```python
from pywinauto.application import Application
app = Application(backend='uia').connect(process=38544)
win = app.window(title_re='.*Sublime Text.*')
#检查窗口是有效的句柄
win.wait('exists')
#检查窗口是否可见
win.wait('visible')
#检查窗口是否未被禁用
win.wait('enabled')
#检查窗口是否准备就绪
win.wait('ready')
```

窗口被最小化之后，在桌面就不可见了，因此最小化时需要将等待状态改为"exists" ，应用程序界面在桌面可见时等待状态可以设置为"visible"
**"enabled"**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ba745b3176684758b7ca2c4a7ee41216.png#pic_center)

```python
calc = Application(backend='uia').connect(process=2308)
win = calc.window(title='计算器')
win.wait('visible')
# win.print_control_identifiers()
# 启用的按钮
enable_btn = win.child_window(title="记忆减法", auto_id="MemMinus", control_type="Button")
# 未启用的按钮
disabled_btn = win.child_window(title="清除所有记忆", auto_id="ClearMemoryButton", control_type="Button")
enable_btn.wait('enabled')
disabled_btn.wait_not('enabled')
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/cfa2754e1f434829ac2aa865a2ba3d31.png#pic_center)
若按钮置灰状态，说明按钮为disabled 状态，当输入项不为空时，按钮高亮，此时为enabled状态

**'ready'**
`ready = visible + enabled`

```python
calc = Application(backend='uia').connect(process=2308)
win = calc.window(title='计算器')
win.wait('visible')
btn = win.child_window(title="打开导航", auto_id="TogglePaneButton", control_type="Button")
print(btn.is_visible())
print(btn.is_enabled())
text = win.child_window(auto_id="PaneTitleTextBlock", control_type="Text")
text.wait('exists')
print(text.is_visible())
print(text.is_enabled())
# ready = visible + enabled
btn.wait('ready')
# text.wait('ready')
```

is_visible() 用于检查元素是否可见，除此之外，is_enabled() 用于检查元素是否启用

**'active'**
需要注意， 'active' 状态指的是窗口是否处于活动状态，需要先操作应用程序使得焦点设置在该窗口上或者配合set_focus 来使用

```python
app = Application(backend='uia').connect(process=15712)
win = app.window(title='计算器')
win.set_focus()
win.wait('active')
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/f1cfc7c964dd43df8503d3a73102a0b2.png#pic_center)

#### wait_until

等待满足某个条件
`wait_until(timeout,retry_interval,func,value=True,op=operator.eq,*args, **kwargs)`
部分参数说明：
• Timeout ：超时时间
• retry_interval ：重试时间
• func ：执行的函数
• value ：比较的值
意思就是**总的等待是时间是timeout，每retry_interval秒重新执行一次func函数，直到返回值为value**

```python
i = 0
def work():
    global i
    i += 1
    print(f"当前i的值为{i}")
    return i
wait_until(10,1,work,5)
print('等待通过')
```

```python
def get_window():
    app = Application(backend='uia').connect(process=17456)
    win = app.window(title_re='.*Sublime Text.*')
    return win.is_visible()

wait_until(10,2,get_window,True)
print("等待通过")
```

### 控件的操作

#### 点击

`click_input()`
模拟鼠标左键单击操作

```python
from pywinauto import Application
app = Application(backend='uia').connect(process=8732)
win = app.window(title_re='.*Sublime Text.*')
win.wait("visible")
#点击最大化按钮
win.child_window(title="最大化", control_type="Button").click_input()
```

`right_click_input()`
模拟鼠标右键单击操作

```python
from pywinauto import Application
app = Application(backend='uia').connect(process=8732)
win = app.window(title_re='.*Sublime Text.*')
win.wait("visible")
#右键窗口
win.right_click_input()
```

`double_click_input()`
模拟鼠标左键双击操作

```python
from pywinauto import Application
app = Application(backend='uia').connect(process=8732)
win = app.window(title_re='.*Sublime Text.*')
win.wait("visible")
menu = win['应用程序']
#双击菜单栏——达到窗口最大化目的
menu.double_click_input()
```

#### 文本

`texts()`
用来获取窗口或空间中所有文本内容，返回一个==列表==，其中每个元素都是一个字符串，表示窗口或空间中的某个文本片段

````python
app = Application(backend="uia").connect(process=17456)
win = app.window(title_re='.*Sublime Text.*')
win.wait('visible')

print(win.texts())
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6a6097cbb05e4840b233c622f09ba30a.png#pic_center)
`window_text()`
用于获取窗口或空间的主文本内容，通常是窗口的标题或主要显示的文本。他返回一个==字符串==。
```python
app = Application(backend="uia").connect(process=17456)
win = app.window(title_re='.*Sublime Text.*')
win.wait('visible')

print(win.texts())
print(win.window_text())
```
````

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1527a18a7e0c4a5b81ea5ba257393170.png#pic_center)
### 鼠标操作
在使用 pywinauto 进行自动化测试时，我们通常会利用控件的点击方法来实现交互操作。这些方法不仅支持对控件的直接点击，还允许通过指定 oords 参数来实现基于坐标的点击操作

pywinauto 提供了一个独立的 mouse 模块，专门用于模拟真实用户的鼠标事件。这个模块的优势在于，它完全独立于控件操作，能够更贴近真实用户的行为模式。通过 mouse模块，我们可以直接在幕上指定坐标进行点击、双击、拖动等操作，而无需依赖控件的层次结构

```python
from pywinauto import Application
app = Application(backend='uia').connect(process=32936)
win = app.window(title_re='.*Sublime Text.*')
win.wait("visible")
#通过鼠标点击
mouse.click(coords=(1043,130))
```
`rectangle()`：获取元素对应坐标，返回矩形尺寸，具有top，left，right，bottom属性
`mid_point()`：获取元素中间位置坐标，返回类型为元组，元组汇总两个整数分别为x，y轴的值
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/58d8c6186aaa45f4820ceb4cc8d42158.png#pic_center)
```python
from pywinauto import Application
# app = Application(backend='uia').start("mspaint.exe")
app = Application(backend='uia').connect(process=28372)
win = app.window(title="无标题 - 画图")
win.wait('visible')
#定位滚动条
right_ScrollBar = win.child_window(title="垂直滚动条",
auto_id="NonClientVerticalScrollBar", control_type="ScrollBar")
right_ScrollBar.wait('visible')
#获取滚动条中间位置
mid = right_ScrollBar.rectangle().mid_point()
#从中间位置下拉
mouse.scroll(coords=(mid.x,mid.y),wheel_dist=500)
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/140b3b2f96ff4e8d87b85a541127c238.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/31c148bb705d40f1b278e493fc0377ec.png#pic_center)
### 键盘操作
在自动化测试中，pywinauto 提供了强大的键盘操作功能，其中 keyboard 模块是核心组件之一。

keyboard.send_keys() 是一个通用的键盘输入方法，它可以直接将按键序列发送到当前具有焦点的窗口。然而，在实际的自动化场景中，我们通常需要针对特定的控件（如文本框、按钮等）进行精确的输入操作，而不是于窗口的焦点状态。

```python
from pywinauto.keyboard import send_keys
send_keys("1234567")
```
为了满足这种需求，pywinauto 对键盘输入功能进行了进一步的封装，引入了type_keys 方法。是控件对象（例如 Edit 控件或 Button 控件）的专属方法，可以直接作用于指定的控件，确保输入内容精准无误。这种方法避免了因焦点切换导致的输入错误，特别适合在复杂的用户界面中进行自动化操作
```python
type_keys(
keys, # 要输入的键序列，可以是普通字符、特殊键或组合键
pause = None, #每次按键后的延迟时间（秒）
with_spaces = False, # 如果为 True，则会在输入的字符串中保留空格。
with_newlines = False, #如果为 True，则会在输入的字符串中保留换行符。
...
)
```
#### 输入文本

 - 直接输入文本（支持函Unicode字符）：
```python
from pywinauto import Application
app = Application(backend='uia').connect(process=32936)
win = app.window(title_re='.*Sublime Text.*')
win.wait("visible")
#输入文本内容
win.123("------type_keys------")
#保留换行符
win.type_keys("------type_keys------\n",with_newlines=True)
#保留空格
win.type_keys(" -----type keys----",with_spaces=True)
#延迟输入，避免输入过快导致内容不完整
win.type_keys("一二三四五六七",with_spaces=True)
```
#### 按键
 - 使用 {VK_CODE} 格式表示虚拟键码
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a091e21fddde40e2b6eca3a8bfedffe8.png#pic_center)
```python
app = Application(backend='uia').connect(process=21136)
win = app.window(title_re=".*Sublime Text.*")
win.wait('visible')

# 在Sublime中输入内容
win.type_keys("hello{ENTER}world")
```

 - 指定重复次数

```python
#发送文本和回车
win.type_keys("Hello World{ENTER 2}",with_spaces=True)
win.type_keys("Hello",with_spaces=True)
```

 - 转移特殊字符

使用 {} 包裹特殊字符（如 {+} , {%} , {^} ）以避免被识别为修饰符
```python
win.type_keys("1+2=3") # 错误：`+` 会被识别为 Shift
win.type_keys("1{+}2=3") # 正确
```
### 菜单空间的操作
#### item
返回对话框的菜单项，如果没有菜单项，则返回空列表
示例：获取菜单
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c33870f5e84c4c0daed142bac222d4df.png#pic_center)
```python
from pywinauto import Application

app = Application(backend='uia').connect(process=18624)
win = app.window(title_re=".*Sublime Text.*")
win.wait('visible')
menu = win['应用程序']
print(menu.items())

```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/4a6804b6169e4fda9f77c3ff558e2ed2.png#pic_center)
#### item_by_index()
语法： item_by_index(idx)
查找索引指定的菜单项
idx ：索引，从0开始
```python
from pywinauto import Application

app = Application(backend='uia').connect(process=18624)
win = app.window(title_re=".*Sublime Text.*")
win.wait('visible')
menu = win['应用程序']
# print(menu.items())
print(menu.item_by_index(0))
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d5770b18a45f40f29ea2032552b8bbba.png#pic_center)
#### item_by_path()
语法： item_by_path(path, exact=False)
用户查找路径指定的菜单项
path ：用于指定要选择的菜单项路径。
exact ：设置为 True，则要求菜单项名称与路径中的名称完全匹配；如果为 False，则允许模糊匹配
路径可以是“MenuItem-> MenuItem-> MenuItem ...”形式的字符串，其中每个MenuItem是菜单该
级别的项目文本。
```python
from pywinauto import Application

app = Application(backend='uia').connect(process=18624)
win = app.window(title_re=".*Sublime Text.*")
win.wait('visible')
menu = win['应用程序']
# print(menu.items())
# print(menu.item_by_index(0))
menu.item_by_path('File->Save').click_input()

```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/50abea8739104a2280b51f19eb948813.png#pic_center)
**多层菜单选项的定位**
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/cdb95f3b0ed94359b778e99e107beb6e.png#pic_center)
点击File 打开了File 窗口，点击Open Recent 会调起Open Recent 窗口
```python
from pywinauto import Application

app = Application(backend='uia').connect(process=18624)
win = app.window(title_re=".*Sublime Text.*")
win.wait('visible')
menu_bar = win.child_window(title="应用程序", auto_id="MenuBar", control_type="MenuBar")
menu_bar.item_by_path('File->Open Recent').click_input()
# win.print_control_identifiers()
openRecent = win.child_window(title="Open Recent", control_type="Menu")
openRecent.wait('visible')

clearItems = openRecent.child_window(title="Clear Items", auto_id="31", control_type="MenuItem")
clearItems.click_input()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e66aab4b45df4773b62428626a8adf04.png#pic_center)
#### menu_select()
语法： menu_select(path, exact=False)
用户查找路径指定的菜单项
path ：用于指定要选择的菜单项路径。
exact ：设置为 True，则要求菜单项名称与路径中的名称完全匹配；如果为 False，则允许模糊匹配

注意， menu_select() 的使用和上面有区别，使用 menu_select() 的场景下，通常至少有两个菜单栏：“系统”和“应用程序”系统菜单栏是一个标准的窗口菜单，包含以下项目：“还原”、“移动”、“大小”、“最小化”等。此菜单栏通常有一个“标题栏”控件作为父级。应用程序菜单栏通常是我们要找的。在大多数情况下，它的父级是对话框本身，因此可以在对话框的直接子级中找到它。
（空格不影响效果）
```python
from pywinauto import Application, mouse

app = Application(backend='uia').connect(process=18624)
win = app.window(title_re=".*Sublime Text.*")
win.wait('visible')
menuBar = win.window(title='应用程序')
menuBar.wait('visible')

# menuBar.item_by_path('File->Save').click_input()
win.menu_select('File->Save')# 和上面的具有同等的效果

```
意思就是，**menu_select**不仅查找，找到之后还选中，相当于点击

### 列表控件的操作
#### get_items()
获取列表视图中的所有项目。
```python
from pywinauto import Application

app = Application(backend='uia').connect(process=10432)
win = app.window(title_re='.*文件资源管理器')
win.wait('visible')
data_list = win.child_window(auto_id='HomeListView',control_type='List')
print(data_list.get_items())

```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/98f7cb61f34148c483e54b3069134e46.png#pic_center)
#### item_count()
列表视图中的项数
```python
from pywinauto import Application

app = Application(backend='uia').connect(process=10432)
win = app.window(title_re='.*文件资源管理器')
win.wait('visible')
data_list = win.child_window(auto_id='HomeListView',control_type='List')
# print(data_list.get_items())
print(data_list.item_count())
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c6213a0e30af4c8a847c3ec5b4e8cf44.png#pic_center)
#### get_item()
返回列表视图中的指定项目
参数：
`row`：可以是行的索引
```python
from pywinauto import Application

app = Application(backend='uia').connect(process=10432)
win = app.window(title_re='.*文件资源管理器')
win.wait('visible')
data_list = win.child_window(auto_id='HomeListView',control_type='List')
# print(data_list.get_items())
# print(data_list.item_count())
print("item: ",data_list.get_item(row=1))
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/88f6665d3b904cc19db8df370e78dad1.png#pic_center)

