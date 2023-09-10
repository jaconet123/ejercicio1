productos={

    1:{
        'id':123,
        'nombre':'libreta',
        'precio':12.500,
        'id_cat':1
    },
    2:{
        'id':345,
        'nombre':'Jabon',
        'precio':10.500,
        'id_cat':2
    },
}

categorias={

    1:{
        'id':1,
        'nombre':'utiles escolares',
        
    },
    2:{
        'id':2,
        'nombre':'Aseo',
        
    }
}

resultante={}
for x in productos.keys():
   resultante[x]={
      'id': productos[x]['id'],
      'nombre': productos[x]['nombre'],
       'categoria': categorias[productos[x]['id_cat']]['nombre']
   }
print(resultante)
