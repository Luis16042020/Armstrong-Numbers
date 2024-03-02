def is_armstrong_number(number):

   
    total_number_string = str(number)
    qtd_digits = len(total_number_string)


    soma = 0 

    for digito in total_number_string:
        digito_int = int(digito)

        soma += digito_int ** qtd_digits

        
    return number == soma
           
        
        

  
