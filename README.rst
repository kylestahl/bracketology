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
This is how you can look at your brackets

.. code-block:: python

    b19.regions
    # or
    b19.round1
    # or
    b19.result.get('first')

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








