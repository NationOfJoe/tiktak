from setuptools import setup, find_packages

setup(name='TikTak',
      version='0.0.5',
      description='a simulation of the old game tik-tak',
      author='Yoav Ekshtein',
      url='',
      license='',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'Programming Language :: Python :: 2.7',
                   'License :: OSI Approved :: MIT License'],
      packages=find_packages(exclude=['tests']),
      entry_points={'console_scripts': ['TikTak = game.user_interface:__main__']},
      install_requires=[""])