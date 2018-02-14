from setuptools import setup

setup(name ="systeminfo2",
      version="0.1",
      description= "Basic system information for COMP30670",
      author="Gary Cremins",
      author_email="gary.cremins1@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo2'],
      entry_points={
          'console_scripts':['EclipseWorkspace2_systeminfo2=systeminfo2.main:main']
          }
      )
