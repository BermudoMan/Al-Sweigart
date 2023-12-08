class Person:
    def say(self, massage):
        print(massage)
    def say_hello(self):
        self.say('Hello work')


tom = Person()
tom.say_hello()