file=open("table_multiplication","w+")
for i in range(1,10,1):
    file.write(f"le table de multiplication de {i} est: \n")
    for j in range(10):
        file.write(f"{i:>2} x {j+1} = {i*(j+1)}\n")
file.close()