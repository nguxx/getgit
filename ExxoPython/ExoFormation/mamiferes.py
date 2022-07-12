embranchement = "vertébrés"
classe = "mammifères"
ordre = "carnivores"
famille = "félins"
if embranchement == "vertébrés":            # 1
    if classe == "mammifères":              # 2
        if ordre == "carnivores":           # 3
            if famille == "félins":          # 4
                print("c'est peut-être un chat")      # 5
        print("c'est en tous cas un mammifère")      # 6
    elif classe == "oiseaux":              # 7
        print("c'est peut-être un canari")      # 8
print("la classification des animaux est complexe")  # 9

