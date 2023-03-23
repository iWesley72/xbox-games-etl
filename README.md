# ETL do Catálogo de Jogos Xbox
<p>Projeto de ETL da lista de jogos disponíveis para Xbox</p>

## Objetivos do projeto
<ul>
  <li>Automatizar a coleta de dados do catálogo;</li>
  <li>Tratar os dados;</li>
  <li>Conhecer a biblioteca psycopg2;</li>
  <li>Carregar os dados em um data warehouse local.</li>
</ul>

## Inicializar o ambiente
<p>Para inicializar o ambiete execute no terminal "source venv/bin/activate".</p>

## Notas/observações
<ul>
  <li>Eu não conhecia métodos de passar os dados do arquivo CSV para o postgre, então de início fiz por iteração(idéia horrível, eu sei), depois encontrei o método .copy_from().</li>
  <li>Pretendo voltar nesse repositório para corrigir a forma que inseri os dados das dimensões, acho que o método que usei para a tabala fato foi bom pro momento, além de tentar otimizar alguns processos.</li>
</ul>
