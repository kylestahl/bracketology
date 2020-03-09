import random
def upset_prob(p):
    """
    Given a probability between 0-1 will return a function that can
    be as an algorithm to fill out an NCAA bracket with `p` as 
    the probability of an upset
    
    Parameters
    ----------
    p  :  float
        The probability of an upset
    
    Returns
    -------
    scoring_func  :  function
        function to pick an upset of a Game with probability `p`
    """
    assert type(p) == float, "p must be a float"
    assert p <= 1.0, "p must be <= 1.0"
    assert p >= 0.0, "p must be >= 0.0"
    
    def sim_func(the_game):
        team1 = the_game.top_team
        team2 = the_game.bottom_team

        team1_seed = team1.seed
        team2_seed = team2.seed
        
        team1_is_higher_seed = (team1_seed <= team2_seed)
        is_upset = (random.random() < p)
        
        if team1_is_higher_seed:
            if is_upset:
                winner = team2
            else:
                winner = team1
        else:
            if is_upset:
                winner = team1
            else:
                winner = team2
        return winner

    return sim_func
    



