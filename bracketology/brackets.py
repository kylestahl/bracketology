import json
from pkg_resources import resource_filename
filepath = resource_filename('bracketology', 'data/brackets.json')
with open(filepath, 'r') as f:
    brackets_dict = json.load(f)

class Team():
    """
    A team that is in a Game or a Bracket
    
    Attributes
    ----------
    name : str
        Name of the school (or abbreviation)
    seed : int
        Seed of the team in the tournament (1-16)
    stats : (dict)
        A dictionary with other information about the team, like season stats
    """
    def __init__(self, name, seed):
        """
        Parameters
        ----------
        name : str
            The name of the school for the team.
        seed : int
            The seed of the team in the bracket.
        """
        if type(name) != str: raise TypeError("name needs to be of type str")
        if type(seed) != int: raise TypeError("seed needs to be of type int")
        self.name = name
        self.seed = seed
        self.stats = {}
    def __repr__(self):
        return f"<{self.seed} {self.name}>"

class Game():
    """
    A game between two teams in the bracket
    
    Attributes
    ----------
    top_team : Team
        The "top team" in the game refers to bracket position, not seed
    bottom_team : Team
        The "bottom team" in the game refers to bracket position, not seed
    round_number : int
        Which round of the tournament is it (1-6)
    """
    def __init__(self, top_team, bottom_team, round_number):
        """
        Parameters
        ----------
        top_team : Team
            The top team of the game, not by seed but by position on the bracket.
            Closest to the top left
        bottom_team : Team
            Team closest to the bottom right of the bracket
        round_number : int
            Round number, first round is 1, championship game is 6

        """
        #if not isinstance(top_team, Team): raise TypeError("top_team must be Type Team")
        #if not isinstance(bottom_team, Team): raise TypeError("bottom_team must be Type Team")
        self.top_team = top_team
        self.bottom_team = bottom_team
        self.round_number = round_number
    def __repr__(self):
        return f"<Round {self.round_number}: Top Team: {self.top_team} , Bottom Team: {self.bottom_team}>\n"

