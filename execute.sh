#!/bin/bash
echo -n "Ingresa RFC: "
read rfc

echo -n "Ingresa CIEC:"
read ciec

python /c/Server/htdocs/Python/Examen/ValidData.py rfc ciec #send parameter to python script