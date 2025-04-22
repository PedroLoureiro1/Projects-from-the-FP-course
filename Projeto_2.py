#TAD Gerador
def cria_gerador(b, s):
    """Esta recebe um numero de bits e uma seed e retorna um gerador de numeros pseudo-aleatorios xorshift"

    Args:
        b (int): bits
        s (int): seed

    Raises:
        ValueError: Quando os bits sao diferentes de 32/64 e a nao esta entre 0 e 2**bits

    Returns:
        dicionario(gerador): gerador
    """
    if type(b) != int or (b != 32 and b != 64) or type(s) != int or s <= 0 or s>2**b-1:
        raise ValueError ("cria_gerador: argumentos invalidos")

    return { "bits": b, "state": s }

def cria_copia_gerador(g):
    """Recebe um gerador e devolve uma copia nova do mesmo

    Args:
        g (dicionario(gerador)): _description_

    Returns:
        dicionario(gerador): copia do dicionario introduzido
    """
    return g.copy()

def obtem_estado(g):
    """Esta funcao recebe um gerador e devolve o seu estado

    Args:
        g (int): estado

    Returns:
        _type_: Devolve o estado atual do gerador g(introduzido)
    """
    return g["state"]

def define_estado(g, s):
    """Define o novo valor do estado do gerador como sendo s

    Args:
        g (int): gerador
        s (int): seed

    Returns:
        int: Devolve s com um novo valor
    """
    g["state"] = s
    return s

def atualiza_estado(g):
    """Atualiza o estado do gerador g de acordo com o algoritmo xorshift de geracao de numeros pseudoaleatorios

    Args:
        g (gerador): gerador

    Returns:
        int: Devolve o estado atualizado
    """
    if (g["bits"] == 32):
        g["state"] ^= ( g["state"] << 13 ) & 0xFFFFFFFF 
        g["state"] ^= ( g["state"] >> 17 ) & 0xFFFFFFFF 
        g["state"] ^= ( g["state"] << 5 ) & 0xFFFFFFFF
    elif (g["bits"] == 64):
        g["state"] ^= ( g["state"] << 13 ) & 0xFFFFFFFFFFFFFFFF
        g["state"] ^= ( g["state"] >> 7 ) & 0xFFFFFFFFFFFFFFFF 
        g["state"] ^= ( g["state"] << 17 ) & 0xFFFFFFFFFFFFFFFF
    
    return g["state"]

def eh_gerador(arg):
    """Verifica se o argumemnto introduzido e ou nao um gerador

    Args:
        arg (gerador): gerador

    Returns:
        booleano: Devolve True se for gerador e False caso contrario
    """
    return type(arg) == dict and len(arg)== 2 and "bits" in arg and "state" in arg

def geradores_iguais(g1, g2):
    """Verifica se os dois geradores introduzidos sao iguais

    Args:
        g1 (gerador): gerador
        g2 (gerador): gerador

    Returns:
        booleano: Devolve True se forem iguais e False caso contrario
    """
    if eh_gerador(g1) and eh_gerador(g2):
        if g1["bits"]==g2["bits"] and g1["state"]==g2["state"]:
            return True
    return False

def gerador_para_str(g1):
    """Recebe um gerador e transforma-o para string

    Args:
        g1 (gerador): gerador

    Returns:
        str: Devolve a cadeia de caracteres que representa o gerador
    """
    return "xorshift"+str(g1["bits"])+"(s=" + str(g1["state"])+ ")"

def gera_numero_aleatorio(g, n):
    """Recebe um gerador e um numero maximo de um intervalo e atualiza o estado do gerador, gerando um numero

    Args:
        g (gerador): gerador
        n (int): numero maximo do intervalo

    Returns:
        int: Devolve um numero dentro do intervalo gerado pseudo_aleatoriamente
    """
    s=atualiza_estado(g)
    return (1+s%n)

def gera_carater_aleatorio(g, c):
    """Esta funcao recebe um gerador e um caracter maximo de um intervalo e atualiza o estado do gerador, gerando um caracter aleatorio

    Args:
        g (gerador): gerador
        c (str): caracter maiusculo

    Returns:
        str: caracter entre "A" e o caracter c introduzido
    """
    s= atualiza_estado(g)
    return chr(ord("A")+s%(ord(c)-ord("A")+1))

