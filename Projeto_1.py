def limpa_texto(cad_carateres):
    "Esta funcao recebe uma cadeira de carateres e devolve a mesma cadeia sem carateres brancos"
    cad_carateres=cad_carateres.replace('\t',' ') #substitui tab por espaço
    cad_carateres=cad_carateres.replace('\n',' ')
    cad_carateres=cad_carateres.replace('\v',' ')
    cad_carateres=cad_carateres.replace('\f',' ')
    cad_carateres=cad_carateres.replace('\r',' ')
    cad_carateres=" ".join(cad_carateres.split()) #remove vários espaços em branco
    cad_carateres=cad_carateres.strip() #remove espaços em branco no inicio e no final do texto

    return(cad_carateres)

def corta_texto(cad_carateres,largura):
    """ Esta funcao recebe uma cadeia de carateres e uma largura e devolve duas cadeias de carateres 
    
    Returns:
        Uma com todas as palavras completas até ao comprimento dado pela largura e a outra com o resto das palavras
    """
    cad_carateres_inicio=""
    cad_carateres_resto=""

    palavras=cad_carateres.split(" ")
    if len(palavras) == 0:
        return (cad_carateres_inicio, cad_carateres_resto)
        
    for i in range(len(palavras)):
        if (len(cad_carateres_inicio) == 0):
            aux = palavras[i]
        else:
            aux = cad_carateres_inicio + " " + palavras[i]

        if len(aux) > largura:
            cad_carateres_resto = ' '.join(palavras[i:])
            break
        else:
            cad_carateres_inicio = aux

    return (cad_carateres_inicio.strip(), cad_carateres_resto.strip())

def insere_espacos(cad_carateres,largura):
    "Esta funcao recebe uma cadeia de carateres e uma largura e devolve uma cadeia de carateres"
    cad_carateres_inicio=cad_carateres[:largura]
    total_occurrences = cad_carateres_inicio.count(" ") #contar numero de carateres espaço

    #acrescentar espaços caso tenha mais que 1 palavra
    if total_occurrences >= 1:
        cad_carateres_espacos_final=cad_carateres_inicio.ljust (largura) #cadeia de carateres com espaços no final
        total_occurrences1 = cad_carateres_espacos_final.count(" ") #verificar quantos espaços são necessários

        #caso seja preciso acrescentar espaços
        if total_occurrences1 != total_occurrences:
            espacos_acrescentar = int((total_occurrences1 - total_occurrences)/total_occurrences) #ver o valor inteiro menor que o número de espaços necessários
            
            #vetor com numero de espaços a acresentar
            espacos = []
            for i in range(total_occurrences):
                espacos.append(espacos_acrescentar+1) #acrescentar o espaço inicial
            espacos.append(0) #acrescentar 0 no final do array para concatenar com o array das palavras - lista_palavras
            
            #percorrer o array para inserir os espaços em falta em relação ao valor inteiro mais baixo - espacos_acrescentar
            i=0
            while sum(espacos)<total_occurrences1:
                espacos[i]+=1
                i +=1

            #criar a lista de palavras
            lista_palavras=cad_carateres_inicio.split()
            
            #concatenar as palavras com os espaços
            cad_carateres_inicio = ""
            for i in range(len(espacos)):
                cad_carateres_inicio = cad_carateres_inicio + lista_palavras[i]
                cad_carateres_inicio = cad_carateres_inicio + " "*espacos[i]

    else:
        #caso só tenha uma palavra acrescentar espaços no final
        cad_carateres_inicio=cad_carateres_inicio.ljust (largura)

    return(cad_carateres_inicio)
  

def justifica_texto(cad_carateres,largura):
    """ Esta funcao recebe uma cadeia de carateres e uma largura e devolve uum tuplo com o texto justificado 
    Argumentos:
        cad_carateres: uma string
        largura: um inteiro
    """
    errorMessage = "justifica_texto: argumentos invalidos";

    if not isinstance(largura,int) or largura<0: #verificacao de argumentos
        raise ValueError(errorMessage)

    if not isinstance(cad_carateres, str) or len(cad_carateres) == 0: #verificacao de argumentos
        raise ValueError(errorMessage)

    palavras = cad_carateres.split(' ')
    for palavra in palavras: #verificacao de argumentos
        if len(palavra) > largura:
            raise ValueError(errorMessage)
    
    restante=limpa_texto(cad_carateres)
    resultado=[]
    while len(restante) > 0: 
        inicio, restante = corta_texto(restante,largura)
        resultado.append(inicio)
    
    for i in range(len(resultado)-1) :
        resultado[i] = insere_espacos(resultado[i],largura)

    resultado[len(resultado)-1] = resultado[len(resultado) - 1].ljust(largura)

    return tuple(resultado)

