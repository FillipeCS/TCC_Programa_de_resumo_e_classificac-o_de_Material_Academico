import Process
import os
import requests
from bs4 import BeautifulSoup
from multipledispatch import dispatch
from goose3 import Goose


g = Goose()
p = Process.Process

@dispatch(str)
def save_text(sub):
    v = True
    while v:
        print("Passe o link\n[sair](0)")
        url = input("")
        if url == '0':
            os.system('cls')
            v = False
        else:
            try:
                os.system('cls')
                text = g.extract(url).cleaned_text
                reqs = requests.get(url)
                soup = BeautifulSoup(reqs.text, 'html.parser')
                title = ""
                for t in soup.find_all('title'):
                    title = title + t.get_text()
                p.to_add_data(sub ,title ,text)
                v = False
            except Exception as e:
                os.system('cls')
                print(e)
                print("\n|não é um link valido, tente novamente|\n")
                v = False

            input("precione (ENTER) para continuar")
            os.system('cls')
            v = False

@dispatch(str, str, str)
def save_text(sub, tt, txt):
    p.to_add_data(sub ,tt ,txt)
    input("precione (ENTER) para continuar")
    os.system('cls')

def manual():
    v = True
    while v:
        print("""\nEscolha
    [escolher a matéria](1)
    [escrever nome da matéria](2)
    [sair](0)
""")
        try:
            opt = int(input(""))
            if opt == 0:
                v = False
            elif opt == 1:
                os.system('cls')
                i = True
                classes = p.see_file()
                while i:
                    if classes == []:
                        input("Não há matérias disponíveis\nAperte (ENTER) para continuar")
                        v = False
                        i = False
                        os.system('cls')
                    else:
                        print("\n\nEscolha uma matéria")
                        for l in range(len(classes)):
                            print("[" + str(classes[l]) + "](" + str(l + 1) + ")\n")
                        try:
                            opt = int(input("[sair](0)"))
                            if opt == 0:
                                os.system('cls')
                                v = False
                                i = False
                            elif (opt <= len(classes)) & (opt >= 0) :
                                save_text(classes[opt - 1])
                                os.system('cls')
                                v = False
                                i = False
                            else:
                                os.system('cls')
                                print("|Opção invalida|")
                        except:
                            os.system('cls')
                            print("|Opção invalida|")


            elif opt == 2:
                sub = input("""Escreva o nome da materia
                |lembre-se, o nome escolhido ficará arquivado e usado em funções futuras|
                [sair](0)
        """)
                if sub != '0':
                    os.system('cls')
                    save_text(sub)
                v = False
            else:
                os.system('cls')
                print("|Opção invalida|")
        except:
            os.system('cls')
            print("|Opção invalida|")


def auto():
    v = True
    while v:
        u = True
        while u:
            print("Passe o link\n[sair](0)")
            url = input("")
            if url == '0':
                os.system('cls')
                u = False
                v = False
            else:
                try:
                    os.system('cls')
                    text = g.extract(url).cleaned_text
                    reqs = requests.get(url)
                    soup = BeautifulSoup(reqs.text, 'html.parser')
                    title = ""
                    resum = p.classfy(text)
                    for t in soup.find_all('title'):
                        title = title + t.get_text()
                    if resum == None:
                        opt = input("não há informação insuficiente\nAperte (ENTER) para continuar")
                        v = False
                        u = False
                    else:
                        r = True
                        while v:
                            print("Previsão " + resum[0] + "\nDeseja adicionar a matéria " + resum[0] +"?(ENTER)\n")
                            opt = input("[sair](0)")
                            if opt == '0':
                                os.system('cls')
                                v = False
                                r = False
                                u = False

                            else:
                                os.system('cls')
                                save_text(resum[0], title, text)
                                v = False
                                r = False
                                u = False
                    u = False
                except Exception as e:
                    os.system('cls')
                    print(e)
                    print("\n|não é um link valido, tente novamente|\n")


