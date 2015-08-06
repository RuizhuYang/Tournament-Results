To seccessfully run the application:
1) Launch vagrant.
2) Access to the tournament database, run command: psql tournament
3) Build the database using command: \i tournamnet.sql 
4) Now, start a tournament.First, register players each by each using registerPlayer(name) in module tournament.py.
5) The players have been registered now. They can be checked in table players. After each round, the result of winner and loser should be recorded into table matches. Use reportMatch(winner, loser) in moduel tournament.py to reprot the result. 
6) To continue to next round, a list of pairs of players for the next round of a match is needed. Use swissPairings() in module tournament.py to get the list and continue to the next round.
7) When tournament is done, use playerStandings() in modue tournament.py to check the santdings of players.
8) After delet all the records in talbe players and table matches by using deleteMatches() and deletePlayers(), a new tournament can be started.  