# TAD Coordenada
def cria_coordenada(col, lin):
    """Esta funcao serve de construtor para uma coordenada

    Args:
        col (str): caracter referente a coluna
        lin (int): inteiro referente a linha

    Raises:
        ValueError: A coluna e constituida apenas por uma letra maiuscula entre A e Z e a linha e constituida por um numero entre 1 e 99 

    Returns:
        dicionario(coordenada): coordenada criada pela coluna e linha fornecida
    """
    if not isinstance(col, str) or len(col)!=1 or not(ord("A")<=ord(col)<=ord("Z")) or not isinstance(lin, int) or not 0<lin<100:
        raise ValueError("cria_coordenada: argumentos invalidos")
    return {"coluna": col, "linha": lin}

def obtem_coluna(coordenada):
    """Esta funcao deolve a coluna da coordenada

    Args:
        coordenada (dicionario): coordenada

    Returns:
        str: devolve  a coluna da coordenada introduzida
    """
    return coordenada["coluna"]

def obtem_linha(coordenada):
    """Esta funcao devolve a linha da coordenada

    Args:
        coordenada (dicionario): coordenada

    Returns:
        int: devolve a linha da coordenada
    """
    return coordenada["linha"]

def eh_coordenada(coordenada):
    """Esta funcao verifica se o argumento e uma coordenada

    Args:
        coordenada (dicionario): coordenada 

    Returns:
        booleano: Devolve True caso seja uma coordenada e False caso nao seja 
    """
    return type(coordenada) == dict and len(coordenada) == 2 and "coluna" in coordenada and "linha" in coordenada
        
def coordenadas_iguais(coordenada1, coordenada2):
    """Esta funcao verifica se as coordenadas sao iguais

    Args:
        coordenada1 (dicionario): coordenada
        coordenada2 (dicionario): coordenada

    Returns:
        booleano: Devolve True caso sejam iguais e False caso contrario
    """
    if eh_coordenada(coordenada1) and eh_coordenada(coordenada2):
        if obtem_coluna(coordenada1)==obtem_coluna(coordenada2) and obtem_linha(coordenada1)==obtem_linha(coordenada2):
            return True
    return False

def coordenada_para_str(coordenada):
    """Esta funcao converte a cordenada dada no argumetno para string

    Args:
        coordenada (dicionario): coordenada

    Returns:
        str: Devolve a string correspondente a coordenada
    """
    return f"{obtem_coluna(coordenada)}{obtem_linha(coordenada):02}"

def str_para_coordenada(coordenada_str):
    """Esta funcao converte uma string numa coordenada

    Args:
        coordenada_str (str): string correspondente a uma coordenada

    Returns:
        dicionario: Devolve a coordenada correspondente a string 
    """
    return cria_coordenada(coordenada_str[0], int(coordenada_str[1:]))

def obtem_coordenadas_vizinhas(coordenada):
    """Esta funcao devolve recebe uma coordenada e devolve, se existirem, as coordenadas vizinhas

    Args:
        coordenada (dicionario): coordenada

    Returns:
        tuple: Devovle um tuplo com todas as coordenadas vizinhas da coordenada passada no argumento
    """
    coordenadas_vizinhas=[]
    col=obtem_coluna(coordenada) #coluna
    col_anterior=chr(ord(col)- 1) #coluna_anterior
    col_seguinte=chr(ord(col)+ 1) #coluna_seguinte
    linha=obtem_linha(coordenada) #linha
    linha_anterior= linha - 1 #linha_anterior
    linha_seguinte= linha + 1  #linha_seguinte
    if linha_anterior > 0:
        if ord(col_anterior)>=ord("A"): #verificar se a coluna esta dentro do campo
            coordenadas_vizinhas.append(cria_coordenada(col_anterior, linha_anterior))
        coordenadas_vizinhas.append(cria_coordenada(col, linha_anterior))
        if ord(col_seguinte)<=ord("Z"):
            coordenadas_vizinhas.append(cria_coordenada(col_seguinte, linha_anterior))
    if ord(col_seguinte)<=ord("Z"): #verificar se a coluna esta dentro do campo
        coordenadas_vizinhas.append(cria_coordenada(col_seguinte, linha))
        if linha_seguinte<100: #verificar se a coluna esta dentro do campo
            coordenadas_vizinhas.append(cria_coordenada(col_seguinte, linha_seguinte))
    if linha_seguinte<100: #verificar se a coluna esta dentro do campo
        coordenadas_vizinhas.append(cria_coordenada(col, linha_seguinte))
        if ord(col_anterior)>=ord("A"): #verificar se a coluna esta dentro do campo
            coordenadas_vizinhas.append(cria_coordenada(col_anterior, linha_seguinte))
    if ord(col_anterior)>=ord("A"): #verificar se a coluna esta dentro do campo
        coordenadas_vizinhas.append(cria_coordenada(col_anterior, linha))

    return tuple(coordenadas_vizinhas)

