import boto3
import uuid
from datetime import datetime
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['SOPORTE_TABLE'])

def lambda_handler(event, context):
    try:
        data = event['body']
        usuario_id = data['usuario_id']
        titulo = data['Titulo']
        descripcion = data['descripcion']
        
        ticket_id = str(uuid.uuid4())
        fecha = datetime.utcnow().isoformat()
        
        item = {
            'usuario_id': usuario_id,
            'ticket_id': ticket_id,
            'Titulo': titulo,
            'descripcion': descripcion,
            'estado': 'pendiente',
            'fecha': fecha
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'body': item
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error interno del servidor: {str(e)}"
        }
