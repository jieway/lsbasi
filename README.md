# 🧐 Let’s Build A Simple Interpreter.

> 荀子：“不闻不若闻之，闻之若不见之，见之不若知之，知之不若行之。”

仓库名称 lsbasi 是 Let’s Build A Simple Interpreter 首字母缩写。

原作者的 [repo](https://github.com/rspivak/lsbasi/) 。由于我想自己实现一遍，所以并没有直接 fork 。

顺便写了一个[踩坑记录](https://blog.weijiew.com/2021/02/22-lsbasi-summary/)，主要记录学习过程中遇到问题的解决方案以及一些心得体会。

## 🥳 Commit

常用 emoji 含义如下：

* :sparkles: 引入新功能。
* :bug: 解决 bug 。
* :memo: 更新文档。	

## 🎉 TODO

从算术表达式开始逐步扩展，几乎任何语言都支持算术表达式。

- [x] 算术表达式。
    - [x] 不带空格的一位整数加法。
    - [x] 支持多位整数，跳过空格功能。支持减法。
    - [x] 多个多位整数的加减法。
    - [x] 乘除实现。
    - [x] 加减乘除混合后的优先级处理。
    - [x] 支持括号。
    - [x] 语法分析树改为抽象语法树（AST）。
    - [x] 观察者模式。
    - [x] 支持一元表达式。

- [x] Pascal 解释器：
    - [x] 处理 Pascal 关键字 token。
    - [x] 支持解析 Pascal header 。
    - [x] 采用 div 来做整数除法，采用 / 来做浮点数除法。
    - [x] 支持 Pascal 注释。
    - [x] 支持函数。
    - [x] 符号表。
        - [x] 不定义就使用报错处理。
        - [x] 重复定义报错处理。
    - [x] 作用域嵌套及对应符号表管理。
    - [x] 报错处理。（提供行号和列号以及错误类型等信息）
