# bracketology
The bracketology package is aimed at creating an easy to use interface for 
analyzing historical NCAA mens basketball tournament data & simplify the
process of creating and evaluting bracket prediction algorithms.

## Bracket
The main feature of bracketology is the `Bracket` python object.

### Anatomy of Bracket
Initialize an instance of `Bracket` with a year between 1985 and 2019.

```
b19 = Bracket(2019)
```

This creates a bracket object with the teams that made the tournament in 2019.
A `Bracket` is composed of 4 `SubBracket16` objects for each region and a `FinalFour` object.

Each `SubBracket16` is composed of 5 rounds (first round until final four), and
each round is a list of `Game` objects (with the exception of the final round which
is a `Team` object).

Each `Game` is made up of two `Team` objects and a round number.

The `Team` object has three attributes `name (str)`, `seed (int)`, and `stats (dict)`.

`Bracket` also has a `result` attribute which is a dictionary 
that holds the actual bracket results for the given year.

### Usage of Bracket
The `.sim()` and `.score()` methods are what give this module it's power.
They can take a simulating algorithm, fill out the bracket with that algorithm,
and calcualte the number of games correct as well as calculating the total score.

```
b19 = Bracket(2019)
b19.score(sim_func=upset_prob(0.0))

_Number of games correct: 41/63_
_Total Score: 92/192_
```
Total score is based off a scoring system with 32 points per round.
Each game is worth 32/(number of games in that round).

#### What is a _"simulating algorithm"?_
The `.sim()` and `.score()` methods take a `sim_func` argument.
This argument should be a python function. The function needs to take in 
an object of type `bracketology.Game` _(which contains to `Team` objects)_
and return a `bracketology.Team` object that represents the winner of the game.

This can be any function that can take into account the seeds, tournament round, 
and statistics of the two teams to make a decision about which one should be the winner.

This package comes pre-loaded with some simulator functions in the `bracketology.simulators` module.




