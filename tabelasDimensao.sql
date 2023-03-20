CREATE TABLE dim_jogo(
	id_jogo SERIAL PRIMARY KEY,
	nome varchar(255)
);
CREATE TABLE dim_classificacao(
	id_classificacao SERIAL PRIMARY KEY,
	classificacao varchar(20)
);