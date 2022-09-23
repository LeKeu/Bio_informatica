from Bio import SeqIO
from Bio.Seq import Seq
import os


def caseAll(arq, nome, index):
    titulo = ["SEQUENCIA COMPLEMENTAR", "SEQUENCIA REVERSA COMPLEMENTAR", "TRANSCRICAO", "TRANSCRICAO DE VOLTA"]
    arquivo_nome = ["seq_compl", "seq_rev_compl", "seq_transcri", "seq_transcri_volta"]


    print(titulo[index])
    if arquivo_nome[index] not in os.listdir(os.curdir):
        os.mkdir(arquivo_nome[index])

    with open(f"{arquivo_nome[index]}/{arquivo_nome[index]}_{nome}", "w") as file:
        for i in arq:
            funcs = [arq[i].complement, arq[i].reverse_complement, arq[i].transcribe, arq[i].back_transcribe]

            file.write(f">{i}")
            aux = str(funcs[index]())

            for l in range(len(aux)):
                if l % 70 == 0:
                    file.write("\n")
                file.write(aux[l])
    print(f"Arquivo salvo.\nPath --> {os.getcwd()}\\{arquivo_nome[index]}\\{arquivo_nome[index]}_{nome}")
    input("\n\nPressione qualquer tecla para continuar\n-")

def usuario(arquivo, nome_arq):
    nome = nome_arq
    aux = True
    while aux:
        os.system('cls' if os.name == "nt" else 'clear')
        print(f'''
        OBS: Todas as opções salvam o arquivo numa pasta diferente para melhor organização
    Voce gostaria da:
        [1] Sequencia Complementar
        [2] Sequencia Reversa Complementar
        [3] Processo de Transcrição
        [4] Processo de Transcrição de volta
        [0] Sair''')
        esc = input("--> ").strip()
        os.system('cls' if os.name == "nt" else 'clear')

        match esc:
            case '1' | '2' | '3' | '4':
                caseAll(arquivo, nome, int(esc)-1)
            case '0':
                print("Saindo...")
                aux = False
            case other:
                print("Erro. Tente novamente")
                input("\n\nPressione qualquer tecla para continuar\n-")



if __name__ == "__main__":
    dic = {}
    print("Obs: importante que o arquivo esteja contido no mesmo diretório que o código")
    arq = input("Nome do arquivo: ").strip()
    if ".fasta" not in arq:
        arq += ".fasta"

    try:
        for f in SeqIO.parse(arq, "fasta"):
            dic[f.id] = f.seq
    except FileNotFoundError:
        print("Arquivo não encontrado")
    else:
        usuario(dic, arq)