def obtem_coordenada_aleatoria(c, g):
    """Esta funcao recebe uma coordenada e um gerador devolvendo uma coordenada gerada aleatoriamente

    Args:
        c (dicionario): coordenada
        g (dicionario): gerador

    Returns:
        dicionario(coordenada): Devolve uma coordenada gerada aleatoriamente dentro do "campo" definido pela coordenada do argumento
    """
    
    col=gera_carater_aleatorio(g, obtem_coluna(c)) #gerar uma coluna
    linha=gera_numero_aleatorio(g, obtem_linha(c)) #gerar uma linha
    return cria_coordenada(col, linha) #criar uma coordenada com os valores obtidos

#TAD Parcela

def cria_parcela():
    """Esta funcao serve para construtora do tipo parcela

    Returns:
        dicionario (parcela): Devolve a parcela criada
    """
    return {"estado": "tapada", "mina": False}

def cria_copia_parcela(p):
    """Esta funcao faz uma copia da parcela passada no argumento

    Args:
        p (dicionario): parcela

    Returns:
        dicionario: Devolve uma copia da parcela 
    """
    return p.copy()

def atualiza_estado_parcela(p, estado):
    """Esta funcao atualiza o estado de uma parcela

    Args:
        p (dicionario): parcela
        estado (string): estado

    Returns:
        dicionario: parcela
    """
    p["estado"] = estado
    return p

def obtem_estado_parcela(p):
    """Esta funcao verifica qual e o estado de uma parcela

    Args:
        p (dicionario): parcela

    Returns:
        str: estado
    """
    return p["estado"]


def limpa_parcela(p):
    """Esta funcao modifica o estado da parcela

    Args:
        p (dicionario): parcela

    Returns:
        parcela(dicionario): Devolve a parcela com o estado atualizado para "limpa"
    """
    return atualiza_estado_parcela(p,"limpa")
    

def marca_parcela(p):
    """Esta funcao modifica o estado da parcela

    Args:
        p (dicionario): parcela

    Returns:
        parcela(dicionario): Devolve a parcela com o estado atualizado para "marcada"
    """
    return atualiza_estado_parcela(p, "marcada")
    

def desmarca_parcela(p):
    """Esta funcao modifica o estado da parcela

    Args:
        p (dicionario): parcela

    Returns:
        parcela(dicionario): Devolve a parcela com o estado atualizando para "tapada"
    """
    return atualiza_estado_parcela(p, "tapada")
    

def esconde_mina(p):
    """Esta funcao esconde uma mina na parcela

    Args:
        p (dicionario): parcela

    Returns:
        parcela(dicionario): Devolve a parcela com mina
    """
    
    p["mina"] = True
    return (p)

def eh_parcela(p):
    """Esta funcao verifica se o argumento e parcela

    Args:
        p (dicionario): parcela

    Returns:
        booleano: Devolve True caso seja parcela e False caso nao seja
    """
    return isinstance(p, dict) and len(p) == 2 and "estado" in p and "mina" in p

def eh_parcela_tapada(p):
    """Esta funcao verifica se o estado da parcela e "tapada"

    Args:
        p (dicionario): parcela

    Returns:
        booleano: Devolve True caso o estado seja "tapada" e False caso contrario
    """
    return obtem_estado_parcela(p) == "tapada"