def calcula_quocientes(dicionario, n):
    "Esta funcao recebe um circulo eleitoral e um numero de deputados a atribui e retorna uma lista com os quocientes calculados atraves do metodo de Hondt"
    novo_dict = {}
    for key, value in dicionario.items(): #percorre o nome dos partidos e o numero de votos
        quocientes = []
        for i in range(1, n+1):
            quocientes.append(value / i) #adiciona cada quociente a lista
        novo_dict[key] = quocientes
    return novo_dict

"""Esta funcao recebe:
    dicionario=um circulo eleitoral 
    n=um numero de deputados 
    Atraves da funcao anterior retorna uma lista com o nome desse partido a medida que os mandatos sao atribuidos"""
def atribui_mandatos(dicionario, n):
   
  q = calcula_quocientes(dicionario, n)
  res = []
  for i in range(0, n):
    global_p = ""
    global_m = float("-inf")

    for partido, quocientes in q.items():
      #sort
      quocientes.sort(reverse=True)
      
      local_m = quocientes[res.count(partido)]

      if local_m > global_m or (local_m == global_m and dicionario[partido] < dicionario[global_p]):
        global_m = local_m
        global_p = partido
    
    res.append(global_p)

  return res

def obtem_partidos(dicionario):
    "Esta funcao recebe varios circulos eleitorais e devolve a lista dos partidos que concorreram nas eleiçoes"
    partidos = []
    for x in dicionario.values():
      partidos += list(x["votos"].keys())
    return sorted(list(set(partidos))) #ordena por ordem alfabetica

def obtem_resultado_eleicoes(dicionario):
    "Esta funcao recebe os mesmos circulos eleitorais e devolve o resultado das eleicoes utilizando as funcoes anteriores"
    errorMessage = "obtem_resultado_eleicoes: argumento invalido"
    #join
    contagem = {}
    n_mandatos = {}

    if not isinstance(dicionario, dict) or len(dicionario) == 0: #verificacao de argumentos
        raise ValueError(errorMessage)

    for nome, circulo_eleitoral in dicionario.items():
        if not isinstance(nome,str) or len(nome) == 0: #verificacao de argumentos
            raise ValueError(errorMessage)
        if not isinstance(circulo_eleitoral, dict) or len(circulo_eleitoral) != 2: #verificacao de argumentos
            raise ValueError(errorMessage)

        if not "votos" in circulo_eleitoral or not "deputados" in circulo_eleitoral: #verificacao de argumentos
            raise ValueError(errorMessage)    

        votos = circulo_eleitoral["votos"]
        deputados = circulo_eleitoral["deputados"]

        if not isinstance(deputados, int) or deputados < 1 or not isinstance(votos, dict) or len(votos) < 1: #verificacao de argumentos
            raise ValueError(errorMessage)
        
        #conta votos
        for partido, n_votos in votos.items():
            if not isinstance(n_votos, int) or n_votos < 1 or not isinstance(partido, str) or len(partido) == 0: #verificacao de argumentos
                raise ValueError(errorMessage)

            contagem[partido] = contagem.get(partido, 0) + n_votos        

        mandatos = atribui_mandatos(votos, circulo_eleitoral["deputados"])

        #conta mandatos
        for partido in set(mandatos):
            n_mandatos[partido] = n_mandatos.get(partido, 0) + mandatos.count(partido)  


    res = []
    for partido in contagem:
        res.append((partido, n_mandatos.get(partido, 0), contagem.get(partido, 0)))
    #ordenar
    res.sort(key=lambda x: (x[1], x[2]), reverse=True)

    return res

def produto_interno(vetor1,vetor2):
    "Recebe dois vetores e retorna o produto interno entre ambos"
    res=float(0)
    for i in range(len(vetor1)): #percorrer o v1 e faz a multiplicacao com a mesma entrada do v2
        res+=(vetor1[i]*vetor2[i])
    return res

