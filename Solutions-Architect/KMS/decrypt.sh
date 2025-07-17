#!/bin/bash

echo "Desencriptando chisme -----" 


aws kms decrypt --ciphertext-blob fileb://encoded_secreto.txt \
--key-id alias/Key200 \
--output text \
--query Plaintext | base64 --decode > chisme_descifrado.txt



echo "-- Inicio Chisme desencriptado -----" 
cat chisme_descifrado.txt
echo -e "\n--- Fin de Chisme desencriptado ----- \n" 