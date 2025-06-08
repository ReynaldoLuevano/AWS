def lambda_handler(event, context):
    
    operation = event["operation"]
    message = event["message"]
    custom_message = None

    if operation == 0:
        custom_message = "Recibida la operación 0: " + message

    elif operation == 1:
        custom_message = "Pues hemos recibido un 1: " + message

    else:
        custom_message = "Que no, que ha sido un 2: " + message

    response = {
        "custom_message": custom_message,
    }


    return response