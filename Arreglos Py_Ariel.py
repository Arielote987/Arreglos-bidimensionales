ventas = [[0.0 for _ in range(12)] for _ in range(3)]


departamentos = ["Ropa", "Deportes", "Juguetería"]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

print("--- GESTIÓN DE VENTAS ---")


dept = 2  
mes = 10   
venta_nueva = 987

ventas[dept][mes] = venta_nueva
print(f" Venta de ${venta_nueva} insertada para {departamentos[dept]} en {meses[mes]}.")


dept_buscar = 0
mes_buscar = 0
venta_buscada = ventas[dept_buscar][mes_buscar]
print(f" La venta de {departamentos[dept_buscar]} en {meses[mes_buscar]} es: ${venta_buscada}")


dept_eliminar = 1
mes_eliminar = 9

ventas[dept_eliminar][mes_eliminar] = 0.0
print(f" Venta de {departamentos[dept_eliminar]} en {meses[mes_eliminar]} eliminada.")


print(f" Verificando la venta eliminada: ${ventas[dept_eliminar][mes_eliminar]}")