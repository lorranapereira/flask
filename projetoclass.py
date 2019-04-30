class Projeto:
    def __init__(self, nome, id, dataPrevista):
        self._nome = nome
        self._id = id
        self._dataPrevista = dataPrevista

    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_id (self):
        return self._id
    def _set_id (self, id):
        self._id = id
    def _get_dataPrevista(self):
        return self._dataPrevista
    def _set_dataPrevista(self, dataPrevista):
        self._dataPrevista = dataPrevista
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.nome,self.dataPrevista,self.id)

    nome = property( _get_nome, _set_nome)
    dataPrevista = property( _get_dataPrevista, _set_dataPrevista)
    id = property( _get_id, _set_id)
