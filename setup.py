from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(name='t',
      version='0.1',
      description='CLI tool for removing files safely.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/adamheins/t',
      author='Adam Heins',
      author_email='mail@adamheins.com',
      install_requires=['docopt'],
      license='MIT',
      scripts=['t'],
      python_requires='>=3.5',
      zip_safe=False)
