# pyQualis
 O pacote pyQualis foi desenvolvido com o objetivo de permitir realizar consultas das notas de qualis-periódicos.



## ⚙️ Instalando

Para instalar a `pyQualis`, basta realizar o download do projeto e usar o comando `pip install `. 

```bash
foo@bar:~/pyQualis$ pip install .
```

ou apenas fazer pip diretamente deste repositório do **github**, é necessário possuir o `git`instalado.

```bash
foo@bar:~$ pip install git+https://github.com/JessicaSousa/pyQualis.git
```



## 📝Como usar a `pyQualis`

A `pyQualis` realiza o download da tabela de dados de *qualis* disponíveis na página do Sucupira para todas as áreas e todos os eventos, a atualização dos arquivos locais pode ser feita através do método`update_data` disponível na classe `Search` .

## Atualizando dados

```python
from pyQualis import Search

search = Search()
print(search.get_last_update())
#>'18/02/2020 18:37:54'

search.update_data()
#>'18/02/2020 21:23:30'
```



## Acessando os dados

> O argumento `event` aceita apenas as palavras `triênio` e `quadriênio`, por padrão é preenchido como `triênio`.

```python
from pyQualis import Search

search = Search()
trien = search.get_table(event="triênio")
#>>> trien.head()
#        ISSN                                            Título                                  Área de Avaliação Estrato
#0  0102-6720  ABCD. Arquivos Brasileiros de Cirurgia Digestiva  ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E TURISMO   ...      B1
#1  1980-4814                       ABCustos (São Leopoldo, RS)  ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E TURISMO   ...      B4
#2  1516-618X                                    ABMES Cadernos  ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E TURISMO   ...      B5
#3  1012-8255                                Academia (Caracas)  ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E TURISMO   ...      B1
#4  2048-9803         Academic Publishing International Limited  ADMINISTRAÇÃO, CIÊNCIAS CONTÁBEIS E TURISMO   ...      B4
```

As consultas ainda podem ser filtradas de acordo com a área, ISSN, estrato e título da revista.

```python
from pyQualis import Search

search = Search()
comp = search.by_area("computação")

#>>> comp.head()
#            ISSN                 Título                                  Área de Avaliação Estrato
#12709  2316-9451                 Abakós  CIÊNCIA DA COMPUTAÇÃO                         ...      C 
#12710  1076-6332     Academic Radiology  CIÊNCIA DA COMPUTAÇÃO                         ...      B2
#12711  1519-7859        Ação Ergonômica  CIÊNCIA DA COMPUTAÇÃO                         ...      C 
#12712  0360-0300  ACM Computing Surveys  CIÊNCIA DA COMPUTAÇÃO                         ...      A1
#12713  2153-2184            ACM Inroads  CIÊNCIA DA COMPUTAÇÃO                         ...      B4
```

