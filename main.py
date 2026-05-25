from clases_arboles_farmacia import *

TOTAL_OPERACIONES_FUSION = 0


class Medicamento:

  def __init__(self, id_medicamento, nombre, stock, vencimiento, precio):
    self.id_medicamento = id_medicamento
    self.nombre = nombre
    self.stock = stock
    self.vencimiento = vencimiento
    self.precio = precio

  def __str__(self):
    return (
      "ID: " + str(self.id_medicamento)
      + " | Nombre: " + self.nombre
      + " | Stock: " + str(self.stock)
      + " | Vence: " + str(self.vencimiento)
      + " | Precio: " + str(self.precio)
    )


class InventarioFarmacia:

  def __init__(self):
    self.raiz = None
    self.alertas_stock = 0
    self.valor_total = 0


  def esta_en_alerta(self, medicamento):
    if medicamento.stock < 5:
      return True
    return False


  def valor_producto(self, medicamento):
    return medicamento.stock * medicamento.precio


  def sumar_estado(self, medicamento):
    if self.esta_en_alerta(medicamento):
      self.alertas_stock += 1

    self.valor_total += self.valor_producto(medicamento)


  def restar_estado(self, medicamento):
    if self.esta_en_alerta(medicamento):
      self.alertas_stock -= 1

    self.valor_total -= self.valor_producto(medicamento)


  def registrar_medicamento(self, id_medicamento, nombre, stock, vencimiento, precio):

    if id_medicamento % 2 == 0:
      precio = precio * 0.90
      print("Se aplico descuento del 10%.")

    medicamento = Medicamento(id_medicamento,nombre,stock,vencimiento,precio)

    nuevo_nodo = BinaryTreeNode(medicamento)

    if self.raiz is None:
      self.raiz = nuevo_nodo
      self.sumar_estado(medicamento)
      print("Medicamento registrado.")
      return

    actual = self.raiz

    while actual is not None:

      if id_medicamento == actual.data.id_medicamento:
        print("Ese ID ya existe.")
        return

      elif id_medicamento < actual.data.id_medicamento:

        if actual.leftchild is None:
          actual.leftchild = nuevo_nodo
          self.sumar_estado(medicamento)
          print("Medicamento registrado.")
          return

        actual = actual.leftchild

      else:

        if actual.rightchild is None:
          actual.rightchild = nuevo_nodo
          self.sumar_estado(medicamento)
          print("Medicamento registrado.")
          return

        actual = actual.rightchild


  def buscar(self, id_medicamento):

    actual = self.raiz

    while actual is not None:

      if id_medicamento == actual.data.id_medicamento:
        return actual

      elif id_medicamento < actual.data.id_medicamento:
        actual = actual.leftchild

      else:
        actual = actual.rightchild

    return None


  def vender_medicamento(self, id_medicamento, cantidad):

    nodo = self.buscar(id_medicamento)

    if nodo is None:
      print("Medicamento no encontrado.")
      return

    if cantidad <= 0:
      print("La cantidad debe ser mayor a cero.")
      return

    if nodo.data.stock == 0:
      print("No hay stock.")
      self.sugerir_sustituto(id_medicamento)
      return

    if cantidad > nodo.data.stock:
      print("Stock insuficiente.")
      return

    antes = self.esta_en_alerta(nodo.data)

    nodo.data.stock -= cantidad
    self.valor_total -= cantidad * nodo.data.precio

    despues = self.esta_en_alerta(nodo.data)

    if antes == False and despues == True:
      self.alertas_stock += 1

    print("Venta realizada.")
    print(nodo.data)

    if nodo.data.stock == 0:
      self.sugerir_sustituto(id_medicamento)


  def minimo(self, nodo):

    actual = nodo

    while actual.leftchild is not None:
      actual = actual.leftchild

    return actual


  def eliminar_por_id(self, id_medicamento):

    self.raiz = self.eliminar_recursivo(self.raiz,id_medicamento,True)

  def eliminar_recursivo(self, nodo, id_medicamento, cambiar_estado):

    if nodo is None:
      return None

    if id_medicamento < nodo.data.id_medicamento:

      nodo.leftchild = self.eliminar_recursivo(nodo.leftchild,id_medicamento,cambiar_estado)

    elif id_medicamento > nodo.data.id_medicamento:

      nodo.rightchild = self.eliminar_recursivo(nodo.rightchild,id_medicamento,cambiar_estado)

    else:

      if cambiar_estado:
        self.restar_estado(nodo.data)

      if nodo.leftchild is None:
        return nodo.rightchild

      elif nodo.rightchild is None:
        return nodo.leftchild

      reemplazo = self.minimo(nodo.rightchild)

      nodo.data = reemplazo.data

      nodo.rightchild = self.eliminar_recursivo(nodo.rightchild,reemplazo.data.id_medicamento,False)

    return nodo


  def limpiar_caducados(self, anio_actual):

    self.limpiar_recursivo(self.raiz,anio_actual)


  def limpiar_recursivo(self, nodo, anio_actual):

    if nodo is None:
      return

    self.limpiar_recursivo(nodo.leftchild,anio_actual)

    self.limpiar_recursivo(nodo.rightchild,anio_actual)

    if nodo.data.vencimiento <= anio_actual:
      self.eliminar_por_id(nodo.data.id_medicamento)


  def mostrar_inverso(self):

    if self.raiz is None:
      print("Inventario vacio.")
      return

    self.inverso_recursivo(self.raiz)


  def inverso_recursivo(self, nodo):

    if nodo is None:
      return

    self.inverso_recursivo(nodo.rightchild)

    print(nodo.data)

    self.inverso_recursivo(nodo.leftchild)


  def consultar_rango(self, minimo, maximo):

    if minimo > maximo:
      auxiliar = minimo
      minimo = maximo
      maximo = auxiliar

    self.rango_recursivo(self.raiz,minimo,maximo)


  def rango_recursivo(self, nodo, minimo, maximo):

    if nodo is None:
      return

    if nodo.data.id_medicamento > minimo:
      self.rango_recursivo(nodo.leftchild,minimo,maximo)

    if minimo <= nodo.data.id_medicamento <= maximo:
      print(nodo.data)

    if nodo.data.id_medicamento < maximo:
      self.rango_recursivo(nodo.rightchild,minimo,maximo)


  def buscar_sucesor(self, id_medicamento):

    actual = self.raiz
    sucesor = None

    while actual is not None:

      if id_medicamento < actual.data.id_medicamento:
        sucesor = actual
        actual = actual.leftchild

      else:
        actual = actual.rightchild

    return sucesor


  def buscar_predecesor(self, id_medicamento):

    actual = self.raiz
    predecesor = None

    while actual is not None:

      if id_medicamento > actual.data.id_medicamento:
        predecesor = actual
        actual = actual.rightchild

      else:
        actual = actual.leftchild

    return predecesor


  def sugerir_sustituto(self, id_medicamento):

    sucesor = self.buscar_sucesor(id_medicamento)

    if sucesor is not None:
      print("Sustituto sugerido:")
      print(sucesor.data)
      return

    predecesor = self.buscar_predecesor(id_medicamento)

    if predecesor is not None:
      print("Sustituto sugerido:")
      print(predecesor.data)
      return

    print("No hay sustituto disponible.")


  def fusionar(self, id_origen, id_destino):

    global TOTAL_OPERACIONES_FUSION

    if id_origen == id_destino:
      print("No se puede fusionar el mismo medicamento.")
      return

    origen = self.buscar(id_origen)
    destino = self.buscar(id_destino)

    if origen is None or destino is None:
      print("IDs invalidos.")
      return

    destino_antes = self.esta_en_alerta(destino.data)

    destino.data.stock += origen.data.stock

    destino_despues = self.esta_en_alerta(destino.data)

    if destino_antes == True and destino_despues == False:
      self.alertas_stock -= 1

    self.valor_total += origen.data.stock * destino.data.precio

    self.eliminar_por_id(id_origen)

    TOTAL_OPERACIONES_FUSION += 1

    print("Fusion realizada correctamente.")


  def estado_global(self):

    print("Medicamentos con stock menor a 5:", self.alertas_stock)
    print("Valor total del inventario:", self.valor_total)
    print("Total operaciones de fusion:", TOTAL_OPERACIONES_FUSION)