def eh_parcela_marcada(p):
    """Esta funcao verifica se o estado da parcela e "marcada"

    Args:
        p (dicionario): parcela

    Returns:
        booleano: Devolve True caso o estado seja "marcada" e False caso contrario
    """
    return obtem_estado_parcela(p) == "marcada"

def eh_parcela_limpa(p):
    """Esta funcao verifica se o estado da parcela e "limpa"

    Args:
        p (dicionario): parcela

    Returns:
        boolenao: Devolve True caso o estado seja "limpa" e False caso contrario
    """
    return obtem_estado_parcela(p) == "limpa"

def eh_parcela_minada(p):
    """Esta funcao verifica se parcela tem mina 

    Args:
        p (dicionario): parcela

    Returns:
        booelano: Devolve True caso a parcela tenha minha e False caso contrario
    """
    return p["mina"] == True

def parcelas_iguais(p1, p2):
    """Esta funcao recebe duas parcelas e verifica se sao iguais

    Args:
        p1 (dicionario): parcela
        p2 (dicionario): parcela

    Returns:
        booleano: Devolve True caso as parcelas seja iguais e False caso contario
    """
    return obtem_estado_parcela(p1) == obtem_estado_parcela(p2) and eh_parcela_minada(p1) == eh_parcela_minada(p2)

def parcela_para_str(p):
    """Esta funcao recebe uma parcela e converte-a para string

    Args:
        p (dicionario): parcela

    Returns:
        str: Devolve o simbolo correspondente ao estado
    """
    if eh_parcela_tapada(p): #identificar os diferentes tipos de hipoteses
        return "#"

    if eh_parcela_marcada(p): #identificar os diferentes tipos de hipoteses
        return "@"

    if eh_parcela_limpa(p): #identificar os diferentes tipos de hipoteses
        return "X" if eh_parcela_minada(p) else "?" 

def alterna_bandeira(p):
    """Esta funcao recebe uma parcela e desmarca-a se estiver marcada e vice versa

    Args:
        p (dicionario): parcela

    Returns:
        booleano: Devolve True se a parcela estiver marcada/desmarcada e False caso contrario
    """
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True

    if eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    return False

#TAD Campo

def cria_campo(col, lin):
    """Esta funcao forma um campo limitado pelos argumentos dados

    Args:
        col (str): coluna
        lin (int): linha

    Raises:
        ValueError: A coluna tem de ser uma letra maiuscula entre A e Z e uma linha com um numero inteiro entre 1 e 99

    Returns:
        campo(dicionario): Retorna um campo em que a ultima linha e ultima coluna sao as passadas nos argumentos
    """
    campo={"ultima_coluna": col, "ultima_linha": lin, "parcelas":{}}
    
    
    if not isinstance(col, str) or len(col)!=1 or not(ord("A")<=ord(col)<=ord("Z")) or not isinstance(lin, int) or not 0<lin<100:
        raise ValueError("cria_campo: argumentos invalidos") #verificacao de argumentos
    for linha in range(1, lin+1): #percorrer a linha
        for coluna in range(ord("A"), ord(col)+1): #depois percorrer a coluna
            c1=cria_coordenada(chr(coluna), linha)
            p1=cria_parcela()
            campo["parcelas"][coordenada_para_str(c1)] = p1 #de modo a que a ordem pedida seja respeitada
            
    return campo

def cria_copia_campo(campo):
    """Esta funcao gera uma copia do campo dado

    Args:
        campo (dicionario): campo

    Returns:
        dicionario: Retorna uma copia do campo
    """
    c2={}
    for k, v in campo.items():
        c2[k]=v
    for k, v in campo["parcelas"].items():
        c2["parcelas"][k]=cria_copia_parcela(v)

    return c2

def obtem_ultima_coluna(campo):
    """Esta funcao recebe um campo e devolve a ultima coluna do campo

    Args:
        campo (dicionario): campo

    Returns:
        str: Devolve a ultima colunna
    """
    return campo["ultima_coluna"]

def obtem_ultima_linha(campo):
    """Esta funcao recebe um campo e devolve a ultima linha desse campo

    Args:
        campo (dicionario): campo

    Returns:
        int: Devolve a ultima linha
    """
    return campo["ultima_linha"]

