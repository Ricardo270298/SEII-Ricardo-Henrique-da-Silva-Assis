python // Identificar a versão do Python
python3 //

#Localizar o Python
which python3 
type python3 

echo $PATH // confere pasta por pasta a localização do Python
/usr/local/bin/python3

nanp . bash_profile
nano .bashrc


alias python=python3 // Não pode ter espaço antes ou depois do =
alias pip=pip3

pip install django
pip show django

import django
import sys

sys.executable

exit()

print(sys.version)
print(sys.executable)
