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
A simulator function needs to take in a `Game` and Return a `Team`.

First we create some faux teams and games to test our simulator function on.

.. code-block:: python

    # Create teams
    team1 = Team(name='Blue Mountain State',seed=1)
    team2 = Team(name='School of Hard Knocks',seed=2)
    ​
    # Create a game between the teams
    game1 = Game(team1, team2, round_number=1)

Then we define the simulator function.

.. code-block:: python

    import random
    def pick_a_random_team(the_game):
        
        # Extract Teams from Game
        team1 = the_game.top_team
        team2 = the_game.bottom_team
    ​
        # Randomly select a winner
        if random.random() < 0.5:
            winner = team1
        else:
            winner = team2
           
        # Return the lucky team
        return winner
​
Test the function out on a game.

.. code-block:: python

    >>> pick_a_random_team(game1)
    <2 School of Hard Knocks>

Let's run some simulations with our function!

.. code-block:: python

    # Initialize Simulation Parameters
    BMS_wins = 0
    HardKnocks_wins = 0
    n_games = 1000
    ​
    # Loop through a bunch of games
    for i in range(n_games):
        
        # Simulate the winner
        winner = pick_a_random_team(game1)
        
        # Increment win totals
        if winner.seed == 1:
            BMS_wins += 1
        elif winner.seed == 2:
            HardKnocks_wins += 1
        else:
            raise Exception("We have a tie??")
    ​
    # Calculate total win percentage
    BMS_win_pct = round(BMS_wins/n_games, 4) * 100
    HardKnocks_win_pct = round(HardKnocks_wins/n_games, 4) * 100
    ​
    # Print out results
    print(f"Blue Mountain State Win Percentage:   %{BMS_win_pct}")
    print(f"School of Hard Knocks Win Percentage: %{HardKnocks_win_pct}")
  
Output:

.. code-block:: python 

    Blue Mountain State Win Percentage:   %50.9
    School of Hard Knocks Win Percentage: %49.1


Evaluting Simulator Results
---------------------------

Let's evaluate our simulator function on some actual brackets.

.. code-block:: python
    
    # Initialize simulation parameters
    n_sims = 1000 # number of times to simulate through all years
    total_sims = (n_sims * len(brackets))
    scores = []
    correct_games = []
    
    # Loop through a plethora of brackets
    for i in range(n_sims):
        for bracket in brackets:
            
            # Run the algorithm on the bracket
            bracket.score(sim_func=pick_a_random_team, verbose=False)
            
            # Save the scoring results in a list
            scores.append(bracket.total_score)
            correct_games.append(bracket.n_games_correct)
    
    # Calculate the average across all simulations
    avg_score = round(sum(scores) / total_sims)
    avg_correct = round(sum(correct_games) / total_sims)
    
    # Print result
    print(f"Average number total score {avg_score}/192")
    print(f"Average number of games guessed correctly {avg_correct}/64")
 
Output:

.. code-block:: python

    Average number total score 31/192
    Average number of games guessed correctly 21/64


Easy, right!



