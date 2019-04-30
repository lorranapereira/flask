CREATE TABLE "Departamento" (
    "nome" varchar(100) NOT NULL,
    "id" serial unique,
    "id_gerente" int,
    CONSTRAINT "DepartamentoPK" PRIMARY KEY ("id")
)
INSERT INTO "Departamento" (nome) values ('RH')

CREATE TABLE "Funcionario" (
    "nome" varchar (100) NOT NULL,
    "id" serial unique,
    "idDepto" int NOT NULL,
    CONSTRAINT "FuncionarioPK" PRIMARY KEY ("id"),
    CONSTRAINT "FuncionarioFK" FOREIGN KEY ("idDepto")
        REFERENCES "Departamento" ("id")
            ON DELETE SET NULL
            ON UPDATE CASCADE  
)
INSERT INTO "Funcionario" (nome,"idDepto") values ('lorrana','1')

ALTER TABLE "Departamento" ADD CONSTRAINT "DepartamentoFK" FOREIGN KEY ("id_gerente") 
    REFERENCES  "Funcionario" ("id");

CREATE TABLE "Projeto" (
    "nome" varchar (100) NOT NULL,
    "id" serial unique,
    "dataPrevista" date,
    CONSTRAINT "ProjetoPK" PRIMARY KEY ("id")
)
INSERT INTO "Projeto" (nome,"dataPrevista") values ('lorrana','10/10/2000')

CREATE TABLE "FuncProj" (
    "idProjeto" int unique,
    "idFuncionario" int unique,
    CONSTRAINT "ProjPK" PRIMARY KEY ("idProjeto","idFuncionario"),
    CONSTRAINT "FuncFK" FOREIGN KEY ("idFuncionario")
	REFERENCES "Funcionario" ("id")
	    ON DELETE SET NULL
	    ON UPDATE CASCADE,  
    CONSTRAINT "ProjFK" FOREIGN KEY ("idProjeto")
	REFERENCES "Projeto" ("id")
	    ON DELETE SET NULL
	    ON UPDATE CASCADE  
)
