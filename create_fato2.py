import psycopg2

db_params = {
    'host': 'localhost',
    'database': 'teste',
    'user': 'postgres',
    'password': 'postgres'
}

conn = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password']
)

cursor = conn.cursor()

cursor.execute("SELECT count(*) FROM localizacao1")

result = cursor.fetchall()

result=result[0][0]

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2017' and '31/01/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' + str(x) +''')), ''' + str(x) + ''', 1);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/02/2017' and '28/02/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 2);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/03/2017' and '31/03/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 3);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/04/2017' and '30/04/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' + str(x) +''')), ''' + str(x) + ''', 4);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/05/2017' and '31/05/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 5);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/06/2017' and '30/06/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 6);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/07/2017' and '31/07/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 7);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/08/2017' and '31/08/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 8);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/09/2017' and '30/09/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 9);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/10/2017' and '31/10/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 10);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/11/2017' and '30/11/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 11);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/12/2017' and '31/12/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 12);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2018' and '31/01/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 13);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/02/2018' and '28/02/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 14);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/03/2018' and '31/03/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 15);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/04/2018' and '30/04/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 16);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/05/2018' and '31/05/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 17);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/06/2018' and '30/06/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 18);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/07/2018' and '31/07/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 19);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/08/2018' and '31/08/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 20);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/09/2018' and '30/09/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 21);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/10/2018' and '31/10/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 22);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/11/2018' and '30/11/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 23);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/12/2018' and '31/12/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 24);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2019' and '31/01/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 25);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/02/2019' and '28/02/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 26);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/03/2019' and '31/03/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 27);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/04/2019' and '30/04/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 28);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/05/2019' and '31/05/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 29);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/06/2019' and '30/06/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 30);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/07/2019' and '31/07/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 31);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/08/2019' and '31/08/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 32);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/09/2019' and '30/09/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 33);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/10/2019' and '31/10/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 34);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/11/2019' and '30/11/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 35);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/12/2019' and '31/12/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 36);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2020' and '31/01/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 37);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/02/2020' and '29/02/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 38);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/03/2020' and '31/03/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 39);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/04/2020' and '30/04/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 40);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/05/2020' and '31/05/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 41);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/06/2020' and '30/06/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 42);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/07/2020' and '31/07/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 43);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/08/2020' and '31/08/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 44);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/09/2020' and '30/09/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 45);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/10/2020' and '31/10/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 46);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/11/2020' and '30/11/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 47);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/12/2020' and '31/12/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 48);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2021' and '31/01/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 49);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/02/2021' and '28/02/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 50);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/03/2021' and '31/03/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 51);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/04/2021' and '30/04/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 52);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/05/2021' and '31/05/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 53);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/06/2021' and '30/06/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 54);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/07/2021' and '31/07/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 55);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/08/2021' and '31/08/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 56);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/09/2021' and '30/09/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 57);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/10/2021' and '31/10/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 58);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/11/2021' and '30/11/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 59);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/12/2021' and '31/12/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 60);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2022' and '31/01/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 61);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/02/2022' and '28/02/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 62);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/03/2022' and '31/03/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 63);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/04/2022' and '30/04/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 64);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/05/2022' and '31/05/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 65);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/06/2022' and '30/06/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 66);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/07/2022' and '31/07/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 67);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/08/2022' and '31/08/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 68);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/09/2022' and '30/09/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 69);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/10/2022' and '31/10/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 70);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/11/2022' and '30/11/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 71);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/12/2022' and '31/12/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 72);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2023' and '31/01/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 73);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/02/2023' and '28/02/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 74);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/03/2023' and '31/03/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 75);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/04/2023' and '30/04/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 76);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/05/2023' and '31/05/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 77);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/06/2023' and '30/06/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 78);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/07/2023' and '31/07/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 79);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/08/2023' and '31/08/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 80);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/09/2023' and '30/09/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 81);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/10/2023' and '31/10/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 82);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/11/2023' and '30/11/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 83);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/12/2023' and '31/12/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 84);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2017' and '31/12/2017' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 85);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2018' and '31/12/2018' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 86);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2019' and '31/12/2019' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 87);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2020' and '31/12/2020' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 88);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2021' and '31/12/2021' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 89);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2022' and '31/12/2022' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 90);''')

for x in range(1, result+1):
    cursor.execute('''insert into fato_mortos(quantidade, cod_localizacao, cod_tempo) values(
    (select count(*) from
    (select * 
    from acidentes inner join secao on acidentes.id_secao=secao.id 
    inner join acidente_veiculo_pessoa on acidentes.id=acidente_veiculo_pessoa.id_acidente
    inner join pessoa on pessoa.id=acidente_veiculo_pessoa.id_pessoa, localizacao1
    where data_acidente between '01/01/2023' and '31/12/2023' 
    and mortos>0 
    and localizacao1.cidade=secao.cidade and localizacao1.estado=secao.estado
    and localizacao1.id=''' +str(x) +''')), ''' + str(x) + ''', 91);''')

conn.commit()