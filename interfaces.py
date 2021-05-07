while True:
    hostname = input("Input Data Trunk Interface Baru  (Yes/No) : ")
    print("********************************************************")  

    if hostname == "no":
        file=open("db-interfaces.txt","r")
        for item in file:
            print(item)
        file.close()
        break

    if hostname == "yes":
        file=open("db-interfaces.txt","a")
        newhost = input("Masukan Hostname swicth : ")
        interface = input("Masukan nama Interface : ")
        print("---------------------------------------")
    file.write(newhost + "\n")
    file.write(interface + "\n")
file.close()