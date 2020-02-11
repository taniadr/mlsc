"# mlsc"

1------------------ SETUP <br>

In order to run, clone this repo in your PC and change to its directory. Then, run the following commands: <br>

"pip install virtualenv env" 

"env\Scripts\activate"  

At this point, you should be able to see (env) in front of your command line<br>

Now, run the command bellow and check the output once its concluded. 

2------------------ RUNNING <br>

O programa pede para você entrar um termo para buscar. Recomendo usar "cookbook" e "cadeado" seguido da tecla enter.

scrapy runspider spider.py -t json -o "output.json"


![mlsc_prompt1](/images/prompt1.png)
Prompt1: Execução 


![mlsc_prompt2](/images/prompt2.png)
Prompt2: Resultado após execução estará no arquivo output.json, no diretório do projeto e do spider.


3------------------ NEXT STEPS <br>

Para melhoria deste projeto, intenciona-se a junção da api abaixo com o backend mlsc.
A integração do Scrapy com o Flask não é trivial, e a proposta é usar após um POST, a chamada

subprocess.check_output(['scrapy', 'runspider', spider_name, '-t', 'json', '-o', 'output.json']) 

mas ainda não deu certo. Essa versão vai estar no repo FullStack_MLSC.

![mlsc_api](/images/API_poc.png)
API: Prova de Conceito
