from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='crgis.transmogrifier',
      version=version,
      description="CRGIS Transmogrifier Package",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='TsungWei Hu',
      author_email='marr.tw@gmail.com',
      url='http://github.com/l34marr/crgis.transmogrifier/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['crgis'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'SQLAlchemy',
          'psycopg2',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
