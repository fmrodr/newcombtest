# Desafio Back-end - New Combin

En el archivo requirements.txt estan todos los modulos usados

- Los 3 primeros requisitos estan completados al 100%, el 4to requisito no esta completo al 100%
- Para acceder a la API las urls del dev server son las siguientes: 
1. API Root: http://127.0.0.1:8000/ 
2. Payable - Lista de Todas las Payables: http://127.0.0.1:8000/payables/ (desde ahi se puede hacer el POST para agregar mediante el formulario o mediante raw data) 
3. Para obtener la info se realiza mediante la solicitud GET http://127.0.0.1:8000/payables/000001/ (Donde 000002 representa un codigo de barras)
4. Payables que no han sido pagados con los siguientes atributos de la solicitud GET: http://127.0.0.1:8000/payables/?not_paid=true (Donde not_paid es la variable que solo activa el filtrado si es true)
5. Payables según tipo con los siguientes atributos de la solicitud GET http://127.0.0.1:8000/payables/?type=Agua (donde Agua es el texto de la descripcion de la Entidad/Modelo tipo)
6. Combinacion de Payables que no han sido pagados y segun tipo: http://127.0.0.1:8000/payables/?not_paid=true&type=Agua
7. Transactions - Lista de Todas las Transactions: http://127.0.0.1:8000/transactions/ (desde ahi se puede hacer el POST para agregar mediante el formulario o mediante raw data)
8. Para obtener la info se realiza mediante la solicitud GET http://127.0.0.1:8000/transactions/1/ (Donde 1 representa un id)
9. Transactions entre períodos: Se realiza mediante la solicitud GET http://127.0.0.1:8000/transactions/?from=2021-12-1&to=2021-12-4 (from y to son strings de fecha separadas por guiones en el formato YYYY-M-D

Quedo a disposición para aclaraciones.

Federico Rodriguez