def obtem_parcela(campo, coordenada):
    """Esta funcao recebe um campo e uma coordenada e devolve uma parcela

    Args:
        campo (dicionario): campo
        coordenada (dicionario): campo

    Returns:
        dicionario: parcela
    """
    return campo["parcelas"][coordenada_para_str(coordenada)]

def obtem_coordenadas(campo, estado):
    """Esta funcao recebe um campo e um estado e retorna as coordenadas que possuem o estado atribuido

    Args:
        campo (dicionario): campo
        estado (str): estado

    Returns:
        tuple: Devolve as coordenadas ordenadas da esquerda para a direita
    """

    coordenadas=[]
    for coordenada, parcela in campo["parcelas"].items():

        if estado == "limpas" and eh_parcela_limpa(parcela): #adicionar a lista de coordenadas aquelas que forem do mesmo estado passado no argumento
            coordenadas.append(str_para_coordenada(coordenada))
        elif estado == "tapadas" and eh_parcela_tapada(parcela):
            coordenadas.append(str_para_coordenada(coordenada))
        elif estado == "marcadas" and eh_parcela_marcada(parcela):
            coordenadas.append(str_para_coordenada(coordenada))
        elif estado == "minadas" and eh_parcela_minada(parcela):
            coordenadas.append(str_para_coordenada(coordenada))
    return tuple(coordenadas)
            
def obtem_numero_minas_vizinhas(campo, coordenada):
    """Esta funcao recebe um campo e uma coordenada devolve o numero de parcelas vizinhas que contem uma mina

    Args:
        campo (dicionario): campo
        coordenada (dicionario): campo

    Returns:
        int: Devolve o numero de minas existentes nas parcelas das coordenadas vizinhas
    """
    coordenadas_vizinhas=obtem_coordenadas_vizinhas(coordenada)
    minas=0
    for coordenada_vizinha in coordenadas_vizinhas:
        if obtem_linha(coordenada_vizinha) > obtem_ultima_linha(campo) or ord(obtem_coluna(coordenada_vizinha)) > ord(obtem_ultima_coluna(campo)):
            continue
        if eh_parcela_minada(obtem_parcela(campo, coordenada_vizinha)): 
            minas+=1
    return minas

def eh_campo(campo):
    """Esta funcao verifica se o argumento e um campo

    Args:
        campo (dicionario): campo

    Returns:
        boolenao: Devolve True caso seja um campo e False caso contrario
    """
    return isinstance(campo, dict) and len (campo) == 3 and "ultima_coluna" in campo and "ultima_linha" in campo and "parcelas" in campo



def eh_coordenada_do_campo(campo, coordenada):
    """Esta funcao verifica se a coordenada do argumento pertence ao campo passado no mesmo

    Args:
        campo (dicionario): campo
        coordenada (dicionario): campo

    Returns:
        booleano: Devolve True caso a coordenada faca parte do campo e False caso contrario
    """
    return ord("A")<=ord(obtem_coluna(coordenada))<=ord(obtem_ultima_coluna(campo)) and 1<=obtem_linha(coordenada)<=obtem_ultima_linha(campo)

def campos_iguais(campo1, campo2):
    """Esta funcao verifica se os campos passados nos argumentos sao iguais

    Args:
        campo1 (dicionario): campo
        campo2 (dicionario): campo

    Returns:
        booelano: Caso os campos sejam iguais devolve True ou False caso contrarioo
    """
    if not eh_campo(campo1) or not eh_campo(campo2):
        return False
    if obtem_ultima_coluna(campo1) != obtem_ultima_coluna(campo2) or obtem_ultima_linha(campo1) != obtem_ultima_linha(campo2):
        return False
    for linha in range(1, obtem_ultima_linha(campo1)+1):
        for coluna in range(ord("A"), ord(obtem_ultima_coluna(campo1))+1): 
            c1=cria_coordenada(chr(coluna), linha)
            if not parcelas_iguais(obtem_parcela(campo1, c1), obtem_parcela(campo2, c1)):
                return False
    return True
        

