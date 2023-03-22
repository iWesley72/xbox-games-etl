'''
    Precisamos inserir os dados nas tabelas dimensões(dim_jogo e dim_classificacao), e então inserir os dados da nossa tabela fato.
'''


import pandas as pd
import numpy as np
import psycopg2
import csv


df = pd.read_csv('dadosTratado.csv', sep=';')
classificacoes = df['classificacao'].unique()


try:
    connection = psycopg2.connect(
        user='wesley',
        password='admar77mara77',
        host='127.0.0.1',
        port='5432',
        database='xboxgamelist'
    )

    cursor = connection.cursor()


    """
        O bloco a seguir insere as classificações encontradas para a tabela dim_classificacao enquanto verifica se o registro já existe, e se já existir ele não insere dado algum.
    """
    query = """DO $$
    BEGIN
    IF  NOT EXISTS (SELECT classificacao FROM dim_classificacao WHERE classificacao = %s) THEN
    INSERT INTO dim_classificacao (classificacao) VALUES (%s);
    END IF;
    END;
    $$
    """
    for i in classificacoes:
        cursor.execute(query, (i, i, ))
        connection.commit()
    print('Dados inseridos com sucesso na tabela dim_classificacao.')

    """
        O bloco a seguir insere o nome dos jogos encontradas para a tabela dim_jogo enquanto verifica se o registro já existe, e se já existir ele não insere dado algum.
    """


    query = """DO $$
    BEGIN
    IF NOT EXISTS (SELECT * FROM dim_jogo WHERE nome = %s) THEN
    INSERT INTO dim_jogo (nome) VALUES (%s);
    END IF;
    END;
    $$
    """
    for i in df['nome']:
        cursor.execute(query, (i, i, ))
        connection.commit()
    print('Dados inseridos com sucesso na tabela dim_jogo.')

    """
        O bloco a seguir popula a tabela fato fat_lista
    """
    with open('dadosTratado.csv') as csvFile:
        next(csvFile)
        cursor.copy_from(csvFile, 'fat_lista', sep=';', null='')
        connection.commit()


except (Exception, psycopg2.Error) as error:
    print("Erro ao inserir dados na tabela", error)