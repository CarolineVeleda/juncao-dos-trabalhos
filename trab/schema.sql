select * from usuario;

create table Usuario(
    codusuario serial,
    nome VARCHAR(200),
    login VARCHAR(100),
    altura float,
    idade int,
    email VARCHAR(300),
    senha VARCHAR(100),    
	CONSTRAINT "usuarioPK" PRIMARY KEY (codusuario)
);