class SubBracket16():
    """
    A region, or sub-bracket of 16 teams for a NCAA tournament
    
    Attributes
    ----------
    region : str
        Name of the region for the bracket
    team01, ..., team16 : Team
        Each team in the subracket named for its seed
    Game1, ..., Game15 : Game
        The games that make up the bracket. Round 1 is 1-8, 
        Round 2 is 9-12, Sweet 16 is 13 and 14, Final Four is 15
    round1, ..., round6 : list
        List of games in each round
    winner : Team
        The team from this region that is simulated to make the final four
    """
    def __init__(self, region):
        """
        Parameters
        ----------
        region : str
            Name of the region for this sub bracket.
        """
        # Set region
        self.region = region
        self.round1 = [] # first round will have 16 teams
        self.round2 = [] # 8 teams left in region
        self.round3 = [] # sweet 16, 4 teams left in region
        self.round4 = [] # elite 8, 2 teams left in region
        self.winner = None # Initalize as None until winner is set

    
    def initialize_first_round(self, teams):
        # Check to ensure teams and region are valid objects
        # teams is a list of teams whose seeds are 1-16
        TEAM_ERROR = ValueError("teams must be an ordered (by seed) list of 16 teams")
        
        n_teams = 16
        if len(teams) != n_teams: raise TEAM_ERROR
        for i in range(n_teams):
            if teams[i].seed != (i+1): raise TEAM_ERROR

        # Set teams
        self.teams = teams
        self.team01 = teams[0]
        self.team02 = teams[1]
        self.team03 = teams[2]
        self.team04 = teams[3]
        self.team05 = teams[4]
        self.team06 = teams[5]
        self.team07 = teams[6]
        self.team08 = teams[7]
        self.team09 = teams[8]
        self.team10 = teams[9]
        self.team11 = teams[10]
        self.team12 = teams[11]
        self.team13 = teams[12]
        self.team14 = teams[13]
        self.team15 = teams[14]
        self.team16 = teams[15]
        
        # Set round 1
        self.Game1 = Game(self.team01, self.team16, 1)
        self.Game2 = Game(self.team08, self.team09, 1)
        self.Game3 = Game(self.team05, self.team12, 1)
        self.Game4 = Game(self.team04, self.team13, 1)        
        self.Game5 = Game(self.team06, self.team11, 1)
        self.Game6 = Game(self.team03, self.team14, 1)
        self.Game7 = Game(self.team07, self.team10, 1)
        self.Game8 = Game(self.team02, self.team15, 1)     
        
        self.round1 = [self.Game1, self.Game2, self.Game3, self.Game4,
                       self.Game5, self.Game6, self.Game7, self.Game8]
        return self
   
    def run_first_round(self, sim_func):
        
        if not self.round1: raise Exception("Need to initialize first round before running")
            
        self.Game9 = Game(sim_func(self.Game1), sim_func(self.Game2), 2)
        self.Game10 = Game(sim_func(self.Game3), sim_func(self.Game4), 2)
        self.Game11 = Game(sim_func(self.Game5), sim_func(self.Game6), 2)
        self.Game12 = Game(sim_func(self.Game7), sim_func(self.Game8), 2)
        
        self.round2 = [self.Game9, self.Game10 ,self.Game11 ,self.Game12]
        
        return self
    
    def run_second_round(self, sim_func):
        # Verify first round has completed
        if not self.round2: raise Exception("Need to complete first round before second")
        
        self.Game13 = Game(sim_func(self.Game9), sim_func(self.Game10), 3)
        self.Game14 = Game(sim_func(self.Game11), sim_func(self.Game12), 3)
        
        self.round3 = [self.Game13, self.Game14]
        
        return self

    def run_sweet_sixteen(self, sim_func):
        # Verify first round has completed
        if not self.round3: raise Exception("Need to complete second round before third")
        
        self.Game15 = Game(sim_func(self.Game13), sim_func(self.Game14), 4)
        
        self.round4 = [self.Game15]
        
        return self

    def run_elite_eight(self, sim_func):
        # Verify first round has completed
        if not self.round4: raise Exception("Need to complete second round before third")       
        self.winner = sim_func(self.Game15)
        return self
        
    def run_bracket(self, sim_func):
        self.run_first_round(sim_func)
        self.run_second_round(sim_func)
        self.run_sweet_sixteen(sim_func)
        self.run_elite_eight(sim_func)
        return self

    def __repr__(self):
        region_header = f'{self.region} Region\n-----------\n'
        round1_header = 'Round 1:\n-------\n'
        round2_header = '\nRound 2:\n-------\n'
        round3_header = '\nSweet 16:\n--------\n'
        round4_header = '\nElite 8:\n-------\n'
        winner_header = '\nFinal 4:\n-------\n'
        round1_str = round1_header + ''.join([str(game) for game in self.round1])
        round2_str = round2_header + ''.join([str(game) for game in self.round2])
        round3_str = round3_header + ''.join([str(game) for game in self.round3])
        round4_str = round4_header + ''.join([str(game) for game in self.round4])
        winner_str = winner_header
        if self.winner is not None:
            winner_str += str(self.winner)
        bracket_str = f"{region_header}{round1_str}{round2_str}{round3_str}{round4_str}{winner_str}"
        return bracket_str


class FinalFour():
    """
    A bracket of four teams to simulate the final four of a NCAA tournamnet
    
    Attributes
    ----------
    Game1 : Game
        Final four game for regions 1 and 3
    Game2 : Game
        Final four game for regions 2 and 4
    Championship : Game
        Final game of tournament to determine the simulated winner
    winner : Team
        The team from this region that is simulated to make the final four    
    """
    def __init__(self, year):
        """
        Parameters
        ----------
        year : int
            Year of the NCAA tournament
        """
        self.year = str(year)
        
        # Get bracket dict
        bracket = brackets_dict.get(self.year)
        self.final_matches = bracket.get('Finals')
        
        self.Game1 = None
        self.Game2 = None
        self.Championship = None
        self.winner = None
        
    def __repr__(self):
        final_four_header = '\nFinal Four:\n------------\n'
        championship_header = '\nChampionship:\n------------\n'
        winner_header = '\nWinner:\n------------\n'
        
        return f"{winner_header}{self.winner}{championship_header}{self.Championship}{final_four_header}{self.Game1}{self.Game2}\n"
        
    def set_matches(self, teams):
        
        game1 = self.final_matches.get('game1')
        game2 = self.final_matches.get('game2')

        self.Game1 = Game(teams[game1['team1']], teams[game1['team2']], 5)
        self.Game2 = Game(teams[game2['team1']], teams[game2['team2']], 5)
        
    def run_final_four(self, sim_func):
        
        if self.Game1 is None or self.Game2 is None:
            raise Exception("Need to initialize teams before running games")
        
        self.Championship = Game(sim_func(self.Game1), sim_func(self.Game2), 6)
        
    def run_championship(self, sim_func):
        
        if self.Championship is None:
            raise Exception("Need to run final four round before championship")
            
        self.winner = sim_func(self.Championship)

