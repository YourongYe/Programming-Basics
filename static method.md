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
