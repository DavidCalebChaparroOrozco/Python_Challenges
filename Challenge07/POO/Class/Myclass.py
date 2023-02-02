class MyClass:

    variable_class = 'Variable value class'

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    # Method static
    @staticmethod
    def static_method():
        print(MyClass.variable_class)

    # Class methods
    @classmethod
    def class_method(cls): # cls = class
        print(cls.variable_class)

    # Static and dynamic context
    def method_instance(self):
        self.class_method()
        self.static_method()
        print(self.variable_class)
        print(self.instance_variable)

# print(MyClass.variable_class)
# myClass = MyClass('Variable instance value')
# print(myClass.instance_variable)
# print(myClass.variable_class)
#
# # Creating dynamic variables
# MyClass.variable_class2 = 'Variable value class 2'
#
# myClass2 = MyClass('Other instance variable value')
# print(myClass2.instance_variable)
# print(myClass2.variable_class)
# print(''.center(50,'-'))
# print(MyClass.variable_class2)
# print(myClass.variable_class2)
# print(myClass2.variable_class2)

# # Method static
# MyClass.static_method()
#
# print(''.center(50,'-'))
#
# # Class methods
MyClass.class_method()

# Static and dynamic context
myObject1 = MyClass('instance_variable')
myObject1.class_method()
myObject1.method_instance()