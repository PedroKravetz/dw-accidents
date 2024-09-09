CREATE TABLE IF NOT EXISTS secao
(
   id serial not null,
   br INTEGER NOT NULL,
   km text NOT NULL,
   latitude text NOT NULL,
   longitude text NOT NULL,
   cidade VARCHAR(255) NOT NULL,
   estado char(2) not null,
   PRIMARY KEY (id)
);

create table if not exists tipo_veiculo
(
   id serial not null,
   marca text not null,
   nome text not null,
   primary key (id)
);

CREATE TABLE IF NOT EXISTS veiculo
(
   id integer NOT NULL,
   tipo VARCHAR(255),
   tipo_veiculo integer,
   ano_fabricacao INTEGER  NOT NULL,
   PRIMARY KEY (id),
   foreign key (tipo_veiculo) references tipo_veiculo(id)
);

CREATE TABLE IF NOT EXISTS acidentes
(
   id integer NOT NULL,
   data_acidente date NOT NULL,
   dia_semana text not null,
   horario text NOT NULL,
   id_secao INTEGER not null,
   causa VARCHAR(255) NOT NULL,
   tipo VARCHAR(255),
   classificacao VARCHAR(255),
   fase_dia VARCHAR(255) NOT NULL,
   sentido_via VARCHAR(255) NOT NULL,
   tempo VARCHAR(255) NOT NULL,
   tipo_via VARCHAR(255) NOT NULL,
   solo CHAR(3) NOT NULL,
   delegacia VARCHAR(255),
   uop VARCHAR(255),
   regional VARCHAR(255),
   PRIMARY KEY (id),
   FOREIGN KEY (id_secao) REFERENCES secao(id)
);



