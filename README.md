# Projeto-2-SEL0456
O projeto 2 tem como objetivo a introdução a python, para isso será criado uma classe para o controle de usuários.

## Como Funciona o programa
Foi criado uma classe User para realização da criação de usuários. Nela tem a definição de cada uma das variáveis nescessárias (nome, senha e cargo) para caracterizar um usuário. Para o bom funcionamento, foi realizaddo todo o tratamento de erro nescessário, de modo que ao inserir um dado que não condiz com as regras estabelecidas você será notificado e receberá a oportunidade de inserir novamente.
### Criptografia da senha 
Para garantir a segurança foi realizado a criptografia das senhas utilizando a sha256 da bilbioteca hashlib, que nos permite armazenar a informação de um dado em 32 bytes (256 bits) de caracteres completamente aleatórios. 
### Armazenamento de Usuários
Assim, para que fosse possível armazenar todos os usuarios, com todas as suas informações, utilizei a extensão json do pyton. Ela nos permite armazenar irfomações em forma de dicionário. E para agrupar todos os dicionarios (cada dicionário representa um usuário) coloquei todos eles dentro de uma lista.
Portanto, todos os usuários quando forem criados serão armazenados no arquivo usuarios.json.