class Pessoa:
    def __init__(self, name, id, tel, email,uff, status):
        self.nome = name
        self.matricula = id
        self.telefone = tel
        self.email = email
        self.uffMail = uff
        self.status = status

    def __str__(self):
        return ("Nome: "+self.nome+"\n"+"Matrícula: "+str(self.matricula)+"\n"+"Telefone: "+str(self.telefone)+
        "\n"+"Email: "+self.email+"\n"+"Uff Mail: "+self.uffMail+"\n"+"Status: "+str(self.status)+"\n")

    def getNome(self):
        return self.nome

    def getMatricula(self):
        return self.matricula

    def getTelefone(self):
        return self.telefone

    def getEmail(self):
        return self.email
    def getUffEmail(self):
        return self.uffMail

    def getStatus(self):
        return self.status

    def setUffEmail(self, email):
        self.email = email