def campo_para_str(campo):
    """Esta funcao converte o campo inserido no argumento para uma string equivalente 

    Args:
        campo (dicionario): campo

    Returns:
        str: Devolve uma string equivalente ao campo
    """
    col=ord("A")
    count=0
    lin=1
    campo_str="   "
    utlima_coluna=obtem_ultima_coluna(campo) #definir qual a ultima coluna
    ultima_linha=obtem_ultima_linha(campo) #definir qual a ultima linha
    while col <= ord(utlima_coluna): #enquanto a coluna for menor que a ultima coluna
            campo_str+=chr(col)
            count+=1 #contar o numero de "-" que vao ser necessarios no print do campo
            col+=1

    campo_str+="\n  +"+"-"*count+"+\n"

    while lin <= ultima_linha:
            campo_str+=f"{lin:02}"+"|"
            for col in range(ord("A"), ord(utlima_coluna)+1):
                coordenada = cria_coordenada(chr(col), lin)
                parcela = obtem_parcela(campo, coordenada)
                parcela_chr = parcela_para_str(parcela)
                if parcela_chr == "?":
                    minas_vizinhas=obtem_numero_minas_vizinhas(campo, coordenada)
                    parcela_chr = " " if minas_vizinhas == 0 else str(minas_vizinhas)  #quando se limpa fazer o replace de "?" para " " caso nao haja minas e "numero de minas vizinhas" caso haja
                campo_str+=parcela_chr
            campo_str+="|\n"
            lin+=1
    
    campo_str+="  +"+"-"*count+"+"
    return campo_str

def eh_coordenada_valida(a, c, vizinhas_c, m):
    """Esta funcao auxiliar serve para verificar se e plausivel por uma mina naquela coordenada

    Args:
        a (dicionario): coordenada aleatoria
        c (dicionario): coordenada
        vizinhas_c (tuple): coordenadas vizinhas
        m (dicionario): campo

    Returns:
        _booleano: Devolve True caso possa ter uma mina e False caso contrario
    """
    if coordenadas_iguais(a, c): #gerada igual a passada no argumento
        return False
    for vizinha in vizinhas_c:
        if coordenadas_iguais(a, vizinha): #gerada igual as vizinhas da passada no argumento
            return False
    if eh_parcela_minada(obtem_parcela(m, a)):
        return False
    return True


def coloca_minas(m, c, g, n):
    """Esta funcao modifica destrutivamente o campo escondendo "n" minas em parcelas dentro do campo. 
    As n coordenadas sao geradas em sequencia atraves do gerador "g" de modo a que nao coincidam co "c" ou suas vizinhas

    Args:
        m (dicionario): campo
        c (dicionario): coordenada
        g (dicionario): gerador
        n (int): numero inteiro

    Returns:
        dicionario: Devolve o campo atualizado
    """
    i=0
    vizinhas_c=obtem_coordenadas_vizinhas(c)
    coordenada_limite=cria_coordenada(obtem_ultima_coluna(m), obtem_ultima_linha(m)) #coordenada delimitativa do campo
    while i < n:
        a=obtem_coordenada_aleatoria(coordenada_limite, g)
        if eh_coordenada_valida(a, c, vizinhas_c, m): #validacao atraves da funcao auxiliar
            esconde_mina(obtem_parcela(m, a)) #esconder mina
            i+=1

    return m

def limpa_campo(campo, coordenada):
    """Esta funcao modifica destrutivamente o campo limpando a parcela na coordenada c e devolvendo-a.
    Se nao houver nenhuma mina vizinha escondida limpa todas as parcelas vizinhas tapadas

    Args:
        campo (dicionario): campo

        coordenada (dicionario): coordenada

    Returns:
        dicionario: Devolve o campo atualizado
    """
    parcela_coordenada=obtem_parcela(campo, coordenada) #definicao parcela de uma coordenada
    if eh_parcela_limpa(parcela_coordenada):
        return campo
    limpa_parcela(parcela_coordenada)
    if eh_parcela_minada(parcela_coordenada) or obtem_numero_minas_vizinhas(campo, coordenada) > 0:
        return campo
    
    
    vizinhas_coordenadas=obtem_coordenadas_vizinhas(coordenada) #coordenadas vizinhas
    for vizinha in vizinhas_coordenadas:
        if not eh_coordenada_do_campo(campo ,vizinha):
            continue
        parcela_vizinha=obtem_parcela(campo, vizinha)
        if eh_parcela_tapada(parcela_vizinha):
            limpa_campo(campo, vizinha)
    return campo

