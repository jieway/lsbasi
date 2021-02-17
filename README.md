# 🧐 Let’s Build A Simple Interpreter.

> 荀子：“不闻不若闻之，闻之若不见之，见之不若知之，知之不若行之。”

仓库名称 lsbasi 是 Let’s Build A Simple Interpreter 首字母缩写。

原作者的 [repo](https://github.com/rspivak/lsbasi/) 。由于我想自己实现一遍，所以并没有直接 fork 原仓库。

## 🥳 提交

常用 emoji 含义如下：

* :sparkles: 引入新功能。
* :bug: 解决 bug 。
* :memo: 更新文档。	

## TODO

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
    - [ ] 程序嵌套。
    - [ ] 函数支持。
    - [ ] 函数调用。
    - [ ] 语义分析，例如类型检查。
    - [ ] 控制流，例如 if else。
    - [ ] 函数调用。
    - [ ] 增加内置数据类型。
    - [ ] 表。
    - [ ] 调试器 debugger。
    