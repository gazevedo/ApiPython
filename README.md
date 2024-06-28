**Webapi Python**

Nesta tarefa, foi desenvolvida uma API utilizando o framework Flask em Python, com o objetivo de estudo da linguagem python. 

**Detalhamento das Funcionalidades Implementadas:**

-Listagem de Funcionários: Implementada através da rota /listafuncionario, que retorna uma lista com os nomes de todos os funcionários registrados na folha de pagamento.

-Total da Folha de Pagamento: A funcionalidade disponível na rota /totalfolha calcula e retorna o valor total da folha de pagamento, somando os salários de todos os funcionários.

-Detalhes da Folha de Pagamento: A rota /folha retorna todos os dados da folha de pagamento em formato JSON, incluindo informações como nome do funcionário, código e salário.

-Consulta de Funcionário por Código: Implementada na rota /funcionario/<codigo>, que permite consultar e retornar detalhes específicos de um funcionário através do seu código único.

-Atualização de Salário: A rota /atualizarSalario possibilita a atualização do salário de um funcionário especificado pelo seu código, utilizando requisições do tipo POST com dados em formato JSON.

-Exclusão de Funcionário: Implementada na rota /excluirFuncionario/<codigo>, que permite remover um funcionário do sistema com base no seu código, utilizando requisições do tipo DELETE.

**Tecnologias Utilizadas:**

Flask: Utilizado como framework principal para o desenvolvimento da API, proporcionando uma estrutura leve e flexível para criação das rotas HTTP.
pandas: Biblioteca utilizada para a manipulação de dados, facilitando a leitura e escrita em arquivos CSV contendo informações da folha de pagamento.
