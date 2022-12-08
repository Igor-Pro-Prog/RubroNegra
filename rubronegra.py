#função remover da arvore rubro negra e a função rebalancear_remocao

def remover(self, chave):
    # se a arvore estiver vazia
    if self.raiz == None:
        return
    # se a arvore tiver apenas um elemento
    if self.raiz.esq == None and self.raiz.dir == None:
        if self.raiz.chave == chave:
            self.raiz = None
        return
    # se a arvore tiver mais de um elemento
    # busca o nó que contém a chave
    n = self.buscar(chave)
    if n == None:
        return
    # se o nó não tiver filhos
    if n.esq == None and n.dir == None:
        if n.pai.esq == n:
            n.pai.esq = None
        else:
            n.pai.dir = None
        if n.cor == 'preto':
            self.rebalancear_remocao(n.pai)
        return
    # se o nó tiver apenas um filho
    if n.esq == None or n.dir == None:
        if n.esq == None:
            filho = n.dir
        else: 
            filho = n.esq
        if n.pai.esq == n:
            n.pai.esq = filho
        else:
            n.pai.dir = filho
        filho.pai = n.pai
        if n.cor == 'preto':
            if filho.cor == 'vermelho':
                filho.cor = 'preto'
            else:
                self.rebalancear_remocao(filho)
        return
    # se o nó tiver dois filhos
    # busca o sucessor do nó
    s = n.dir
    while s.esq != None:
        s = s.esq
    # troca as chaves do nó e do sucessor
    n.chave, s.chave = s.chave, n.chave
    # remove o sucessor
    if s.dir != None:
        if s.pai.esq == s:
            s.pai.esq = s.dir
        else:
            s.pai.dir = s.dir
        s.dir.pai = s.pai
        if s.cor == 'preto':
            if s.dir.cor == 'vermelho':
                s.dir.cor = 'preto'
            else:
                self.rebalancear_remocao(s.dir)
    else:
        if s.pai.esq == s:
            s.pai.esq = None
        else:
            s.pai.dir = None
        if s.cor == 'preto':
            self.rebalancear_remocao(s.pai)

def rebalancear_remocao(self, n):
    # se o nó for a raiz
    if n == self.raiz:
        return
    # se o nó for vermelho
    if n.cor == 'vermelho':
        n.cor = 'preto'
        return
    # se o nó for preto e tiver um irmão vermelho
    if n.pai.esq == n:
        irmao = n.pai.dir
    else:
        irmao = n.pai.esq
    if irmao.cor == 'vermelho':
        irmao.cor = 'preto'
        n.pai.cor = 'vermelho'
        if n.pai.esq == n:
            self.rotacao_esquerda(n.pai)
        else:
            self.rotacao_direita(n.pai)
        self.rebalancear_remocao(n)
        return
    # se o nó for preto e tiver um irmão preto e ambos os filhos pretos
    if irmao.esq == None and irmao.dir == None:
        irmao.cor = 'vermelho'
        self.rebalancear_remocao(n.pai)
        return
    if irmao.esq != None and irmao.esq.cor == 'vermelho':
        if n.pai.esq == n:
            irmao.esq.cor = 'preto'
            irmao.cor = 'vermelho'
            self.rotacao_direita(irmao)
        else:
            irmao.esq.cor = n.pai.cor
            n.pai.cor = 'preto'
            irmao.cor = 'preto'
            self.rotacao_direita(n.pai)
        return
    if irmao.dir != None and irmao.dir.cor == 'vermelho':
        if n.pai.esq == n:
            irmao.dir.cor = n.pai.cor
            n.pai.cor = 'preto'
            irmao.cor = 'preto'
            self.rotacao_esquerda(n.pai)
        else:
            irmao.dir.cor = 'preto'
            irmao.cor = 'vermelho'
            self.rotacao_esquerda(irmao)
        return
    # se o nó for preto e tiver um irmão
    # preto e um filho vermelho
    if n.pai.esq == n:
        irmao.cor = 'vermelho'
        irmao.dir.cor = 'preto'
        self.rotacao_esquerda(irmao)
    else:
        irmao.cor = 'vermelho'
        irmao.esq.cor = 'preto'
        self.rotacao_direita(irmao)


