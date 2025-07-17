#!/bin/bash

echo "Encriptando chisme -----" 


aws kms encrypt \
    --key-id alias/Key200 \
    --plaintext fileb://misecreto.txt \
    --output text \
    --query CiphertextBlob | base64 \
    --decode > encoded_secreto.txt


echo  "-- Inicio Chisme encriptado -----" 
cat encoded_secreto.txt
echo -e "\n--- Fin de Chisme desencriptado ----- \n" 