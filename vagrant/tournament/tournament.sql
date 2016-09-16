
DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS players, matches CASCADE;

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players(
	player_id serial PRIMARY KEY,
	player_name text
);

CREATE TABLE matches(
	match_id serial PRIMARY KEY,
	winner_id integer,
	loser_id integer
);


CREATE VIEW standings AS 
	SELECT players.player_id, players.player_name,
	(SELECT count(matches.winner_id)
	FROM matches
	WHERE  players.player_id = matches.winner_id)
	AS player_wins,
	(SELECT count(matches.match_id)
	FROM matches
	WHERE players.player_id = matches.winner_id 
	OR players.player_id = matches.loser_id)
	AS player_total
	FROM players
	ORDER BY player_wins DESC, player_total DESC
;	