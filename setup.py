from distutils.core import setup
setup(
  name = 'bracketology',         
  packages = ['bracketology'],   
  version = '0.0.1',     
  license='MIT',        
  description = 'Analyze and simulate NCAA march madness tournaments',
  author = 'Kyle Stahl',                   
  author_email = 'stahl085@umn.edu',      
  url = 'https://github.com/stahl085/bracketology',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['brackets', 'NCAA', 'basketball', 'march', 'madness', 'tournament'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
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