def verifica_convergencia(matriz, vetor_constantes, soluçao_atual, precisao):
    """ Esta funcao recebe tres tuplos e um inteiro, devolvendo um tuplo booleano
     Argumentos:
        matriz=uma linha da matriz quadrada
        vetor_constantes=um vetor das constantes
        precisao=precisao pretendida

    Return: Um tuplo com a resolucao do sistema
    """
    for i in range(len(matriz)): #percorre as linhas da matriz
        valor_abs_erro=abs(produto_interno(matriz[i],soluçao_atual)-vetor_constantes[i])
        if valor_abs_erro >= precisao: #compara o valor abs do erro com a precisao ate que esta nos agrade
            return False
    return True

def retira_zeros_diagonal(matriz, vetor_constantes):
    "Esta funcao recebe uma matriz e um vetor de constantes e devolve a matriz sem zeros na diagonal, atualizando tambem o vetor"
    matriz_res=list(matriz)
    vetor_res=list(vetor_constantes)
    for i in range(len(matriz)):
        if matriz_res[i][i] == 0:
            for j in range(len(matriz)):
                if matriz_res[j][i] != 0 and matriz_res[i][j] != 0:
                    troca_linhas(matriz_res, vetor_res, i, j)
                    break
                    
    return tuple(matriz_res), tuple(vetor_res)

def troca_linhas(matriz_res, vetor_res, i, j):
    "Troca as linhas"
    aux=matriz_res[i]
    matriz_res[i]=matriz_res[j]
    matriz_res[j]=aux
    aux=vetor_res[i]
    vetor_res[i]=vetor_res[j]
    vetor_res[j]=aux

def eh_diagonal_dominante(matriz):
    "Recebe uma matriz, verifica se é diagonal dominante e devolve um booleano"
    for i in range(len(matriz)):
        soma=0
        for j in range(len(matriz)):
            if i != j:
                soma+=abs(matriz[i][j]) #soma dos valores que nao estao na diagonal
        if abs(matriz[i][i]) < soma:
            return False
    return True

def resolve_sistema(matriz, vetor_constantes, precisao):
    """ Esta funcao recebe tres tuplos e um inteiro, devolvendo um tuplo booleano
    Argumentos:
        matriz=uma linha da matriz quadrada
        vetor_constantes=um vetor das constantes
        solucao_atual=vetor com a solucao atual
        precisao0=precisao pretendida

    Return: True se precisao nos satisfaz, False caso contrario
    """

    errorMessage = "resolve_sistema: argumentos invalidos"
    
    if not isinstance(precisao, float) or precisao < 0: #verificacao de argumentos
        raise ValueError(errorMessage)

    if not isinstance(matriz, tuple) or not isinstance(vetor_constantes, tuple) or len(matriz) != len(vetor_constantes): #verificacao de argumentos
        raise ValueError(errorMessage)

    for elemento in vetor_constantes:
        if not (isinstance(elemento, float) or isinstance(elemento, int)): #verificacao de argumentos
            raise ValueError(errorMessage)

    for linha in matriz:
        if not isinstance(linha, tuple) or len(linha) != len(matriz): #verificacao de argumentos
            raise ValueError(errorMessage)

        for elemento in linha:
            if not (isinstance(elemento, float) or isinstance(elemento, int)): #verificacao de argumentos
                raise ValueError(errorMessage)

    matriz, vetor_constantes = retira_zeros_diagonal(matriz, vetor_constantes) #retira os zeros da diagonal, afetando o vetor das constantes

    if not eh_diagonal_dominante(matriz):
        raise ValueError ("resolve_sistema: matriz nao diagonal dominante") #verificacao de argumentos
    
    solucao_atual=[0] * (len(vetor_constantes))
    while not verifica_convergencia(matriz, vetor_constantes, solucao_atual, precisao): 
        solucao_pendente=[0] * (len(vetor_constantes))
        for i in range(len(matriz)):
            solucao_pendente[i] = solucao_atual[i] + (vetor_constantes[i] - produto_interno(matriz[i], solucao_atual)) / matriz[i][i]
        solucao_atual=solucao_pendente[:]

    return solucao_atual
