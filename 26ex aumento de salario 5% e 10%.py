




#26. Faça um programa que leia o salário de um funcionário, calcule e mostre o novo salário,
#sabendo-se que este sofreu um aumento de 10% para quem recebe até R$ 3500,00 e 5%
#para quem recebe mais de R$ 3500,00

Idade = int(input("Quantos Voce recebe ? R$ "))

Idade10 = (Idade*10/100+Idade)
Idade5 = (Idade*5/100+Idade)

if (Idade <= 3500):
    print(f"\nSeu Idade + 10% = R$ {Idade10:,.0f} \n")
else:
    print(f"\nSeu Idade + 5% = R$ {Idade5:,.0f} \n")