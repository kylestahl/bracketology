Welcome to bracketology's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Before You Start
----------------
This package is aimed to help speed up the analysis of NCAA march madness data
and developing algorithms for filling out brackets.    

Here are the main things you need to know:
 - The main parts of this package are the `Bracket` objects and simulator functions in the simulators module
 - A Bracket is composed of `Team` and `Game` objects
 - Game objects have two Team objects as attributes, and the round number
 - Teams have a name, seed, and dictionary for statistics
 - Simulator functions have 1 argument of type Game, and return the winning Team of that Game

   
Installation
------------
Install from `PyPi <https://pypi.org/project/bracketology/>`_

.. code-block:: bash

    pip install bracketology

 
Getting Started
--------------
.. code-block:: python

    from bracketology import Bracket, Game, Team
    
    # Create a bracket object from 2019
    year = 2019
    b19 = Bracket(year)
    
Usage
-----

The main part of this package is the `Bracket` object.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
