
![Logo](docs/_static/bracketology_logo.png)

The bracketology package is aimed at creating an easy to use interface for 
analyzing historical NCAA mens basketball tournament data & accelerating the
process of creating and evaluting bracket prediction algorithms.

## Documentation

Documentation is hosted by [Read The Docs](https://bracketology.readthedocs.io/en/latest/#)

## Installation

Get the package from [PyPi](https://pypi.org/project/bracketology/#):
```
pip install bracketology
```

## Usage: Hello Bracket!
Create a Bracket object
```
from bracketology import Bracket, Game, Team
b19 = Bracket(2019)
```

Check out the teams that made it that year
```
b19.regions
# or
b19.round1
# or
b19.result.get('first')
```

Simulate a result
```
from bracketology.simulators import upset_prob
b19.score(upset_prob(0.15))
```

## Table of Contents

#### _/bracketology_
This is for the actual package files; what gets uploaded to PyPi 
and downloaded when you `pip install bracketology`.

#### _/docs_
This folder contains the files to create the Read The Docs documentation.
The structure was automatically generated with [Sphinx-quickstart](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)    

The file `index.rst` contains the main info for the documentation.

#### _/notebooks_
Some Jupyter notebooks for the original data cleaning, exploratory analysis,
and (eventually) some baseline modeling. 

#### _setup.py, setup.cfg, and MANIFEST_
These are used for uploading the package to PyPi.


## Contributing
This project is still in it's nascent stages. There is plenty of room to contribute! 
Feel free to branch or fork this repo and PR for contributing, or just have it for personal use.

At the moment, there is not strict coding standards. But any PR's should be
comprehensible and have comments where neccessary.

If you are passionate about this topic and have large scale feature ideas, 
or any ideas on how to better achieve the goals of this package, feel free to reach out! 
I would love to work with you to make this better for everyone.     

Maybe one day we will get a perfect bracket.

Message me on [LinkedIn](https://www.linkedin.com/in/kyle-stahl-mn/)     
or Email: stahl085@umn.edu

## Future Developement
Big ticket feature in progress
 - adding regular season data for each team each year
 - more robust error handling
 - adding more simulator functions to go with each package
 - TBD





