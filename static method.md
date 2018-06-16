  # Static method vs class method vs normal method
    class test:
      name = 'class name'

      def normalmethod(self,name):
        print(self.name)

      @classmethod
      def class_method(cls,name):
        print(cls.name)

      @staticmethod
      def static_method(name):
        print(name)


    obj = test()
    obj.name = 'instance name'

    obj.normalmethod('name')
    obj.class_method('name')
    obj.static_method('name')
 
 
 # Result
    instance name
    class name
    name

conclusion: 三种方法都可以被实例调用，但是static method 和 class method 不能访问实例方法（属性），只有普通方法才可以调用实例属性
 
 # Test2
    test.class_method('name')
    test.static_method('name')
    #test.normalmethod('name')
    
    #result:
    class name
    name

conclusion: 只有static method和class method可以被类名调用，而普通方法被类名调用时会报错
