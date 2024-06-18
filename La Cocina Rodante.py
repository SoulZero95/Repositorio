
# Inicialización de Variables
subtotal=0
tipo_desc=0
desc=0
total_pagar=0
desc_estudiante = 0.12
desc_docente = 0.10
valor_churrasco = 4500
valor_chacarero = 5500
valor_barrosluco = 6000

#Inicialización de Contadores
cont_barrosluco=0
cont_chacarero=0
cont_churrasco=0

#Inicialización de Acumuladores
total_barrosluco=0
total__chacarero=0
total_churrasco=0

#PROGRAMA PRINCIPAL
flag=0
while True:  
  try:
    pedido=int(input("Desea realizar un pedido de Sándwiches \n1) Confirmar \n2) Cancelar\n==> "))
    if (pedido == 1) or (pedido == 2):
      break
    else: 
      print("Dato ingresado erroneo \nIntente nuevamente\n ")
  except:
      print("Dato ingresado erroneo \nIngrese nuevamente\n ")


if (pedido == 1):
  while True:
    bandera=0
    print("\n!LA COCINA RODANTE¡")
    print("**********************")
    print("1) Sándwich Churrasco:    $4.500 ")
    print("2) Sándwich Chacarero:    $5.500 ")
    print("3) Sándwich Barros Luco:  $6.000 ")
    print("4) Cancelar ")
    
    while (bandera == 0):
      try:
        tipo=int(input("\nSelecciona el Sándwich que desea comprar \n==>"))
        if (tipo <= 0) or (tipo >= 5):
          print("Dato ingresado erroneo \nIntente nuevamente\n ")
        else: 
          bandera = 1
      except:
          print("Dato ingresado erroneo \nIngrese nuevamente\n ")

    if tipo==1:
      print("Usted ha elegido Sándwich Churrasco")
      cantidad=int(input("Ingrese la cantidad que desea comprar \n==>"))
      cont_churrasco = cont_churrasco + cantidad     #Contador Churrasco
      total_churrasco = cont_churrasco * valor_churrasco   #Acumulador Churrasco
      j=0
      while j==0:
        try:
          continuar=int(input("Desea ordenar algo más? \n1)Si \n2)No \n"))
          if continuar==1:
            j=1
          elif continuar==2:
            j=1
          else: 
            print("Dato ingresado erroneo \nIntente nuevamente\n ")
        except:
            print("Dato ingresado erroneo \nIngrese nuevamente\n ")
  

    elif (tipo == 2):
      print("Usted ha elegido Sándwich Chacarero")
      cantidad=int(input("Ingrese la cantidad que desea comprar \n==>"))
      cont_chacarero = cont_chacarero + cantidad
      total__chacarero = cont_chacarero * valor_chacarero
      j=0
      while j==0:
        try:
          continuar=int(input("Desea ordenar algo más? \n1)Si \n2)No \n"))
          if continuar==1:
            j=1
          elif continuar==2:
            j=1
          else: 
            print("Dato ingresado erroneo \nIntente nuevamente\n ")
        except:
            print("Dato ingresado erroneo \nIngrese nuevamente\n ")

    elif (tipo == 3):
      print("Usted ha elegido Sándwich Barros Luco")
      cantidad=int(input("Ingrese la cantidad que desea comprar \n==>"))
      cont_barrosluco = cont_barrosluco + cantidad
      total_barrosluco = cont_barrosluco * valor_barrosluco
      j=0
      while j==0:
        try:
          continuar=int(input("Desea ordenar algo más? \n1)Si \n2)No \n"))
          if continuar==1:
            j=1
          elif continuar==2:
            j=1
          else: 
            print("Dato ingresado erroneo \nIntente nuevamente\n ")
        except:
            print("Dato ingresado erroneo \nIngrese nuevamente\n ")

    else:
      print("Se cancelo exitosamente")

    if continuar==2:
     break


  while flag==0:
    try:
      tipo_desc=int(input("\nIngrese descuento \n1) Estudiante \n2) Docentes \n3) Directivos \n"))
      if (tipo_desc==1) or (tipo_desc==2) or (tipo_desc==3):
        flag=1
    except:
      print("Información de Descuento mal ingresado ")
    else:
      flag=1
  
  #Imprimir la Información de salida
  print(f"\nLA COCINA RODANTE")
  print("**********************")
  if cont_churrasco >= 1:
    print(f"* {cont_churrasco}  Churrasco   ${total_churrasco}")
  if cont_chacarero >= 1:
    print(f"* {cont_chacarero}  Chacarero   ${total__chacarero}")
  if cont_barrosluco >= 1:
    print(f"* {cont_barrosluco} BarrasLuco  ${total_barrosluco}")
  
  #Obtención del Subtotal de la compra.
  subtotal = total_churrasco + total__chacarero + total_barrosluco
  
  #Aplicar descuento si procede a estudiantes o docentes
  if tipo_desc == 1:
    desc = subtotal * desc_estudiante
  elif tipo_desc == 2:
    desc=subtotal * desc_docente

  #Obtención del Total a pagar
  total_pagar = subtotal - desc

  print("-----------------------------------------------")   
  print(f"Subtotal        ${subtotal}")
  print(f"Descuento       ${desc}")
  print("-----------------------------------------------")
  print(f"Total a pagar   ${total_pagar}")   
  
  print("Gracias por su compra, vuelva pronto.")
else:
  print("Se cancelo el pedido, vuelva pronto")

