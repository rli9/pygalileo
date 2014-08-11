from distutils.core import setup

setup(name = 'pygalileo', 
      version = '0.0.1',
      description = 'Python Libary to Manipulate Intel Galileo Board',
      package_dir = {'pygalileo' : 'src'},
      packages = ['pygalileo', 'pygalileo.io'],
      url = 'https://github.com/rli9/pygalileo',
      license = 'The MIT License (MIT)')