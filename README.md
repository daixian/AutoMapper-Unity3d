在Unity3d中使用AutoMapper
--------------------------------
### 特性
* 主要是支持IL2CPP

### 为什么选择AutoMapper4.2.1 
它后面的版本加了一个ExpressionFactory类，并且取消了DelegateFactory类的接口定义，要难改很多，所以选择从这个版本开始修改。

### 一点个人观点 
这整个库里面，System.Linq.Expressions反复用，真的有必有吗？