from Bio import Entrez, SeqIO
import os, sys, pyperclip

Entrez.email = "lekeuffer@gmail.com"


def nucleotide_term(term0):
    print("Searching...\nThis might take a while.")
    handle = Entrez.esearch(db="nucleotide", term=term0)
    rec_list = Entrez.read(handle)
    handle.close()
    list_ids = rec_list['IdList']
    print("IDs collected...\n", list_ids)

    handle = Entrez.efetch(db="nucleotide", id=list_ids, rettype="gb")
    recs = list(SeqIO.parse(handle, 'gb'))
    print(recs)
    handle.close()

    for i in range(len(recs)):
        print(f"#{i + 1}#")
        print(f"ID              {recs[i].id}")
        print(f"NAME            {recs[i].name}")
        print(f"DESCRIPTION     {recs[i].description}")
        print("\n")

    errado = True
    while errado:
        esc = input("Digit the number/id of the record you want to see more info about.\nOr press '0' to return\n--> ").strip()
        if esc != '0':
            if len(esc) == 1 or len(esc) == 2:
                pyperclip.copy(recs[int(esc)-1].id)
                errado = False
            else:
                if esc in recs:
                    pyperclip.copy(recs)
                    errado = False
                else:
                    print("Please make sure the number/ID is correct")
            print(f"ID copied to your clipboard.")
        else:
            errado = False


def nucleotide_id_full(id0):
    handle = Entrez.efetch(db="nucleotide", id=id0, rettype="gb")
    rec = handle.read()
    aux = id0

    if '.1' in id0:
        aux = id0.replace('.1', '')
    if '.2' in id0:
        aux = id0.replace('.2', '')

    if "full_info" not in os.listdir(os.curdir):
        os.mkdir("full_info")
    with open(f"full_info/info_{aux}.txt", "w") as file:
        file.write(rec)
    print(f"All info found on {id0} has been saved.\nPath --> {os.getcwd()}\\full_info\\info_{aux}.txt")

    handle.close()


def nucleotide_id_seq(id0):
    handle = Entrez.efetch(db="nucleotide", id=id0, rettype="fasta", retmode="text")
    rec = SeqIO.read(handle, "fasta")
    print(rec)
    handle.close()
    aux = id0

    if '.1' in id0:
        aux = id0.replace('.1', '')

    if '.2' in id0:
        aux = id0.replace('.2', '')

    if "seq_info" not in os.listdir(os.curdir):
        os.mkdir("seq_info")

    with open(f"seq_info/seq_{aux}.fasta", "w") as file:
        file.write(f">{rec.description}")
        for l in range(len(rec.seq)):
            if l % 70 == 0:
                file.write("\n")
            file.write(str(rec.seq[l]))

    print(f"File created\nPath --> {os.getcwd()}\\seq_info\\seq_{aux}.fasta")  # BOTAR AS PARADAS DA AULA DO MP


if __name__ == "__main__":
    stay = True
    while stay:
        print("      NUCLEOTIDE DATABASE\n")
        print("[1] SEARCH 20 RECORDS THROUGH TERM")
        print("[2] SEARCH FULL INFO THROUGH ID")
        print("[3] GET FASTA FILE THROUGH ID")
        print("[0] LEAVE")
        esc = input("--> ").strip()
        match esc:
            case '1':
                term = input("Term: ").strip()
                nucleotide_term(term)
            case '2':
                idT = input("ID: ").strip()
                try:
                    nucleotide_id_full(idT)
                except:
                    print("Something went wrong.\nPlease make sure the ID is correct or try again later.")

            case '3':
                idT = input("ID: ").strip()
                try:
                    nucleotide_id_seq(idT)
                except:
                    print("Something went wrong.\nPlease make sure the ID is correct or try again later.")
            case '0':
                print("Thank you for using this program.\n")
                stay = False
            case other:
                print("Please, try again.")