from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='nifipy',
      version=version,
      description="Reusable NiFi Jython Scripts",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='jython nifi',
      author='Izhar Firdaus',
      author_email='kagesenshi.87@gmail.com',
      url='http://github.com/kagesenshi/nifipy',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'requests',
          'rulez',
          'PyYAML',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
