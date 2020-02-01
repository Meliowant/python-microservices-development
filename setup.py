from setuptools import setup, find_packages

setup(name="runnerly",
      version="0.1",
      packages=find_packages(),
      install_requires=[
          'flask',
          'flask_sqlalchemy'
      ],
      include_package_data=True,
      zip_safe=False)
