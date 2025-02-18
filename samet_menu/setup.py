from setuptools import setup

setup(name='samet_menu',
      version='1.0.0',
      description='samet menu',
      author='',
      author_email='@gmail.com',
      url='', # or your new samet repo
      setup_requires=['wheel'],
      install_requires=['colored~=1.4.4',
                        'pyfiglet~=0.8.post1',
                        'prettytable~=3.5.0']
      )