CREATE TABLE IF NOT EXISTS pessoa
(
   id SERIAL NOT NULL,
   tipo VARCHAR(255),
   estado VARCHAR(255),
   idade INTEGER NOT NULL,
   sexo CHAR(13),
   ilesos INTEGER,
   feridos_leves INTEGER,
   feridos_graves INTEGER,
   mortos INTEGER,
   PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS tracado_via
(
   id SERIAL NOT NULL,
   nome VARCHAR(255) NOT NULL,
   PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS acidente_tracado
(
	id_acidente integer NOT NULL,
	id_tracado integer NOT NULL,
	PRIMARY KEY(id_acidente, id_tracado),
	FOREIGN KEY (id_acidente) REFERENCES acidentes(id),
	FOREIGN KEY (id_tracado) REFERENCES tracado_via
);

create table if not exists acidente_veiculo_pessoa
(
    id_acidente integer,
	id_veiculo integer,
	id_pessoa integer,
	primary key(id_acidente, id_veiculo, id_pessoa),
	FOREIGN KEY (id_acidente) REFERENCES acidentes(id),
	FOREIGN KEY (id_veiculo) REFERENCES veiculo(id),
	FOREIGN KEY (id_pessoa) REFERENCES pessoa(id)
);

INSERT INTO tracado_via (nome)
SELECT distinct TRIM(value)
FROM teste1, UNNEST(STRING_TO_ARRAY(tracado_via, ';')) AS value;

insert into secao(br, km, longitude, latitude, cidade, estado)
select distinct teste1.br, teste1.km, teste1.longitude, teste1.latitude, 
teste1.municipio, teste1.uf
from teste1;

insert into tipo_veiculo(marca, nome)
select distinct split_part(marca, '/', 1), split_part(marca, '/', 2) from teste1;

insert into veiculo(id, tipo_veiculo, tipo, ano_fabricacao)
select distinct teste1.id_veiculo, tipo_veiculo.id, tipo_veiculo, ano_fabricacao_veiculo
from teste1, 
tipo_veiculo where split_part(teste1.marca, '/', 1) = tipo_veiculo.marca 
and split_part(teste1.marca, '/', 2) = tipo_veiculo.nome;

insert into pessoa(id, tipo, estado, idade, sexo, ilesos, 
feridos_leves, feridos_graves, mortos)
select distinct pesid, tipo_envolvido, estado_fisico, idade, sexo, ilesos, 
feridos_leves, feridos_graves, mortos
from teste1;

insert into acidentes(id, data_acidente, dia_semana,horario,id_secao,
causa,tipo,classificacao,fase_dia,sentido_via,tempo,tipo_via,solo, 
delegacia, uop, regional)
select distinct teste1.id, to_date(data_inversa, 'YYYY-MM-DD'), dia_semana, horario, 
secao.id, causa_acidente, tipo_acidente, classificacao_acidente, fase_dia, sentido_via, 
condicao_metereologica, tipo_pista, uso_solo, delegacia, uop, regional
from teste1, secao
where teste1.br=secao.br and teste1.km=secao.km and teste1.br=secao.br 
and teste1.longitude=secao.longitude and teste1.latitude=secao.latitude 
and teste1.uf=secao.estado and teste1.municipio=secao.cidade;

insert into acidente_tracado(id_acidente, id_tracado)
select distinct teste1.id, tracado_via.id
from teste1, tracado_via
where teste1.tracado_via like '%' || tracado_via.nome || '%';

insert into acidente_veiculo_pessoa(id_acidente, id_veiculo, id_pessoa)
select id, id_veiculo, pesid
from teste1;

--drop table if exists teste1;

create table if not exists tempo(
	id serial primary key,
	mes varchar(20) null,
	trimestre varchar(20) null,
	ano integer null
);

create table if not exists localizacao(
	id serial primary key,
	cidade VARCHAR(255) NOT NULL,
  	estado char(2) not null
);

create table if not exists fato_acidentes(
	quantidade integer,
	cod_localizacao integer,
	cod_tempo integer,
	primary key (cod_localizacao, cod_tempo),
	foreign key (cod_localizacao) references localizacao(id),
	foreign key (cod_tempo) references tempo(id)
);

insert into tempo(mes, ano)
values('Janeiro', 2017);
insert into tempo(mes, ano)
values('Fevereiro', 2017);
insert into tempo(mes, ano)
values('Março', 2017);
insert into tempo(mes, ano)
values('Abril', 2017);
insert into tempo(mes, ano)
values('Maio', 2017);
insert into tempo(mes, ano)
values('Junho', 2017);
insert into tempo(mes, ano)
values('Julho', 2017);
insert into tempo(mes, ano)
values('Agosto', 2017);
insert into tempo(mes, ano)
values('Setembro', 2017);
insert into tempo(mes, ano)
values('Outubro', 2017);
insert into tempo(mes, ano)
values('Novembro', 2017);
insert into tempo(mes, ano)
values('Dezembro', 2017);

insert into tempo(mes, ano)
values('Janeiro', 2018);
insert into tempo(mes, ano)
values('Fevereiro', 2018);
insert into tempo(mes, ano)
values('Março', 2018);
insert into tempo(mes, ano)
values('Abril', 2018);
insert into tempo(mes, ano)
values('Maio', 2018);
insert into tempo(mes, ano)
values('Junho', 2018);
insert into tempo(mes, ano)
values('Julho', 2018);
insert into tempo(mes, ano)
values('Agosto', 2018);
insert into tempo(mes, ano)
values('Setembro', 2018);
insert into tempo(mes, ano)
values('Outubro', 2018);
insert into tempo(mes, ano)
values('Novembro', 2018);
insert into tempo(mes, ano)
values('Dezembro', 2018);

insert into tempo(mes, ano)
values('Janeiro', 2019);
insert into tempo(mes, ano)
values('Fevereiro', 2019);
insert into tempo(mes, ano)
values('Março', 2019);
insert into tempo(mes, ano)
values('Abril', 2019);
insert into tempo(mes, ano)
values('Maio', 2019);
insert into tempo(mes, ano)
values('Junho', 2019);
insert into tempo(mes, ano)
values('Julho', 2019);
insert into tempo(mes, ano)
values('Agosto', 2019);
insert into tempo(mes, ano)
values('Setembro', 2019);
insert into tempo(mes, ano)
values('Outubro', 2019);
insert into tempo(mes, ano)
values('Novembro', 2019);
insert into tempo(mes, ano)
values('Dezembro', 2019);

insert into tempo(mes, ano)
values('Janeiro', 2020);
insert into tempo(mes, ano)
values('Fevereiro', 2020);
insert into tempo(mes, ano)
values('Março', 2020);
insert into tempo(mes, ano)
values('Abril', 2020);
insert into tempo(mes, ano)
values('Maio', 2020);
insert into tempo(mes, ano)
values('Junho', 2020);
insert into tempo(mes, ano)
values('Julho', 2020);
insert into tempo(mes, ano)
values('Agosto', 2020);
insert into tempo(mes, ano)
values('Setembro', 2020);
insert into tempo(mes, ano)
values('Outubro', 2020);
insert into tempo(mes, ano)
values('Novembro', 2020);
insert into tempo(mes, ano)
values('Dezembro', 2020);

insert into tempo(mes, ano)
values('Janeiro', 2021);
insert into tempo(mes, ano)
values('Fevereiro', 2021);
insert into tempo(mes, ano)
values('Março', 2021);
insert into tempo(mes, ano)
values('Abril', 2021);
insert into tempo(mes, ano)
values('Maio', 2021);
insert into tempo(mes, ano)
values('Junho', 2021);
insert into tempo(mes, ano)
values('Julho', 2021);
insert into tempo(mes, ano)
values('Agosto', 2021);
insert into tempo(mes, ano)
values('Setembro', 2021);
insert into tempo(mes, ano)
values('Outubro', 2021);
insert into tempo(mes, ano)
values('Novembro', 2021);
insert into tempo(mes, ano)
values('Dezembro', 2021);

insert into tempo(mes, ano)
values('Janeiro', 2022);
insert into tempo(mes, ano)
values('Fevereiro', 2022);
insert into tempo(mes, ano)
values('Março', 2022);
insert into tempo(mes, ano)
values('Abril', 2022);
insert into tempo(mes, ano)
values('Maio', 2022);
insert into tempo(mes, ano)
values('Junho', 2022);
insert into tempo(mes, ano)
values('Julho', 2022);
insert into tempo(mes, ano)
values('Agosto', 2022);
insert into tempo(mes, ano)
values('Setembro', 2022);
insert into tempo(mes, ano)
values('Outubro', 2022);
insert into tempo(mes, ano)
values('Novembro', 2022);
insert into tempo(mes, ano)
values('Dezembro', 2022);

insert into tempo(mes, ano)
values('Janeiro', 2023);
insert into tempo(mes, ano)
values('Fevereiro', 2023);
insert into tempo(mes, ano)
values('Março', 2023);
insert into tempo(mes, ano)
values('Abril', 2023);
insert into tempo(mes, ano)
values('Maio', 2023);
insert into tempo(mes, ano)
values('Junho', 2023);
insert into tempo(mes, ano)
values('Julho', 2023);
insert into tempo(mes, ano)
values('Agosto', 2023);
insert into tempo(mes, ano)
values('Setembro', 2023);
insert into tempo(mes, ano)
values('Outubro', 2023);
insert into tempo(mes, ano)
values('Novembro', 2023);
insert into tempo(mes, ano)
values('Dezembro', 2023);

insert into tempo(ano)
values (2017);
insert into tempo(ano)
values (2018);
insert into tempo(ano)
values (2019);
insert into tempo(ano)
values (2020);
insert into tempo(ano)
values (2021);
insert into tempo(ano)
values (2022);
insert into tempo(ano)
values (2023);

insert into localizacao(cidade, estado)
select distinct cidade, estado from secao;

create table if not exists tempo1(
	id serial primary key,
	mes varchar(20) null,
	trimestre varchar(20) null,
	ano integer null
);

create table if not exists localizacao1(
	id serial primary key,
	cidade VARCHAR(255) NOT NULL,
  	estado char(2) not null
);

create table if not exists fato_mortos(
	quantidade integer,
	cod_localizacao integer,
	cod_tempo integer,
	primary key (cod_localizacao, cod_tempo),
	foreign key (cod_localizacao) references localizacao1(id),
	foreign key (cod_tempo) references tempo1(id)
);

insert into tempo1(mes, ano)
values('Janeiro', 2017);
insert into tempo1(mes, ano)
values('Fevereiro', 2017);
insert into tempo1(mes, ano)
values('Março', 2017);
insert into tempo1(mes, ano)
values('Abril', 2017);
insert into tempo1(mes, ano)
values('Maio', 2017);
insert into tempo1(mes, ano)
values('Junho', 2017);
insert into tempo1(mes, ano)
values('Julho', 2017);
insert into tempo1(mes, ano)
values('Agosto', 2017);
insert into tempo1(mes, ano)
values('Setembro', 2017);
insert into tempo1(mes, ano)
values('Outubro', 2017);
insert into tempo1(mes, ano)
values('Novembro', 2017);
insert into tempo1(mes, ano)
values('Dezembro', 2017);

insert into tempo1(mes, ano)
values('Janeiro', 2018);
insert into tempo1(mes, ano)
values('Fevereiro', 2018);
insert into tempo1(mes, ano)
values('Março', 2018);
insert into tempo1(mes, ano)
values('Abril', 2018);
insert into tempo1(mes, ano)
values('Maio', 2018);
insert into tempo1(mes, ano)
values('Junho', 2018);
insert into tempo1(mes, ano)
values('Julho', 2018);
insert into tempo1(mes, ano)
values('Agosto', 2018);
insert into tempo1(mes, ano)
values('Setembro', 2018);
insert into tempo1(mes, ano)
values('Outubro', 2018);
insert into tempo1(mes, ano)
values('Novembro', 2018);
insert into tempo1(mes, ano)
values('Dezembro', 2018);

insert into tempo1(mes, ano)
values('Janeiro', 2019);
insert into tempo1(mes, ano)
values('Fevereiro', 2019);
insert into tempo1(mes, ano)
values('Março', 2019);
insert into tempo1(mes, ano)
values('Abril', 2019);
insert into tempo1(mes, ano)
values('Maio', 2019);
insert into tempo1(mes, ano)
values('Junho', 2019);
insert into tempo1(mes, ano)
values('Julho', 2019);
insert into tempo1(mes, ano)
values('Agosto', 2019);
insert into tempo1(mes, ano)
values('Setembro', 2019);
insert into tempo1(mes, ano)
values('Outubro', 2019);
insert into tempo1(mes, ano)
values('Novembro', 2019);
insert into tempo1(mes, ano)
values('Dezembro', 2019);

insert into tempo1(mes, ano)
values('Janeiro', 2020);
insert into tempo1(mes, ano)
values('Fevereiro', 2020);
insert into tempo1(mes, ano)
values('Março', 2020);
insert into tempo1(mes, ano)
values('Abril', 2020);
insert into tempo1(mes, ano)
values('Maio', 2020);
insert into tempo1(mes, ano)
values('Junho', 2020);
insert into tempo1(mes, ano)
values('Julho', 2020);
insert into tempo1(mes, ano)
values('Agosto', 2020);
insert into tempo1(mes, ano)
values('Setembro', 2020);
insert into tempo1(mes, ano)
values('Outubro', 2020);
insert into tempo1(mes, ano)
values('Novembro', 2020);
insert into tempo1(mes, ano)
values('Dezembro', 2020);

insert into tempo1(mes, ano)
values('Janeiro', 2021);
insert into tempo1(mes, ano)
values('Fevereiro', 2021);
insert into tempo1(mes, ano)
values('Março', 2021);
insert into tempo1(mes, ano)
values('Abril', 2021);
insert into tempo1(mes, ano)
values('Maio', 2021);
insert into tempo1(mes, ano)
values('Junho', 2021);
insert into tempo1(mes, ano)
values('Julho', 2021);
insert into tempo1(mes, ano)
values('Agosto', 2021);
insert into tempo1(mes, ano)
values('Setembro', 2021);
insert into tempo1(mes, ano)
values('Outubro', 2021);
insert into tempo1(mes, ano)
values('Novembro', 2021);
insert into tempo1(mes, ano)
values('Dezembro', 2021);

insert into tempo1(mes, ano)
values('Janeiro', 2022);
insert into tempo1(mes, ano)
values('Fevereiro', 2022);
insert into tempo1(mes, ano)
values('Março', 2022);
insert into tempo1(mes, ano)
values('Abril', 2022);
insert into tempo1(mes, ano)
values('Maio', 2022);
insert into tempo1(mes, ano)
values('Junho', 2022);
insert into tempo1(mes, ano)
values('Julho', 2022);
insert into tempo1(mes, ano)
values('Agosto', 2022);
insert into tempo1(mes, ano)
values('Setembro', 2022);
insert into tempo1(mes, ano)
values('Outubro', 2022);
insert into tempo1(mes, ano)
values('Novembro', 2022);
insert into tempo1(mes, ano)
values('Dezembro', 2022);

insert into tempo1(mes, ano)
values('Janeiro', 2023);
insert into tempo1(mes, ano)
values('Fevereiro', 2023);
insert into tempo1(mes, ano)
values('Março', 2023);
insert into tempo1(mes, ano)
values('Abril', 2023);
insert into tempo1(mes, ano)
values('Maio', 2023);
insert into tempo1(mes, ano)
values('Junho', 2023);
insert into tempo1(mes, ano)
values('Julho', 2023);
insert into tempo1(mes, ano)
values('Agosto', 2023);
insert into tempo1(mes, ano)
values('Setembro', 2023);
insert into tempo1(mes, ano)
values('Outubro', 2023);
insert into tempo1(mes, ano)
values('Novembro', 2023);
insert into tempo1(mes, ano)
values('Dezembro', 2023);

insert into tempo1(ano)
values (2017);
insert into tempo1(ano)
values (2018);
insert into tempo1(ano)
values (2019);
insert into tempo1(ano)
values (2020);
insert into tempo1(ano)
values (2021);
insert into tempo1(ano)
values (2022);
insert into tempo1(ano)
values (2023);

insert into localizacao1(cidade, estado)
select distinct cidade, estado from secao;