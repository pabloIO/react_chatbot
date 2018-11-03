#!/bin/bash
echo "INICIANDO MONGO DB"
mongod &
echo "INICIALIZANDO APLICACIÓN WEB: VALKIR.IA"
python app.py &

