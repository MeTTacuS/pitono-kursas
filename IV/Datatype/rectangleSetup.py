from distutils.core import setup, Extension

module = Extension("Rectangle", sources = ["rectangleModule.c"])

setup(name="RectangleModule",
	ext_modules = [module])

# python3 rectangleSetup.py install --user
# python3
# >>> import Rectangle
# >>> r = Rectangle.Rectangle(3,4)
# >>> r.perimeter()
# >>> r.area()