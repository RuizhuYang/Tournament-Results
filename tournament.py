#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    s = " delete from Matches;"
    c.execute(s)
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    s = " delete from Players;"
    c.execute(s)
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    s = " select count(*) as num from Players;"
    c.execute(s)
    conn.commit()
    row = c.fetchone()
    number = row[0]
    conn.close()
    return number


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("insert into Players(name) values(%s)",(name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    list = []
    conn = connect()
    c = conn.cursor()
    """get the wins number of each player"""
    winCount = "create view winCount as(select winner as winner , count(*) as num from Matches group by winner );"
    """get the lose number of each player""" 
    loseCount = "create view loseCount as(select player2 as loser, count(*) as num from Matches group by player2);"
    c.execute(winCount)
    c.execute(loseCount)
    conn.commit()
    """join the player name and id with win number"""
    joinWin = "create view joinWin as(select Players.id as id, Players.name as name, winCount.num as wins from Players left join winCount on Players.id = winCount.winner order by wins desc);"
    """join the player id and lose number"""
    joinLose = "create view joinLose as(select Players.id as id, loseCount.num as num from Players left join loseCount on Players.id = loseCount.loser);"
    c.execute(joinWin)
    c.execute(joinLose)
    conn.commit()
    """put id, name, win, lose of each player together """
    alljoin = "select joinWin.id as id, joinWin.name as name, joinWin.wins as wins, joinLose.num as lose from joinWin left join joinLose on joinWin.id = joinLose.id order by wins;"
    c.execute(alljoin)
    conn.commit()
    rows = c.fetchall()
    """use the win, lose to get the matches of each player, and change None to zero"""
    count = 0
    inlist = []
    for row in rows:
        for item in row:
            if count != 3:
                if item is None:
                    inlist.append(0)
                else:
                    inlist.append(item)
                count = count + 1
            else:
                if item is None:
                    inlist.append(inlist[2])
                else:
                    inlist.append(item + inlist[2])
                list.append(inlist)
                count = 0
                inlist = []
    c.execute("drop view joinLose;")
    c.execute("drop view joinWin;")
    c.execute("drop view loseCount;")
    c.execute("drop view winCount;")
    conn.commit()
    conn.close()
    return list

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute(" insert into Matches(player1, player2, winner) values(%s,%s,%s)",(winner,loser, winner))
    conn.commit()
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    list = []
    inlist = []
    standings = playerStandings()
    for i in range(len(standings)/2):
        inlist.append(standings[i*2][0])
        inlist.append(standings[i*2][1])
        inlist.append(standings[i*2+1][0])
        inlist.append(standings[i*2+1][1])
        list.append(inlist)
        inlist = []
    return list
        
    


