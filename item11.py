def imprimindo(*args, **keywords):
    print("ola, aqui esta sua lista impressa: \n")
    for arg in args:
        print("-> {0}".format(arg))

    print("\ne aqui esta seu dicionario: \n")
    keys = sorted(keywords.keys())
    for k in keys:
        print("-> {0} : {1}".format(k, keywords[k]))

imprimindo("um", "dois", "tres", "quatro",
           numero = 'quatro',
           forma = 'escrito',
           proposito = 'demonstracao')
