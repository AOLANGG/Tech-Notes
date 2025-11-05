YAML是⼀种数据序列化语⾔，⽤于以⼈类可读的形式存储信息。它最初代表“Yet Another Markup Language”，但后来更改为“ YAML Ain’t Markup Language”（YAML不是⼀种标记语⾔），以区别于真正的标记语⾔。

它类似于XML和JSON⽂件，但使⽤更简洁的语法。

## 介绍
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/ed3ab325a2f04acdac73d5e954d563c0.png)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/662ee5e0b92949de8381bbe4c3cc4bc4.png)
## 使用
yaml ⽂件通常作为配置⽂件来使⽤，可以使⽤ aml 库来读取和写⼊ YAML ⽂件
安装
```
pip install PyYAML==6.0.1
```
读取和写入yaml文件
```python
import yaml


# 追加写入
def write_yaml(filename,data):
    with open(filename,'a+',encoding='utf-8') as f:
        yaml.safe_dump(data,f)

# 读取
def read_yaml(filename,key):
    with open(filename,'r',encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data[key]

# 清空
def clear_yaml(filename):
    with open(filename,'w',encoding='utf-8') as f:
        f.truncate()

def test_yaml():
    data = {'apple':"苹果"}
    write_yaml('data.yml',data)
    ret = read_yaml('data.yml','apple')
    print(ret)
    clear_yaml('data.yml')

```
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/40404399b5ac4a0caa49f2296be49477.png)

