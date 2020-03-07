Welcome to Bracketology!
========================

.. figure:: docs/_static/bracketology_logo.png
   :width: 100%
   :align: center
   :alt: Bracketology logo

.. inclusion-marker-do-not-remove
   
The goal of bracketology is to speed up the analysis of NCAA march madness data 
and help develop algorithms for filling out brackets.  

:Documentation: https://bracketology.readthedocs.io/en/latest/
:GitHub Repo: https://github.com/stahl085/bracketology
:Issue Tracker: https://github.com/stahl085/bracketology/issues
:Backlog: https://github.com/stahl085/bracketology/projects/1?fullscreen=true
:PyPI: https://pypi.org/project/bracketology/

Before You Start
----------------  

Here are the main things you need to know:
 - The main parts of this package are the :code:`Bracket` objects and simulator functions in the :code:`simulators` module
 - A Bracket is composed of :code:`Team` and :code:`Game` objects
 - Game objects have two Team objects as attributes, and the round number
 - Teams have a name, seed, and dictionary for statistics
 - Simulator functions have 1 argument of type Game, and return the winning Team of that Game

   
Installation
------------

Install from `pip <https://pip.pypa.io/en/stable/>`_

.. code-block:: bash

    pip install bracketology

Or download directly from `PyPi <https://pypi.org/project/bracketology/>`_

Getting Started
---------------
Import bracketology and create a bracket from last year.

.. code-block:: python

    from bracketology import Bracket, Game, Team
    
    # Create a bracket object from 2019
    year = 2019
    b19 = Bracket(year)
    
Tutorial
========

Inspecting the Bracket Object
-----------------------------
Here are three different ways you can inspect the Bracket.    

 * Inspect teams in each region (dictionary of actual results)
 * Inspect actual results by round (dictionary)
 * Inspect simulated results by round (list of Team attributes)

Get Teams in each Region
~~~~~~~~~~~~~~~~~~~~~~~~

Print out all the teams in each region. The `regions` attribute is
a dictionary with the information of all the teams in each region.

.. code-block:: python

    >>> print(b19.regions)
    {
        'East': [{'Team': 'Duke', 'Seed': 1}, 
                 {'Team': 'Michigan St', 'Seed': 2}, 
                 {'Team': 'LSU', 'Seed': 3}, 
                 ...],
        'West': [{'Team': 'Gonzaga', 'Seed': 1}, 
                 {'Team': 'Michigan', 'Seed': 2}, 
                 {'Team': 'Texas Tech', 'Seed': 3},
                 ...],
        'Midwest': [{'Team': 'North Carolina', 'Seed': 1}, 
                    {'Team': 'Kentucky', 'Seed': 2}, 
                    {'Team': 'Houston', 'Seed': 3},
                    ...],
        'South': [{'Team': 'Virginia', 'Seed': 1}, 
                  {'Team': 'Tennessee', 'Seed': 2}, 
                  {'Team': 'Purdue', 'Seed': 3},
                  ...]
    }

Actual Results by Round
~~~~~~~~~~~~~~~~~~~~~~~

The `result` attribute will return a dictionary (similar to `regions` above)
but will be broken out by which teams actually made it to each round. You can 
use it to inspect the real tournament results.

.. code-block:: python

    >>> print(b19.result.keys())
    dict_keys(['first', 'second', 'sweet16', 'elite8', 'final4', 'championship', 'winner'])
    
    >>> print(b19.result['final4'])
    [{'Team': 'Michigan St', 'Seed': 2}, {'Team': 'Virginia', 'Seed': 1}, 
     {'Team': 'Texas Tech', 'Seed': 3}, {'Team': 'Auburn', 'Seed': 5}]
    
    >>> print(b19.result.get('winner'))
    {'Team': 'Virginia', 'Seed': 1}    

Simulation Results by Round
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print out all the teams that are simulated to make it to each round.
The first round is filled out by default. This is a list of `Team` objects
that are simulated to make it to each round. Right now `round2` is an empty list
because we have not simulated the bracket yet.

.. code-block:: python
    
    >>> print(b19.round1)
    [<1 Duke>, <2 Michigan St>, <3 LSU>, ... , <1 Gonzaga>, <2 Michigan>, <3 Texas Tech>, 
     ... , <1 North Carolina>, <2 Kentucky>, <3 Houston>, ... , <1 Virginia>, <2 Tennessee>, <3 Purdue>]
        
    >>> print(b19.round2)
    []

Creating a Simulator Algorithm
-------------------------------
A simulator needs to take in a Game and Return a Team

.. code-block:: python

    team1 = Team(name='Blue Mountain State',seed=1)
    team2 = Team(name='School of Hard Knocks',seed=2)
    
    game1 = Game(team1, team2, round=1)

.. code-block:: python

    def pick_a_random_team(Game):
        return Team

Evaluting Simulator Results
---------------------------

Here we can evaluate two different simulators

.. code-block:: python
    
    # TBD








