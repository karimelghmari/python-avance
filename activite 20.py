adresse_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
adresse_ip1={"192.168.0.2":"classe C","10.0.0.1":"classe A","172.16.0.1":"classe B","200.100.50.1":"adresse IP publique","169.254.0.1":"adresse IP de lien local"}
#1
print(f"la premiere adresse est:{adresse_ip[0]}")
#2
print(f"la derniere adresse est:{adresse_ip[len(adresse_ip)-1]}")
#3
print(f"le troisieme element est: {adresse_ip[2]}")
#4
adresse_ip.append("172.31.0.1")
#5
adresse_ip.remove("200.100.50.1")
#6
print(f"il reste {len(adresse_ip)} elements")
#7
print("192.168.0.1" in adresse_ip)
#8
print(f"la classe de l'adresse 10.0.0.1 est {adresse_ip1['10.0.0.1']}")
#9
adresse_ip.sort(key=lambda x: [int(part) for part in x.split('.')])
print(adresse_ip)
#10
if all(x=="192.168.0.2" for x in adresse_ip):
    print("toutes kes adresses sont de classe C")
else:
    print("il y a des adresses qui ne sont pas de classe C")
#11
s=0
for i in adresse_ip:
    if i=="200.100.50.1":
        s+=1
print(f"il y a {s} adresse(s) IP publique(s)")