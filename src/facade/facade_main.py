# encoding: utf-8

from walrus import *
from facade.aluno_facade import AlunoFacade
# from facade.historico_facade import HistoricoFacade
from facade.observador_facade import ObservadorFacade
from facade.estrutura_facade import EstruturaFacade
from facade.jogo_facade import OaConcluidoFacade
from facade.historico_facade import HistoricoFacade

class Facade(AlunoFacade, OaConcluidoFacade,ObservadorFacade, EstruturaFacade,HistoricoFacade):
    def __init__(self):
        super(Facade, self).__init__()
        # super(ObservadorFacade, self).__init__()
        ObservadorFacade.__init__(self)
        OaConcluidoFacade.__init__(self)
        EstruturaFacade.__init__(self)
        AlunoFacade.__init__(self)
        HistoricoFacade.__init__(self)

