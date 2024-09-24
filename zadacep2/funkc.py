pozdrav = lambda ime: print("Pozdrav " + ime + "!")

def dobrodosao(naziv):
    print("Dobrodosao " + naziv + "!")

def treca(naziv):
    dobrodosao(naziv)

pozdrav("Galic")
dobrodosao("Galic")
treca("Galic")