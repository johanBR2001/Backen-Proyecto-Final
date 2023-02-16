import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


    
@csrf_exempt
def loginCliente(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        # TODO: Consultar a base de datos
        if usuario == "pw" and password == "123":
            # Correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    


@csrf_exempt
def loginRestaurante(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        # TODO: Consultar a base de datos
        if usuario == "rest" and password == "1234":
            # Correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    
    
    
def obtenerRestaurantes(request):
    if request.method == "GET":
        #TODO: consultas a BD
        dictResponse = {
            "error": "",
            "restaurantes": [
                {
                    "id":1,
                    "tittle":"Long Horn",
                    "category": "Carnes",
                    "img": "https://img.mesa247.pe/archivos/restaurante/logo/2021/10/restaurante-longhorn-san-miguel-1.png"
                    },
                    {
                        "id":2,
                        "tittle":'Hornero',
                        "category": 'Carnes',
                        "img": "https://media-cdn.tripadvisor.com/media/photo-s/17/96/74/c5/el-hornero-san-isidro.jpg"
                    },
                    {
                        "id":3,
                        "tittle":'Mis costillitas',
                        "category": 'Carnes',
                        "img": "https://peruretail.sfo3.cdn.digitaloceanspaces.com/wp-content/uploads/1656596285689.png"
                    },
                    {
                        "id":4,
                        "tittle":'Señor Limon',
                        "category": 'Mariscos',
                        "img": "https://media-cdn.tripadvisor.com/media/photo-s/0f/d9/0b/24/photo1jpg.jpg"
                    },
                    {
                        "id":5,
                        "tittle":'Embarcadero 41',
                        "category": 'Mariscos',
                        "img": "https://tofuu.getjusto.com/orioneat-prod-resized/7at29vGyrTXCNPdyS-300-500.webp"
                    },
                    {
                        "id":6,
                        "tittle":'Fudgy Chewy Brownies',
                        "category": 'Mariscos',
                        "img": "https://complejoruralelmolinillo.com/wp-content/uploads/2018/01/restaurante.png"
                    },
                    {
                        "id":7,
                        "tittle":'Punto Italiano  ',
                        "category": 'Pastas',
                        "img": "https://img.restaurantguru.com/rd12-Punto-Italiano-interior.jpg"
                    },
                    {
                        "id":8,
                        "tittle":'La Piccolina',
                        "category": 'Pastas',
                        "img": "https://www.trattorialapiccolina.pe/wp-content/uploads/2020/03/visitanos1.jpg"
                    },{
                        "id":9,
                        "tittle":'La piazzeta',
                        "category": 'Pastas',
                        "img": "https://media-cdn.tripadvisor.com/media/photo-s/1c/25/33/bd/terrasse-de-la-piazzetta.jpg"
                        }
  ]
        }
        
            
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error" : "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
        
        
        
        
        
        
        
        
        
def Realizado(request):
    if request.method != "GET":
        dictError = {
            "error": "Peticion erronea."
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    else: 
        lista = [
            {
                "id": 1,
                "cod": "CODIGO:RLH-356",
                "producto" : "BIFE ANGOSTO",
                "precio": "Precio: S/.79",
                "estado": "Enviado"
            },
            {
                "id": 2,
                "cod": "CODIGO:RLH-741",
                "producto" : "Lomo fino 400g",
                "precio": "Precio: S/.73",
                "estado": "Enviado"
            },
            {
                "id": 3,
                "cod": "CODIGO:RLH-847",
                "producto" :  "Parrilla 4 Carnes (4 personas)",
                "precio": "Precio: S/.250",
                "estado": "Enviado"
            }
        ]

        dictResponse = {
            "error":"",
            "pedido": lista
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    
  