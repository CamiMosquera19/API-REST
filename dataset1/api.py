
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import action
import csv

class BdataViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'], url_path='', url_name='Bdata-root') 
    def all_modelo(self, request):
        file_path = './csvdata/tabela-fipe-historico-precos.csv'
        
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                modelo = [row['modelo'] for row in reader if 'modelo' in row]
                
                if modelo:
                    return Response({'modelo': modelo})
                else:
                    return Response({'error': 'Columna no encontrada'}, status=404)
        
        except FileNotFoundError:
            return Response({'error': 'Archivo no encontrado'},status=404)
    

  