from distutils.core import setup
setup(
  name = 'bracketology',         
  packages = ['bracketology'],
  package_data={'bracketology': ['data/*']},
  version = '0.0.9',     
  license='MIT',        
  description = 'Analyze and simulate NCAA march madness tournaments',
  long_description=open('README.rst').read(),
  author = 'Kyle Stahl',                   
  author_email = 'stahl085@umn.edu',      
  url = 'https://github.com/stahl085/bracketology',   
  download_url = 'https://github.com/stahl085/bracketology/archive/0.0.4.tar.gz', 
  keywords = ['brackets', 'NCAA', 'basketball', 'march', 'madness', 'tournament'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
