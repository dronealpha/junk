<br><h1># junk</h1>
<br>Aplicação para coletar informações do valor de ativos da bovespa usando a sigla da compania com refrencia
<br>
<br>#Arquitetura
<br>Linguagem:Python
<br>Banco:MySQL
<br><h2>Como funciona</h2><br>
<br>Descrição:Sistema realiza uma requisição para um serviço rest que retorna um json com payload e uma metadata da empresa.
<br>Após resposta da requisição o sistema pega e trata apenas o paylo da mensagem e gerar string sql para insert em banco.
