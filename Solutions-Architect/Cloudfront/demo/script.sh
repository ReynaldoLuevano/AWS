#!/bin/bash

#generate key
openssl genrsa -out private_key.pem 2048

#generate public key
openssl rsa -pubout -in private_key.pem -out public_key.pem