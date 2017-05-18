# -*- codeing:utf-8 -*-
import os
__author__ = 'Buguin'


print(os.name)
print(os.environ['PATH'])
print(os.getlogin())

print(os.supports_bytes_environ)
os.supports_bytes_environ = True
print(os.supports_bytes_environ)
print(os.getcwdb())
print(os.fsencode('Filename'))
str = os.PathLike().__fspath__
print(str)

