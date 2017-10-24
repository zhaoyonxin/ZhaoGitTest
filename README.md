JSON可以理解为是一种数据传输的格式，应用很普遍；
序列化，就是将原生的JS值转化为JSON字符串，实现可以使用原生JSON.stringify()方法；
反序列化，也就是序列化的相反过程，将JSON字符串解析为原生JS值，可用JSON.parse()方法来实现；
之所以要进行序列化与反序列化（或者称之为解析），主要目的就是方便进行数据的传输和处理

为什么对象序列化是objectOutputStream，而反序列化是objectInputStream？
序列化过程是把object转成字节数组，反序列化是把字节数组转化回来，所以对象序列化不应该是objectInputStream，反序列化objectOutputStream，为什么是相反的呀

初学，讨论下，因为序列化是将当前的内存中存在的对象（包括其状态）进行持久化，
并且在持久化完毕之后，可以通过反序列化的方式进行重新构建对象。
也就是说写入内存时使用的是inputSteam，写出内存使用的是outputStream，input和output是针对于内存而言的。

序列化的目的：
1、以某种存储形式使自定义对象持久化；
2、将对象从一个地方传递到另一个地方，对象的传递
3、使程序更具维护性。		

ObjectOutputStream 将 Java 对象的基本数据类型和图形写入 OutputStream。可以使用 ObjectInputStream 读取（重构）对象。通过在流中使用文件可以实现对象的持久存储。writeObject方法用来将对象写入OutputStream，而readObject方法从ObjectInputStream中读取对象的信息。与序列化的关系是ObjectInputStream 与 ObjectOutputStream 类所读写的对象必须实现了 Serializable 接口。需要注意的是：对象中的 transient 和 static 类型的成员变量不会被读取和写入 


<!DOCTYPE struts PUBLIC

	"-//Apache Software Foundation//DTD Struts Configuration 2.3//EN"

	"http://struts.apache.org/dtds/struts-2.3.dtd">

这是提前准备好的代码，希望对大家有帮助，直接复制粘贴进去即可。

Struts-2.5.13 在org.apache.struts2.dispatcher.filter.StrutsPrepareAndExecuteFilter

搞了很久，最后把web.xml改了一下就成功了。<filter-class>org.apache.struts2.dispatcher.ng.filter.StrutsPrepareAndExecuteFilter</filter-class>
高版本struts2中 过滤器的路径没有去掉“ng.”
路径应为“org.apache.struts2.dispatcher.filter.StrutsPrepareAndExecuteFilter”


HairInterface left = factory.getHairByClassName(LeftHair.class.getName());这样做与HairInterface left = factory.getHairByClassName("left")并没有本质区别，还是没有将代码进行解耦，需要修改结果的时候还是需要在代码中修改参数内容，只有将需要配置的属性脱离代码，放在配置文件中，才能最好的提高代码的可重用性。

高内聚，低耦合有助于程序的维护，单独的功能做成独立模块，整个系统由一个个模块通过接口组合而成，如果需要更新或者修改局部功能，只要修改一个接口的一个模块，不影响整个系统其他功能使用
