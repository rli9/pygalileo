from distutils.core import setup

setup(name='pyquark',
      version='0.0.2',
      description='Python Libary to Manipulate Intel Quark based board (support Galileo now)',
      package_dir={'pyquark' : 'src'},
      packages=['pyquark', 'pyquark.io', 'pyquark.nxt', 'pyquark.arduino'],
      url='https://github.com/rli9/pyquark',
      license='The MIT License (MIT)')