def to_add_text():
    v = True
    while v:
        print("""deseja:
        [processo manual](1)
        [ver classificação](2)
        [sair](0)
    """)
        try:
            opt = int(input(""))
        except:
            os.system('cls')
            print("|Opção invalida|")
        if opt == 0:
            os.system('cls')
            v = False
        elif opt == 1:
            os.system('cls')
            manual()
            v = False
        elif opt == 2:
            os.system('cls')
            auto()
            v = False
        else:
            os.system('cls')
            print("|Opção invalida|")

def to_del_text():
    v = True
    classes = p.see_file()
    while v:
        if classes == []:
            input("Não há matérias disponíveis\nAperte (ENTER) para continuar")
            v = False
            os.system('cls')
        else:
            print("\n\nEscolha uma matéria")
            for l in range(len(classes)):
                print("[" + str(classes[l]) + "](" + str(l + 1) + ")\n")
            try:
                opt = int(input("[sair](0)"))
            except:
                os.system('cls')
                print("|Opção invalida|")
            if opt == 0:
                os.system('cls')
                v = False
            elif opt <= len(classes):
                i = True
                while i:
                    data = p.get_text(classes[opt - 1])
                    cls = classes[opt - 1]
                    if data == []:
                        input("Não há textos disponíveis\nAperte (ENTER) para continuar")
                        v = False
                        i = False
                        os.system('cls')
                    else:
                        data.sort()
                        print("\n\nEscolha um texto")
                        for l in range(len(data)):
                            print("[" + str(data[l][0]) + "](" + str(l + 1) + ")\n")
                        try:
                            opt = int(input("[sair](0)"))
                        except:
                            os.system('cls')
                            print("|Opção invalida|")
                        if opt == 0:
                            os.system('cls')
                            v = False
                            i = False
                        elif opt <= len(data):
                            p.to_delete_data([cls, data[opt - 1]])
                            input("\nAperte (ENTER) para continuar")
                            v = False
                            i = False

def to_read_text():
    v = True
    classes = p.see_file()
    while v:
        if classes == []:
            input("Não há matérias disponíveis\nAperte (ENTER) para continuar")
            v = False
            os.system('cls')
        else:
            print("\n\nEscolha uma matéria")
            for l in range(len(classes)):
                print("[" + str(classes[l]) + "](" + str(l + 1) + ")\n")
            try:
                opt = int(input("[sair](0)"))
            except:
                os.system('cls')
                print("|Opção invalida|")
            if opt == 0:
                os.system('cls')
                v = False
            elif opt <= len(classes):
                i = True
                while i:
                    data = p.get_text(classes[opt - 1])
                    cls = classes[opt - 1]
                    if data == []:
                        input("Não há textos disponíveis\nAperte (ENTER) para continuar")
                        v = False
                        i = False
                        os.system('cls')
                    else:
                        data.sort()
                        print("\n\nEscolha um texto")
                        for l in range(len(data)):
                            print("[" + str(data[l][0]) + "](" + str(l + 1) + ")\n")
                        try:
                            opt = int(input("[sair](0)"))
                        except:
                            os.system('cls')
                            print("|Opção invalida|")
                        if opt == 0:
                            os.system('cls')
                            v = False
                            i = False
                        elif opt <= len(data):
                            resum = p.summary(cls, data[opt - 1][1])
                            #os.system('cls')
                            print("""\n\n----------------------------------------\n"""
        + str(resum) +
        """\n----------------------------------------\n""")
                            input("\nAperte (ENTER) para continuar")
                            v = False
                            i = False
                            os.system('cls')


v = True
opt = None
while v:
    os.system('cls')
    print("""\nPROGRAMA DE RESUMO E CLASSIFICAÇÃO DE MATERIAL ACADÊMICO\n\n
escolha:\n
    [Adicionar texto](1)
    [Deletar texto](2)
    [Ler resumo](3)
    [sair](0)
""")
    try:
        opt = int(input(""))
    except:
        os.system('cls')
        print("|Opção invalida|")
    if opt == 0:
        v = False
    elif opt == 1:
        os.system('cls')
        to_add_text()
    elif opt == 2:
        os.system('cls')
        to_del_text()
    elif opt == 3:
        os.system('cls')
        to_read_text()

    else:
        os.system('cls')
        print("|Opção invalida|")