class Bracket():
    """
    A NCAA tournament for a specific year
    
    Attributes
    ----------
    year : int
        Calendar year of the tournament (1985-2019)
    result : (dict)
        The actual tournament results for that year
    regions : (dict)
        The teams that year broken down by region
    East : (SubBracket16)
        SubBracket for East
    West : (SubBracket16)
        SubBracket for West
    Midwest : (SubBracket16)
        SubBracket for Midwest
    South : (SubBracket16)
        SubBracket for South
    Finals : (FinalFour)
        Final Four and Championship games
    round1, round2, ... , round6 : (list of Teams)
        Which teams are simulated to make it to each round
    winner : Team
        Simulated tournament winner
    n_games_correct int
        Number of games the simulation got correct
    total_score int
        Total points earned by the simulator function (32 points per round)
    """
    def __repr__(self): 
        header = f"Bracket for year {self.year}"
        return f"{header}{self.Finals}{self.East}{self.West}{self.Midwest}{self.South}"
    
    def __init__(self, year):
        """
        Parameters
        ----------
        year : int
            Year of the NCAA tournament
        """
        valid_years = [y for y in range(1985, 2019+1)]
        if year not in valid_years:
            raise ValueError("Year must be between 1985 and 2019")
        
        # Set year
        self.year = str(year)
        
        # Get bracket dict
        bracket = brackets_dict.get(self.year)
        self.result = bracket.get('Results')
        self.regions = bracket.get('Region')        
        
        # Get Team Lists
        east_teams = [];    add_east = east_teams.append
        west_teams = [];    add_west = west_teams.append
        midwest_teams = []; add_midwest = midwest_teams.append
        south_teams = [];   add_south = south_teams.append

        for team in self.regions['East']: add_east(Team(name=team['Team'], seed=team['Seed']))
        for team in self.regions['West']: add_west(Team(name=team['Team'], seed=team['Seed']))
        for team in self.regions['Midwest']: add_midwest(Team(name=team['Team'], seed=team['Seed']))
        for team in self.regions['South']: add_south(Team(name=team['Team'], seed=team['Seed']))

        # Create Region Brackets
        self.East = SubBracket16('East').initialize_first_round(east_teams)
        self.West = SubBracket16('West').initialize_first_round(west_teams)
        self.Midwest = SubBracket16('Midwest').initialize_first_round(midwest_teams)
        self.South = SubBracket16('South').initialize_first_round(south_teams)
        self.Finals = FinalFour(year)
        
        # Initalize teams in each round
        self.round1 = east_teams + west_teams + midwest_teams + south_teams
        self.round2 = [] # 8 teams left in each region
        self.round3 = [] # sweet 16, 4 teams left in each region
        self.round4 = [] # elite 8, 2 teams left in each region
        self.round5 = [] # final four 1 team from each region
        self.round6 = [] # championship game
        self.winner = None # Initalize as None until winner is set
        
        # Initialize Scores
        self.n_games_correct = 0
        self.total_score = 0
        
    def run_first_round(self, sim_func):
        """
        Simulate the first round of the tournament. Fills out the games 
        and teams in the second round

        Parameters
        ----------
        sim_func : function
            A function that take in `Game` and returns a `Team` of that Game
        """
        if not self.round1: raise Exception("Need to initialize first round before running")
        
        # Run first round for all brackets
        self.East.run_first_round(sim_func)
        self.West.run_first_round(sim_func)
        self.Midwest.run_first_round(sim_func)
        self.South.run_first_round(sim_func)
        
        self.round2 = \
            [team for game in self.East.round2 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.West.round2 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.Midwest.round2 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.South.round2 for team in [game.top_team, game.bottom_team]]
            
    def run_second_round(self, sim_func):
        """
        Simulate the second round of the tournament. Fills out the games 
        and teams in the third round

        Parameters
        ----------
        sim_func : function
            A function that take in `Game` and returns a `Team` of that Game
        """
        # Verify first round has completed
        if not self.round2: raise Exception("Need to complete first round before second")
        
        # Run second round for all brackets
        self.East.run_second_round(sim_func)
        self.West.run_second_round(sim_func)
        self.Midwest.run_second_round(sim_func)
        self.South.run_second_round(sim_func)
        
        self.round3 = \
            [team for game in self.East.round3 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.West.round3 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.Midwest.round3 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.South.round3 for team in [game.top_team, game.bottom_team]]
            
    def run_sweet_sixteen(self, sim_func):
        """
        Simulate the third round of the tournament. Fills out the games 
        and teams in the fourth round

        Parameters
        ----------
        sim_func : function
            A function that take in `Game` and returns a `Team` of that Game
        """
        # Verify first round has completed
        if not self.round3: raise Exception("Need to complete second round before third")
        
        # Run sweet sixteen round for all brackets
        self.East.run_sweet_sixteen(sim_func)
        self.West.run_sweet_sixteen(sim_func)
        self.Midwest.run_sweet_sixteen(sim_func)
        self.South.run_sweet_sixteen(sim_func)
        
        self.round4 = \
            [team for game in self.East.round4 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.West.round4 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.Midwest.round4 for team in [game.top_team, game.bottom_team]] + \
            [team for game in self.South.round4 for team in [game.top_team, game.bottom_team]]
        
    def run_elite_eight(self, sim_func):
        """
        Simulate the fourth round of the tournament. Fills out the games 
        and teams in the fifth round

        Parameters
        ----------
        sim_func : function
            A function that take in `Game` and returns a `Team` of that Game
        """
        # Verify first round has completed
        if not self.round4: raise Exception("Need to complete second round before third")       
        
        # Run sweet sixteen round for all brackets
        self.East.run_elite_eight(sim_func)
        self.West.run_elite_eight(sim_func)
        self.Midwest.run_elite_eight(sim_func)
        self.South.run_elite_eight(sim_func)
        
        # Place each team in final four
        region_names = ['East', 'West', 'Midwest', 'South'] # Order of these two lists must match
        self.round5 = [self.East.winner, self.West.winner, self.Midwest.winner, self.South.winner]
        
        # Create final four games
        self.Finals.set_matches(dict(zip(region_names, self.round5)))
        
    def run_final_four(self, sim_func):
        """
        Simulate the fifth round of the tournament. Fills out the games 
        and teams in the sixth round

        Parameters
        ----------
        sim_func : function
            A function that take in `Game` and returns a `Team` of that Game
        """
        # Verify Previoud round has completed
        if not self.round5: raise Exception("Need to complete third round before fourth")
        
        # Run Games
        self.Finals.run_final_four(sim_func)
        self.round6 = [self.Finals.Championship.top_team, self.Finals.Championship.bottom_team]
        
    def run_championship(self, sim_func):
        """
        Simulate the sixth round of the tournament. 
        Set the winner of entire tournament

        Parameters
        ----------
        sim_func : function
            A function that take in `Game` and returns a `Team` of that Game
        """
        if not self.round6: raise Exception("Need to complete fourth round before fifth")
        
        # Run Game
        self.Finals.run_championship(sim_func)
        
        # Set Winner
        self.winner = self.Finals.winner
        
    def sim(self, sim_func):
        """
        Simulate the entire bracket with `sim_func`, 
        from first round to deciding the winner

        Parameters
        ----------
        sim_func : function
            A function that take in `Game` and returns a `Team` of that Game
        """
        self.run_first_round(sim_func)
        self.run_second_round(sim_func)
        self.run_sweet_sixteen(sim_func)
        self.run_elite_eight(sim_func)
        self.run_final_four(sim_func)
        self.run_championship(sim_func)

    def score(self, sim_func=None, verbose=True):
        """
        Calculates the number of games correct from the simulation and 
        that total score (32 points per round). Will run a new simulation
        as well if passed `sim_func` argument. 

        Parameters
        ----------
        sim_func : function, optional
            A function that take in `Game` and returns a `Team` of that Game.
            Can be null if the bracket has already been simulated
        verbose : bool, optional
            Whether or not to print the score. If False, will not print score,
            only sets the `n_games_correct` and `total_score` parameters. 
            The default is True.
        """
        if sim_func is None:
            if self.winner is None:
                raise Exception("Need to run simulation before scoring")
        else:
            self.sim(sim_func)
        
        n_correct_round1 = len(set([team['Team'] for team in self.result['second']]).intersection([team.name for team in self.round2]))
        n_correct_round2 = len(set([team['Team'] for team in self.result['sweet16']]).intersection([team.name for team in self.round3]))
        n_correct_round3 = len(set([team['Team'] for team in self.result['elite8']]).intersection([team.name for team in self.round4]))
        n_correct_round4 = len(set([team['Team'] for team in self.result['final4']]).intersection([team.name for team in self.round5]))
        n_correct_round5 = len(set([team['Team'] for team in self.result['championship']]).intersection([team.name for team in self.round6]))
        correct_winner = int(self.winner.name == self.result['winner'])
        
        self.n_games_correct = n_correct_round1 + n_correct_round2 + n_correct_round3 + \
                               n_correct_round4 + n_correct_round5 + correct_winner
        
        self.total_score = 1  * n_correct_round1 + \
                           2  * n_correct_round2 + \
                           4  * n_correct_round3 + \
                           8  * n_correct_round4 + \
                           16 * n_correct_round5 + \
                           32 * correct_winner
        if verbose:
            print(f"Number of games correct: {self.n_games_correct}/63")
            print(f"Total Score: {self.total_score}/192")









