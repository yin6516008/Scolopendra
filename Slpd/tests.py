from django.test import TestCase

# Create your tests here.


class ff(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def dd(self,name,age):
        return name,age

cc = ff('yin',19)

if hasattr(cc,'dd'):
    str = getattr(cc,'dd')
    ss = str('yin',19)
    print(ss)


