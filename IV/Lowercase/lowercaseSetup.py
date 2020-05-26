from distutils.core import setup, Extension

# python3 lowercaseSetup.py build
# python3 lowercaseSetup.py install --user
# python3
# >>> import LowercaseModule
# >>> LowercaseModule.AreLowercase("zodis")

module = Extension("LowercaseModule", sources = ["lowercaseModule.c"])

setup(name="LowercaseModule",
	ext_modules = [module])
