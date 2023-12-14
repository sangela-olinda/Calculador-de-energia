print("//////Sua energia sera quanto esse mês?? //////") 

kwh= int(input("Qual valor que você usa de kWh? ")) 
tipo= input("Você a intalação R-Residencial, I-Industrial, C-Comercial? ") 

if tipo == "r": 
    if kwh<= 500: 
        #250 é a taxa que o cliente tem direito de graça  
        result= (kwh-250)* 0.40 
        print(f"Sua energia sera: R${result}") 

    elif kwh>=501 and kwh<=1499: 
        result= (kwh-250)*0.65 
        print(f"Sua energia sera: R${result}") 

    elif kwh>=1500: 
        result= (kwh-250)*0.70 
        #Multa de 2% de bandeira vermelha 
        multa=kwh*0.02 
        result1= result+multa 
        print(f"Sua energia sera R${result1:.2f} que tem R${multa:.2f} de multa por ter atingiado a bandeira vermelha.") 

if tipo == "i": 
    if kwh <= 5000: 
        #500 é a taxa que o cliente tem direito de graça  
        result= (kwh-500)*0.65 
        print(f"Sua energia sera: R${result}") 

    elif kwh>=5001 and kwh<=15000: 
        result= (kwh-500)*0.70 
        print(f"Sua energia sera: R${result}") 

    elif kwh>=15001: 
        result= (kwh-500)*0.70 
        #Multa de 10% da bandeira vermelha 
        multa=kwh*0.10 
        result1= result+multa 
        print(f"Sua energia sera R${result1:.2f} que tem R${multa:.2f} de multa por ter atingiado a bandeira vermelha.") 

if tipo == "c": 
    if kwh<=1000: 
        #400 é a taxa que o cliente tem direito de graça  
        result=(kwh-400)*0.55 
        print(f"Sua energia sera: R${result}") 

    elif kwh>=1001 and kwh<=9999: 
        result=(kwh-400)*0.60 
        print(f"Sua energia sera: R${result:.2f}") 

    elif kwh>=10000: 
        result= (kwh-400)*0.60 
        #Multa de 5% da bandeira vermelha 
        multa=kwh*0.05 
        result1= result+multa 
        print(f"Sua energia sera R${result1:.2f} que tem R${multa:.2f} de multa por ter atingiado a bandeira vermelha.") 
