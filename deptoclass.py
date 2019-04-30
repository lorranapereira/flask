class Departamento:
    def __init__(self, nome, gerente):
        self._nome = nome
        self._gerente = gerente
        self._id = id
    def _get_nome(self):
        return self._nome
    def _set_nome(self, nome):
        self._nome = nome
    def _get_id (self):
        return self._id
    def _set_id (self, id):
        self._id = id
    def _get_gerente(self):
        return self._gerente
    def _set_gerente(self, gerente):
        self._gerente = gerente
    def __str__(self):
        return "{},{},{}".format(self.nome,self.gerente,self.id)

    nome = property( _get_nome, _set_nome)
    gerente = property( _get_gerente, _set_gerente)
    id = property( _get_id, _set_id)
