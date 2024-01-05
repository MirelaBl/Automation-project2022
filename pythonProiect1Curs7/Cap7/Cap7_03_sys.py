"""
703 Module
Modulul sys
PF - 15.06.2021 v6
"""  #


import sys

from Cap7.Cap7_02_platform import modaccess


info = {"argv": "primul argument e numele programului",
          "version": "versiunea de Python",
          "platform": "platforma software",
          "executable": "calea catre executabilul Python",
          "path.append('C:/_WT')": "adauga cale",
          "path.extend(['C:/_WT', 'C:/_WT1'])": "adauga mai multe cai",
          }
module = {"modules": "lista cu modulele importate",
          "builtin_module_names": "lista modulelor builtin",
          }
cai =    {"path": "caile unde se acceseaza module" }

print('***************')
modaccess('sys', cai)
print('***************')
modaccess('sys', info)
print('***************')
modaccess('sys', module)

sys.exit()  # utilizat pentru a iesi din program
