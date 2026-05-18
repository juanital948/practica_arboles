# Sistema de Inventario de Farmacia usando Árbol Binario de Búsqueda (BST)

## Descripción

El proyecto consiste en desarrollar un sistema para gestionar el inventario de una cadena de farmacias utilizando un Árbol Binario de Búsqueda (BST).

Cada nodo del árbol representa un medicamento y contiene la siguiente información:

- ID
- Nombre
- Stock
- Año de vencimiento
- Precio

El ID funciona como llave principal del árbol.

---

# Funcionalidades del Sistema

## Registro de medicamentos

Permite insertar nuevos medicamentos en el árbol respetando las reglas del BST:

- IDs menores → izquierda
- IDs mayores → derecha

Si el ID ingresado es par, el sistema aplica automáticamente un descuento del 10% al precio.

---

## Búsqueda y venta

Permite buscar un medicamento por su ID y reducir unidades del stock.

Si el medicamento queda sin stock, el sistema sugiere automáticamente un sustituto.

---

## Eliminación de medicamentos

Permite eliminar medicamentos del árbol manteniendo la estructura correcta del BST.

---

## Control de estado

El sistema mantiene actualizado:

- Cantidad de medicamentos con stock menor a 5.
- Valor total del inventario.

---

## Limpieza de medicamentos vencidos

El usuario ingresa el año actual y el sistema elimina automáticamente todos los medicamentos vencidos.

---

## Visualización inversa

Muestra todos los medicamentos ordenados de mayor ID a menor ID.

---

## Consulta por rango

Permite mostrar medicamentos cuyos IDs se encuentren dentro de un intervalo ingresado por el usuario.

---

## Sugerencia automática de sustitutos

Cuando un medicamento tiene stock en cero, el sistema busca:

- Sucesor In-Order
- Predecesor In-Order

para sugerir un reemplazo.

---

## Fusión de inventario

Permite transferir el stock de un medicamento origen hacia un medicamento destino.

Después de la transferencia:

- El nodo origen se elimina.
- Se incrementa el contador global de fusiones.

---

# Restricciones

El sistema fue desarrollado utilizando únicamente:

- Árbol Binario de Búsqueda (BST)
- Cola auxiliar entregada en clase

No se utilizaron:

- Listas
- Diccionarios
- Arreglos

Toda la lógica del sistema se realiza directamente sobre el árbol.
