# dic命令行查词工具

## 简介

- 方便用命令行查一查变量名什么的(逃

## 使用方法

1. 在根目录创建`setting.py`文件, 写入自己的金山词霸API的KEY
    ```py
    API_KEY = 'xxx'
    ```
2. windows使用pyinstaller直接打包即可
    ```shell
    pyinstaller -F dic.py
    ```
1. 可以将打包好的exe文件加入到系统环境变量
- 使用方法: `dic 想查的词`
    ```shell
    dic hello
    dic 行
    ```
