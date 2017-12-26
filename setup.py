from setuptools import setup, find_packages

setup(name='osmstats',
      version='1.1',
      description='Processes OpenStreetMap XML file for deriving statistics',
      author='Prasanna Venkadesh',
      author_email='prasmailme@gmail.com',
      url='https://github.com/PrasannaVenkadesh/osmstats',
      install_requires=['lxml==4.1.1'],
      python_requires='>=2.7',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'License :: OSI Approved :: GNU General Public License (GPL)',

          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython'
      ],
)
