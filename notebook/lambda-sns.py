import boto3
import os
from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Inicializar cliente SNS
sns = boto3.client('sns')

# ARN del tópico (puedes ponerlo como variable de entorno)
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', 'arn:aws:sns:REGION:ACCOUNT_ID:lambda-startup-topic')

def lambda_handler(event, context):
    logger.info("Lambda function started")
    logger.info(f"Event: {event}")

    message = f"La función Lambda se ha levantado correctamente a las {datetime.utcnow().isoformat()} UTC."
    subject = "Lambda iniciada"
    
    # Enviar mensaje a SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject=subject
    )
    
    # Registrar en CloudWatch
    logger.info(f"Mensaje enviado a SNS: {message}")


    response = {'response': 'Mensaje enviado a SNS exitosamente.', 'messageVersion': 200}
    print("Response: {}".format(response))

    return response
