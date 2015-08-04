To seccessfully run the application:
1) Launch vagrant.
2) In order to run the following stpes successfully, two tables name players and matches should be created in PostgreSQL darabase tournament.sql.
   use SQL clause to create the tow tables:
   CREATE TABLE players( id serial PRIMARY KEY, name txt);
   CREATE TABLE mateches(palyer1 integer REFERENCES players(id), player2 integer REFERENCES players(id), winner integer REFERENCES players(id));
2) Now, start a tournament.First, register players each by each using registerPlayer(name) in module tournament.py.
3) The players have been registered now. They can be checked in table players. After each round, the result of winner and loser should be recorded into table matches. Use reportMatch(winner, loser) in moduel tournament.py to reprot the result. 
4) To continue to next round, a list of pairs of players for the next round of a match is needed. Use swissPairings() in module tournament.py to get the list and continue to the next round.
5) When tournament is done, use playerStandings() in modue tournament.py to check the santdings of players.
6) After delet all the records in talbe players and table matches by using deleteMatches() and deletePlayers(), a new tournament can be started.  