def menu():

  inventario = InventarioFarmacia()

  while True:

    print("")
    print("====== INVENTARIO FARMACIA ======")
    print("1. Registrar medicamento")
    print("2. Vender medicamento")
    print("3. Eliminar por ID")
    print("4. Limpieza por caducidad")
    print("5. Estado global")
    print("6. Mostrar inventario de mayor a menor")
    print("7. Consultar rango")
    print("8. Fusionar inventario")
    print("0. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":

      id_medicamento = int(input("ID: "))
      nombre = input("Nombre: ")
      stock = int(input("Stock: "))
      vencimiento = int(input("Año vencimiento: "))
      precio = float(input("Precio: "))

      inventario.registrar_medicamento(id_medicamento,nombre,stock,vencimiento,precio)

    elif opcion == "2":

      id_medicamento = int(input("ID medicamento: "))
      cantidad = int(input("Cantidad: "))

      inventario.vender_medicamento(id_medicamento,cantidad)

    elif opcion == "3":

      id_medicamento = int(input("ID eliminar: "))

      inventario.eliminar_por_id(id_medicamento)

    elif opcion == "4":

      anio = int(input("Año actual: "))

      inventario.limpiar_caducados(anio)

    elif opcion == "5":

      inventario.estado_global()

    elif opcion == "6":

      inventario.mostrar_inverso()

    elif opcion == "7":

      minimo = int(input("ID minimo: "))
      maximo = int(input("ID maximo: "))

      inventario.consultar_rango(minimo,maximo)

    elif opcion == "8":

      origen = int(input("ID origen: "))
      destino = int(input("ID destino: "))

      inventario.fusionar(origen,destino)

    elif opcion == "0":

      print("Programa finalizado.")
      break

    else:
      print("Opcion invalida.")


menu()