def jogo_ganho(campo):
    """Esta funcao recebe um campo e verifica se todas as parcelas sem minas estao limpas

    Args:
        campo (dicionario): campo

    Returns:
        booleano: Devolve True caso as parcelas sem minas estejam limpas e False caso contrario
    """
    tapadas=obtem_coordenadas(campo, "tapadas")
    minadas = obtem_coordenadas(campo, "minadas")
    marcadas=obtem_coordenadas(campo, "marcadas")
    return len(tapadas) + len (marcadas) == len(minadas) #se o numero de parcelas tapadas + numero de parcelas marcadas for igual as minadas, o jogo esta ganho

def input_coordenada(campo):
    """Esta funcao auxiliar serve para a verificacao da coordenada passada no input

    Args:
        campo (dicionario): campo

    Returns:
        dicionario: coordenada
    """
    while True:
        coordenada_string=input("Escolha uma coordenada:")
        if not isinstance(coordenada_string, str):
            continue
        if not len(coordenada_string) == 3 or not coordenada_string[1:].isnumeric() or not ord("A") <= ord(coordenada_string[0]) <= ord("Z"):
            continue
        coordenada=str_para_coordenada(coordenada_string)
        if eh_coordenada_do_campo(campo, coordenada):
            break
    return coordenada

def turno_jogador(campo):
    """Esta funcao oferece ao jogador a possibilidade de escolher uma ação e uma coordenada, modificando destrutivamente até se chegar ao jogo ganho/perdido.

    Args:
        campo (dicionario): campo

    Returns:
        booleano: Devolve False caso o jogador escolha uma parcela minada e True caso contrario
    """
    ação = ""
    while ação != "L" and ação != "M": #pedimos a acao
        ação=input("Escolha uma ação, [L]impar ou [M]arcar:")

    coordenada = input_coordenada(campo)
    p=obtem_parcela(campo, coordenada)

    if ação == "M": #especificacao de cada acao
        marca_parcela(p)
        return True
    
    if ação == "L": #especificacao de cada acao
        limpa_campo(campo, coordenada)
        if eh_parcela_minada(p):
            return False
        return True



def imprimir_campo(m, n):
    """Esta funcao auxiliar serve para imprimir o campo

    Args:
        m (dicionario): campo
        n (int): numero de minas
    """
    bandeiras=len(obtem_coordenadas(m, "marcadas")) #numero de bandeiras postas
    print(f"   [Bandeiras {bandeiras}/{n}]")
    print(campo_para_str(m))

def minas(col, linha, n, d, s):
    """Esta funcao permite jogar o jogo 

    Args:
        col (str):coluna
        linha (int): linha
        n (int): numero de minas
        d (int): bits
        s (int): seed

    Raises:
        ValueError: valores verificados em funcoes anteriores
        ValueError: o numero de minas tem que ser um numero inteiro positivo menor que o numero de parcelas do campo

    Returns:
        booleano: Devolve True caso o jogador ganhar o jogo e False caso contrario
    """
    try: 
        m = cria_campo(col, linha)
        g = cria_gerador(d, s)

    except ValueError: #value errors com except/try
        raise ValueError("minas: argumentos invalidos")
    if not isinstance(n, int) or not 0 < n < linha*(ord(col)-ord("A")-1):
        raise ValueError("minas: argumentos invalidos")
    imprimir_campo(m, n)

    coordenada=input_coordenada(m) #na primeira jogada apenas se pode limpar
    m = coloca_minas(m, coordenada, g, n) #so depois da primeira jogada e que se coloca minas
    limpa_campo(m, coordenada)
    imprimir_campo(m, n)
    while True:
        perdeu = not turno_jogador(m)
        imprimir_campo(m, n)
        if perdeu:
            print("BOOOOOOOM!!!")
            return False
        if jogo_ganho(m):
            print("VITORIA!!!")
            return True 
