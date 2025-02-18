from setuptools import setup

setup(name='samet_core',
      version='1.3.8',
      description='samet main functions',
      author='MalKeMit',
      author_email='khodemalkemit@gmail.com',
      url='', # or your new samet repo
      setup_requires=['wheel'],
      install_requires=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6']
      )