from pessoa import Pessoa
import csv

def primeiroNome(nome):
    aux = nome.split(" ")
    return aux[0]

def nomesAleatorios(nome):
    aux = nome.split(" ")
    letras = []
    for i in range(len(aux)):
        primeiraLetra = list(aux[i])
        letras.append(primeiraLetra[0])
    uff = "@id.uff.br"
    nome1 = aux[0]+"_"+aux[1]+uff
    nome2 = aux[0]+letras[1]+letras[len(aux)-1]+uff
    nome3 = aux[0]+aux[len(aux)-1]+uff
    nome4 = letras[0]+aux[len(aux)-1]+uff
    nome5 = letras[0]+aux[1]+aux[len(aux)-1]+uff
    listaDeEmails = [nome1.lower(), nome2.lower(), nome3.lower(), nome4.lower(), nome5.lower()]
    return  listaDeEmails



alunos =[]
with open('alunos.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        alunos.append(
            Pessoa(row['nome'], row['matricula'], row['telefone'], row['email'], row['uffmail'], row['status']))

matricula =input("Digite sua matrícula: \n")
emailEscolhido = " "
alunoSelecionado = None
for aluno in alunos:
    if aluno.matricula==matricula:
        alunoSelecionado = aluno
        if aluno.status == "Ativo":
            print(primeiroNome(aluno.nome)+", por favor escolha uma das opções abaixo para o seu UFFMail")
            listaDeEmails= nomesAleatorios(aluno.nome)
            for i in range(5):
                print(str(i+1)+" - "+listaDeEmails[i]+"\n")

            valorEscolhido = input()
            emailEscolhido = listaDeEmails[int(valorEscolhido)-1]
            print("A criação de seu e-mail (" + emailEscolhido + ") será feita nos próximos minutos. Um SMS foi enviado para "+str(alunoSelecionado.telefone)+" com a sua senha de acesso.")
            aluno.uffMail = emailEscolhido
        else:

            print("Aluno inativo!")

        break


if emailEscolhido == None:
    print("Matrícula não encontrada.")

with open('alunos.csv', 'w', newline='') as csvfile:
    fieldnames = ['nome', 'matricula', 'telefone', 'email', 'uffmail', 'status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for aluno in alunos:
        writer.writerow({'nome': aluno.nome, 'matricula': aluno.matricula, 'telefone': aluno.telefone,
                         'email': aluno.email, 'uffmail': aluno.uffMail, 'status': aluno.status })
