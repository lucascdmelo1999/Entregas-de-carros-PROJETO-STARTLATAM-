## Pré-Requisitos

* Conhecimento básico de git (git add .; git commit -m "msg"; git push; git pull, git merge)
* [Trilha trailhead do DX](https://trailhead.salesforce.com/content/learn/trails/sfdx_get_started)
* Conexão com a VPN da OI
 
# Etapas de instalação e configuração do ambiente

## GIT

* ### Instalação

    * Acessar o link [Git](https://git-scm.com/download/win) para o download do git.

## Chave SSH

* ### Gerar chave .SSH

    * Executar o programa git-bash.exe
    * Inserir o comando ssh-keygen -t RSA -C “Seu Email da OI“
    * Será apresentado a seguinte mensagem ```"Enter file in which to save the key (/c/Users/seu_usuario/.ssh/id_rsa):"``` aperte a tecla Enter
    * Será apresentado a seguinte mensagem ```"Enter passphrase (empty for no passphrase):"```, essa parte serve para gerar uma senha que será utilizada antes de realizar o commit, caso não deseje informar uma senha apenas aperte a tecla Enter
    * Será apresentado a seguinte mensagem "Enter same passphrase again:", caso tenha inserido uma senha no passo anterior, só inseri-la novamente, caso tenha deixado em branco apenas apertar a tecla Enter
    * Para mostrar a chave SSH Pública cat ~/.ssh/id_rsa.pub
    * Copie todo o conteudo da chave id_rsa.pub
    * Acessar a página página do [AzureDevOps](https://dvspw02a.oi.corp.net/devops), logar com seu usuário, ir no canto superior direito da tela e clicar em User settings, acessar a opção SSH public keys, canto superior direito clique em ```New key``` , no ```Nome``` colocque seu Email OI em ```Public Key Data``` cole a chave do arquivo id_rsa.pub e clique no botão ```Add```

## SFDX CLI

* ### Instalação 
    
    * Acesse o link [SFDX-CLI](https://developer.salesforce.com/tools/sfdxcli) para o download do DX. Clique na imagem do ```Windows``` e no botão ```Download for Windows 64```

## VSCODE

* ### Instalação
    
    * Acessar o link [VSCode](https://code.visualstudio.com/download) para o download do VSCode. Clicar na opção de 64 bits do windows e realizar a instalação assim que o download for concluído

* ### Configuração do ambiente do VSCode
    
    * Após instalado acesse as extensões do vscode localizada na barra do lado esquerdo do programa
    * Acesse a barra de pesquisa de extensões e pesquise por
    
    1. Salesforce Package.xml Generator Extension for VS Code 
    2. Salesforce Extension Pack 
    3. Git history
    4. Gitlens
    5. Apex-pmd


## Ambiente de Desenvolvimento

1. Selecionar a Story no quadro kanban (RALLY) e veja suas Us para começar o seu desenvolvimento.

2. Abra seu Gitbash obter repositório  com o comando:

    $ git clone <link http ou ssh do repositorio>

3. Entre no diretório 'DIRETORIO DO PROJETO' para entrar na branch de Dev "git checkout rc/yyyyMMdd/Dev" e criar suas branch escopo/Us0000 para começar a gerar seus pacotes.

    $ cd "DIREOTRIO DO PROJETO"

4. Criar uma branch a partir da branch **rc/yyyyMMdd/Dev**.  [Repository > Branches > New Branch.]

5. Esse branch precisa ter o padrão **tipo_da_branch/Issue_ID_Raly**. Exemplo: **escopo/Us0000**.

6. No final do dia ou quando for subir seu pacote para o repositorio do Azure, utilize os seguintes códigos:
    ## AVISO : sempre verificar se você está dentro da sua branch antes do commit.

    1. $ git status
    2. $ git add .
    3. $ git commit -m "HISTÓRIA - Nome da US - Comentário sobre a alteração ou adição realizada"
        Ex:  $ git commit -m "Feature-110 - Conexão com o banco de dados- implementação da conexão do banco de dados"
    4. $ git push origin <branch de trabalho>
        Ex: $ git push origin escopo/Us0000







