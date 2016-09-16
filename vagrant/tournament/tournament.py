#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print("Cannot connect to database")
    


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    query = "DELETE FROM matches;"
    c.execute(query)
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    query = "DELETE FROM players;"
    c.execute(query)
    conn.commit()
    conn.close()



def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    query = "SELECT count(*) FROM players;"
    c.execute(query)
    total = c.fetchone()[0]
    conn.close()
    return total 
    

def registerPlayer(name):
    """Adds a player to the tournament database."""  
    conn = connect()
    c = conn.cursor()
    query = "INSERT INTO players(player_name) VALUES (%s)"
    c.execute(query, (name, ))
    conn.commit()
    conn.close()
    
    

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins."""
    conn = connect()
    c = conn.cursor()
    query = "SELECT * FROM standings;"
    c.execute(query)
    standings = c.fetchall()
    conn.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players."""

    conn = connect()
    c = conn.cursor()
    query = "INSERT INTO matches(winner_id, loser_id) VALUES (%s, %s)" 
    c.execute(query, (winner, loser,))
    conn.commit()
    conn.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
    """
    standings = playerStandings()
    pairings = []
    
    for i in range(0, len(standings), 2):
        pairings.append((standings[i][0],standings[i][1],standings[i+1][0],standings[i+1][1]))
        
    for pairing in pairings:    
        print pairings    
    return pairings   

   

