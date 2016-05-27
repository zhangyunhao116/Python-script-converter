# **Python-script-converter**

[![PyPI](https://img.shields.io/pypi/v/yagmail.svg?style=flat-square)]()
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)]()

[English introduction click here](https://github.com/ZYunH/Python-script-converter/blob/master/Readme.md)

## 介绍：

​	这是一个简单的工具，作用是将一个python脚本直接转换为可执行文件(只供mac和Linux系统使用)。如此，你可以在系统的任何地方运行这个脚本。

## 安装

注:可在你的脚本程序首行加入#!/usr/bin/env python 或者#!/usr/bin/env python3 来指定解释器。这样使用psc时不需要指定版本号。

### Option 1:通过pip安装（推荐）

```
$ pip3 install python-script-converter
```

你也可以使用pip

### Option 2:从Github从下载最新版本

解压下载的zip文件，然后切换到解压后的目录

```
$ [sudo] python3 setup.py install
```

你也可以使用python

## 如何使用：

使用之前，你必须确保：

- 你的系统是Mac OS 或者LInux

下面演示如何使用 `psc`  来将一个脚本转换至可执行程序

#### 如果你的脚本基于python3.x

```
$ psc test.py
```

或者使用绝对路径

```
$ psc /Users/zyh/test.py
```

#### 如果你的脚本基于python2.x

```
$ psc test.py 2
```

or

```
$ psc /Users/zyh/test.py 2
```

之后，你就可以得到一个与脚本名字相同，但是扩展名为 **.command** 的可执行文件。**程序不会改变你原来的脚本文件**。
