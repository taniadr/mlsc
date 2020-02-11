"# mlsc" - Scrapper para obter dados determinado produto do mercado livro, limitado pela quantidade dada pelo usuário.

1------------------ SETUP <br>

Clone o repositório, e caso necessário, instale o virtualenv para obter as dependências necessárias: <br>

*pip install virtualenv env*

*env\Scripts\activate*

Caso a operação tenha sido um sucesso, você verá um ' (env) ' na frente da sua command line.

2------------------ RUNNING <br>

O programa pede para você entrar um termo para buscar. O scraper foi testado com 'cookbook' e 'cadeado'.

*scrapy runspider spider.py -t json -o "output.json"*


![mlsc_prompt1](/images/prompt1.png)
Prompt1: Execução 


![mlsc_prompt2](/images/prompt2.png)
Prompt2: Resultado após execução estará no arquivo output.json, no diretório do projeto e do spider.


3------------------ NEXT STEPS <br>

Para melhoria deste projeto, intenciona-se a junção da api abaixo com o backend mlsc.
A integração do Scrapy com o Flask não é trivial, e a proposta é usar após um POST, a chamada

*subprocess.check_output(['scrapy', 'runspider', spider_name, '-t', 'json', '-o', 'output.json']) *

mas ainda não deu certo. Essa versão vai estar no repo FullStack_MLSC.

![mlsc_api](/images/API_poc.png)
API: Prova de Conceito
