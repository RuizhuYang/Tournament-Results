-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

--connect to tournament database
\c tournament;

CREATE TABLE players( id serial PRIMARY KEY, name text);

CREATE TABLE mateches(
 	id serial PRIMARY KEY,
 	player1 integer REFERENCES players(id), 
 	player2 integer REFERENCES players(id), 
 	winner integer REFERENCES players(id)
 	);

--finding the number of matches each player has played

--the number of wins for each player

--the player standings