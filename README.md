在Unity3d中使用AutoMapper
--------------------------------

[![Build status](https://daixian.visualstudio.com/Pipeline/_apis/build/status/Pipeline%20-%20AutoMapper-Unity3d)](https://daixian.visualstudio.com/Pipeline/_build/latest?definitionId=10)

### 特性
* 主要是支持IL2CPP。
* 应该只保证了部分功能，不过unity3d用足够了。
* 在Unity2019.3.0f1上使用目前没什么问题，更低的版本可能link.xml要修改增加更多的类型。

### AutoMapper和IL2CPP
* AutoMapper库很好用，但是直接使用IL2CPP的发布方式下肯定用不了。大概你会看到如下的错误:
    ``` S
    NullReferenceException: Object reference not set to an instance of an object.
      at System.Linq.Expressions.Interpreter.LightLambda.MakeRunDelegateCtor (System.Type delegateType) [0x00000] in <00000000000000000000000000000000>:0 
      at System.Linq.Expressions.Interpreter.LightLambda.GetRunDelegateCtor (System.Type delegateType) [0x00000] in <00000000000000000000000000000000>:0 
      at System.Linq.Expressions.LambdaExpression.Compile (System.Runtime.CompilerServices.DebugInfoGenerator debugInfoGenerator) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.MapperConfiguration.CreateMapperFuncs (AutoMapper.MapRequest mapRequest) [0x00000] in <00000000000000000000000000000000>:0 
      at System.Func`2[T,TResult].Invoke (T arg) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.LockingConcurrentDictionary`2+<>c__DisplayClass2_1[TKey,TValue].<.ctor>b__1 () [0x00000] in <00000000000000000000000000000000>:0 
      at System.Func`1[TResult].Invoke () [0x00000] in <00000000000000000000000000000000>:0 
      at System.Lazy`1[T].CreateValue () [0x00000] in <00000000000000000000000000000000>:0 
      at System.Lazy`1[T].LazyInitValue () [0x00000] in <00000000000000000000000000000000>:0 
      at System.Lazy`1[T].get_Value () [0x00000] in <00000000000000000000000000000000>:0 
      at Newtonsoft.Json.Serialization.DefaultContractResolver+EnumerableDictionaryWrapper`2[TEnumeratorKey,TEnumeratorValue]..ctor (System.Collections.Generic.IEnumerable`1[T] e) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.MapperConfiguration.GetUntypedMapperFunc (AutoMapper.MapRequest mapRequest) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.Mapper.Map[TDestination] (System.Object source) [0x00000] in <00000000000000000000000000000000>:0 
      at MagicBook.data.mapper.DataMapper.toModel (System.Collections.Generic.List`1[T] list) [0x00000] in <00000000000000000000000000000000>:0 
      at MagicBook.book.NavigationPage.build (Unity.UIWidgets.widgets.BuildContext context) [0x00000] in <00000000000000000000000000000000>:0 
      at System.Threading.ContextCallback.Invoke (System.Object state) [0x00000] in <00000000000000000000000000000000>:0 
      at System.Threading.ExecutionContext.RunInternal (System.Threading.ExecutionContext executionContext, System.Threading.ContextCallback callback, System.Object state, System.Boolean preserveSyncCtx) [0x00000] in <00000000000000000000000000000000>:0 
      at System.Runtime.CompilerServices.AsyncMethodBuilderCore+MoveNextRunner.Run () [0x00000] in <00000000000000000000000000000000>:0 
      at Unity.UIWidgets.gestures.GestureDragCancelCallback.Invoke () [0x00000] in <00000000000000000000000000000000>:0 
      at Unity.UIWidgets.foundation.ValueChanged`1[T].Invoke (T value) [0x00000] in <00000000000000000000000000000000>:0 
      at UnityEngine.WaitForSecondsRealtime.get_keepWaiting () [0x00000] in <00000000000000000000000000000000>:0 
      at UnityEngine.UnitySynchronizationContext.Exec () [0x00000] in <00000000000000000000000000000000>:0 
    --- End of stack trace from previous location where exception was thrown ---
      at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw () [0x00000] in <00000000000000000000000000000000>:0 
      at System.Runtime.CompilerServices.AsyncMethodBuilderCore+<>c.<ThrowAsync>b__6_0 (System.Object state) [0x00000] in <00000000000000000000000000000000>:0 
      at Unity.UIWidgets.foundation.ValueChanged`1[T].Invoke (T value) [0x00000] in <00000000000000000000000000000000>:0 
      at UnityEngine.WaitForSecondsRealtime.get_keepWaiting () [0x00000] in <00000000000000000000000000000000>:0 
      at UnityEngine.UnitySynchronizationContext.Exec () [0x00000] in <00000000000000000000000000000000>:0 
    UnityEngine.Logger:LogException(Exception, Object)
    UnityEngine.Debug:LogException(Exception)
    UnityEngine.WaitForSecondsRealtime:get_keepWaiting()
    UnityEngine.UnitySynchronizationContext:Exec()
    ```  
    当你把System.Reflection.Emit加进来之后,你大概会看到:
    ``` S
    NotSupportedException: System.Reflection.Emit.DynamicMethod::.ctor
      at System.Reflection.Emit.DynamicMethod..ctor (System.String name, System.Type returnType, System.Type[] parameterTypes, System.Type owner, System.Boolean skipVisibility) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.DelegateFactory.CreateDynamicMethod (System.Reflection.MemberInfo member, System.Type sourceType) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.DelegateFactory.CreateSet (System.Reflection.PropertyInfo property) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.Internal.PropertyAccessor..ctor (System.Reflection.PropertyInfo propertyInfo) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.ReflectionHelper.ToMemberAccessor (System.Reflection.MemberInfo accessorCandidate) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.TypeMapFactory.CreateTypeMap (System.Type sourceType, System.Type destinationType, AutoMapper.IMappingOptions options) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.Configuration.CreateTypeMap (System.Type source, System.Type destination, System.String profileName) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.Configuration.CreateMap (System.Type sourceType, System.Type destinationType, System.String profileName) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.Configuration.CreateMap (System.Type sourceType, System.Type destinationType) [0x00000] in <00000000000000000000000000000000>:0 
      at System.Action`1[T].Invoke (T obj) [0x00000] in <00000000000000000000000000000000>:0 
      at AutoMapper.Mapper.Initialize (System.Action`1[T] action) [0x00000] in <00000000000000000000000000000000>:0 
      at MagicBook.data.mapper.Test.TestMapper () [0x00000] in <00000000000000000000000000000000>:0 
    ```
    这主要是由于AutoMapper里面动态创建Lambda表达式造成的。关于现在IL2CPP对这一块的支持可以参考这里<https://forum.unity.com/threads/are-c-expression-trees-or-ilgenerator-allowed-on-ios.489498/> 
* 为什么选择AutoMapper的4.2.1版本，主要是6.0以上版本修改难度加大，加了一个ExpressionFactory类，并且取消了DelegateFactory类的接口定义，要难改很多，所以选择从这个版本开始修改。改的地方不多，主要是去掉这个动态生成表达式。
* 开始我准备用5.2.0版本，看了一下代码之后又选择降成了4.2.1，不折腾。

### 个人看法
* AutoMapper库的源码里Tab和空格并存，CRLF和LF并存，很蛋疼。
* 这整个库里面，System.Linq.Expressions反反复复用，真的有必有吗？？

### 使用
IL2CPP会有裁剪代码，这个是参考link.xml文件：
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<linker>
  <assembly fullname="Newtonsoft.Json" preserve="all" />
  <assembly fullname="Assembly-CSharp" preserve="all" />
  <assembly fullname="ThirdPartyLib" preserve="all" />
  <assembly fullname="AutoMapper" preserve="all" />
  <assembly fullname="System" preserve="all">
    <type fullname="System.ComponentModel.TypeConverter" preserve="all"/>
    <type fullname="System.ComponentModel.ArrayConverter" preserve="all"/>
  </assembly>
  <!--<assembly fullname="System.Core" preserve="all">
  </assembly>-->
</linker>
```

AutoMapper在unity里的测试代码，也是目前支持的用法。AutoMapper的其他高级用法咱也不会，能支持自定义mapper方法基本够用了=。= 简单的测试代码如下：
``` CSharp
public class C1
{
    public string a { get; set; }
    public string b { get; set; }
    public string c { get; set; }
    public string d;
}

public class C2
{
    public string a { get; set; }
    public string b { get; set; }
    public string c { get; set; }
    public string d;
}

//...
public void TestMapper()
{
    Debug.Log("Test.TestMapper():执行Mapper的简单测试");

    Mapper.Initialize((cfg) => {
        //创建一个List转到string的自定义mapper方法
        cfg.CreateMap<List<string>, string>().ConvertUsing(new Func<List<string>, string>(ls => JsonConvert.SerializeObject(ls)));
        cfg.CreateMap<string, List<string>>().ConvertUsing(new Func<string, List<string>>(s => JsonConvert.DeserializeObject<List<string>>(s)));

        //映射忽略c属性
        cfg.CreateMap(typeof(C1), typeof(C2)).ForMember("c", opt => opt.Ignore());
    });


    List<string> listStr = new List<string> { "1", "2", "3", "4" };

    string str = Mapper.Map<List<string>, string>(listStr);
    Debug.Log("Test.TestMapper():str = " + str);
    List<string> listStr2 = Mapper.Map<string, List<string>>(str);
    for (int i = 0; i < listStr.Count; i++) {
        Debug.Assert(listStr[i] == listStr2[i], "Test.TestMapper():执行List<string>测试失败!");
    }

    C1 o1 = new C1();
    o1.a = "1";
    o1.b = "2";
    o1.c = "3";
    o1.d = "4";
    C2 o2 = Mapper.Map<C1, C2>(o1);

    Debug.Assert(o1.a == o2.a, "Test.TestMapper():o1.a == o2.a测试失败!");
    Debug.Assert(o1.b == o2.b, "Test.TestMapper():o1.b == o2.b测试失败!");
    Debug.Assert(o2.c == default, "Test.TestMapper():o1.c ignore 测试失败!");
    Debug.Assert(o1.d == o2.d, "Test.TestMapper():o1.d == o2.d测试失败!");
    Debug.Log("Test.TestMapper():Mapper的简单测试结束");
}
```
如果要构造不同的名字的属性映射，可能最好直接使用表达式，因为下面的方法目前只写了获取属性名。
``` CSharp
public class C1
{
    public byte[] a { get; set; }
}

public class C2
{
    public byte[] b { get; set; }
}

//C1.a -> C2.b

//work,recommend 
cfg.CreateMap<C1, C2>()
    .ForMember("b", opt => opt.MapFrom(s => s.a));

//work,not recommend 
cfg.CreateMap<C1, C2>()
    .ForMember("b", opt => opt.MapFrom<byte[]>("a"));
```