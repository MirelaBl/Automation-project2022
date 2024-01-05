{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bc3870cc",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "import sys\n",
    "sys.path.extend(['/Users/paulfratila/Library/CloudStorage/OneDrive-Personal/Documents/__PyThOn/0 PyP/_module',\n",
    "                '/Users/paulfratila/Library/CloudStorage/OneDrive-Personal/Documents/__PyThOn'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b4e66bc4",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "<style>\n",
       "     .blue {\n",
       "         color: blue;\n",
       "     }\n",
       "\n",
       "     .orange {\n",
       "         color: orange;\n",
       "     }\n",
       "          \n",
       "     .red {\n",
       "         color: red;\n",
       "     }\n",
       "\n",
       "     .trcz {\n",
       "         color:#48CAE4;\n",
       "     }\n",
       "\n",
       "     .trcz a {\n",
       "         color: inherit;\n",
       "     }\n",
       "\n",
       "     .green {\n",
       "         color: green;\n",
       "     }\n",
       "\n",
       "     .ita {\n",
       "         font-style: italic;\n",
       "     }\n",
       "     \n",
       "     .vio {\n",
       "        font-style: violet;\n",
       "     }\n",
       "\n",
       "    .table_std {\n",
       "        border-collapse: collapse;      \n",
       "    }\n",
       "    \n",
       "    .table_std,\n",
       "    .table_std td,\n",
       "    .table_std th {\n",
       "        border: solid 2px #70C5D7;\n",
       "    }\n",
       "    \n",
       "    .table_std tr:nth-child(even) {\n",
       "        background-color: #C4F3FD;\n",
       "    }\n",
       "    \n",
       "    .table_std tr:nth-child(odd) {\n",
       "        background-color: #70C5D7;\n",
       "    }\n",
       "    \n",
       "    .table_std td {\n",
       "        font: bold 20px sans-serif;\n",
       "        text-align: left;\n",
       "        text-indent: 10px;\n",
       "    }\n",
       "    \n",
       "    .table_std th {\n",
       "        font: bold 20px sans-serif;\n",
       "        text-align: center;\n",
       "    }\n",
       "\n",
       "\n",
       "\n",
       "\n",
       "</style>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from ipythoncss import HTML, STILURI\n",
    "HTML(STILURI)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "325b1001",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "# <span class=\"blue\">5. Programarea orientata pe obiecte (OOP)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64b62c5d",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "# <span class=\"blue\">5.1. Introducere in OOP"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a06ec54",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.1.1. Necesitatea OOP"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0f216288",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: Logan\n",
      "Roti: l\n",
      "Model 4\n"
     ]
    }
   ],
   "source": [
    "# o lista\n",
    "lista_auto = []\n",
    "\n",
    "# lista nu are metode de validare a continutului. Accepta \"orice\"\n",
    "lista_auto.append(['Logan', 4, 'ABS'])\n",
    "lista_auto.append([4, 'Duster', 'EBS'])\n",
    "lista_auto.append('Alt_model')\n",
    "\n",
    "# lucrul cu datele este greoi\n",
    "print('Model:',lista_auto[0][0])\n",
    "\n",
    "# nu avem garantii asupra datelor introduse\n",
    "print('Roti:', lista_auto[2][1])  # ne asteptam sa aflam numarul de roti, dar...\n",
    "print('Model', lista_auto[1][0])  # ne asteptam sa aflam modelul, dar ..."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aeb0b470",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Daca dorim sa rezolvam probleme mai complexe utilizand programarea procedurala (Ex: gestiunea stocurilor sau informatii despre persoane, meserii, hobiuri, etc.) : \n",
    " ### - Am putea utiliza notiunile deja cunoscute (liste, dictionare, etc); \n",
    " ### - Solutie complicata, ineficienta si nesigura;\n",
    " ### - Cod destul de greu de urmarit si neintuitiv, \n",
    " ### - Cod greu de administrat;\n",
    " ### - Posibil greu de validat si de asigurarea coerentei.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81c5c25f",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.1.2. Beneficiile OOP"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f2c6c2b",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Structureaza codul \n",
    "  ### - usor de utilizat;\n",
    "  ### - usor de inteles;\n",
    "  ### - usor de intretinut;\n",
    "  ### - usor de extins;\n",
    "  ### - usurinta in colaborare - modularizare;\n",
    "\n",
    "### Scalabilitate – permite adaugarea de noi tipuri de date, inexistente pana atunci;\n",
    "\n",
    "### Refolosirea codului - Un nou tip de date, odata definit, testat si validat, poate fi refolosit in alte aplicatii.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d19a78eb",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.1.3. Instrumente utilizate de OOP"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0fd2b073",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### <span class=\"green ita\">Clasa \n",
    "### - reprezinta abstractizarea caracteristicilor unui lucru din viata reala \n",
    "### - pune la un loc datele si functionalitatile;\n",
    "\n",
    "### <span class=\"green ita\">Obiectul(instanta) \n",
    "### - contine datele (informatiile)\n",
    "\n",
    "### <span class=\"green ita\">Metoda \n",
    "### - asigura functionalitatile obiectelor. \n",
    "\n",
    "### <span class=\"green ita\">Atributul \n",
    "### - reprezinta o valoare a unei caracteristici a obiectului.\n",
    "\n",
    "### In viata reala un obiect este ceva tangibil. In software obiectul este destinat sa faca ceva. Este o colectie de date si functionalitati;\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c91b4075",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.1.4. Caracteristicile OOP"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4efb0d47",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### <span class=\"green ita\">Abstractizare\n",
    "### - permite ascunderea informatiilor neesentiale si acces doar la cele necesare (privire din avion)\n",
    "\n",
    "### <span class=\"green ita\">Incapsulare\n",
    "### - permite ascunderea informatiilor sensibile si accesarea lor doar prin intermediul metodelor\n",
    "\n",
    "### <span class=\"green ita\">Mostenire (Inheritance)\n",
    "### - permite extinderea caracteristicilor unui obiect\n",
    "\n",
    "### <span class=\"green ita\">Polymorfism  \n",
    "### - ofera flexibilitate in utilizarea unor metode cu nume identice pentru clase diferite"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "74ab8e41",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "# <span class=\"blue\">5.2. Clasa, obiect, metoda, atribut"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe153f28",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.2.1. Clasa"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25aaf7a2",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Clasa - un nou tip de date, compus, definit de programator, care permite punerea impreuna atat a datelor(informatiilor) cat si a functionalitatilor. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03c68b25",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# Sintaxa\n",
    "class NumeClasa:\n",
    "    \"\"\"doc_string\"\"\"\n",
    "    # bloc de instructiuni"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b65e6b9",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### - numele clasei\n",
    "### - docstringul\n",
    "### - blocul de instructiuni\n",
    "### - type() si dir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "048d085a",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "class Auto:\n",
    "    \"\"\"prima clasa, despre autoturisme\"\"\"\n",
    "\n",
    "    marca = ''\n",
    "    siguranta = ''\n",
    "    nr_roti = 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ffe3cf0c",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Marca inainte: \n",
      "4\n",
      "Marca dupa: Mercedes\n"
     ]
    }
   ],
   "source": [
    "print('Marca inainte:', Auto.marca)          # putem accesa atributul\n",
    "print(Auto.nr_roti)\n",
    "Auto.marca = 'Mercedes'    # putem modifica atributul\n",
    "print('Marca dupa:', Auto.marca)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c768ab2",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.2.2. Obiect"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "725c3927",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Obiectul este o instanta a unei clase. \n",
    "### - Crearea de obiecte ale unei clase poarta numele de instantiere\n",
    "### - Putem crea cate obiecte avem nevoie\n",
    "### - Obiectul poate avea atribute generale, specifice clasei si atribute proprii, obtinute prin aplicarea metodelor\n",
    "### - Totalitatea atributelor determina starea obiectului, care, de regula, este diferita de a celorlate obiecte de acelasi tip\n",
    "### - Sintaxa pentru crearea unui obiect (instantiere):\n",
    "      NumeObiect = NumeClasa([parametrii]) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4117efb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "Auto.marca = 'ceva'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "95222af6",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# crearea de obiecte\n",
    "logan = Auto()\n",
    "duster = Auto()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d473535d",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ceva\n",
      "4\n",
      "{}\n"
     ]
    }
   ],
   "source": [
    "# accesarea atributelor\n",
    "print(logan.marca)\n",
    "print(logan.nr_roti)\n",
    "print(logan.__dict__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c80a7515",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# modificarea atributelor\n",
    "logan.marca = 'Dacia logan'\n",
    "duster.siguranta = 'abs'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "623ca168",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dacia logan\n",
      "\n",
      "{'marca': 'Dacia logan'}\n",
      "ceva\n",
      "abs\n",
      "{'siguranta': 'abs'}\n"
     ]
    }
   ],
   "source": [
    "print(logan.marca)\n",
    "print(logan.siguranta)\n",
    "print(logan.__dict__)\n",
    "\n",
    "print(duster.marca)\n",
    "print(duster.siguranta)\n",
    "print(duster.__dict__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e93aa80",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# dictionarul cu atributele obiectului\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "435daa3b",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class '__main__.Auto'>\n"
     ]
    }
   ],
   "source": [
    "# type()\n",
    "print(type(logan))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b7d339f2",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__class__',\n",
       " '__delattr__',\n",
       " '__dict__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getstate__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__le__',\n",
       " '__lt__',\n",
       " '__module__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " '__weakref__',\n",
       " 'marca',\n",
       " 'nr_roti',\n",
       " 'siguranta']"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# dir()\n",
    "dir(logan)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "20bfcc44",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<__main__.Auto object at 0x1044ba2d0>\n"
     ]
    }
   ],
   "source": [
    "# print()\n",
    "print(logan)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1c40248",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.2.3. Metoda"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "705ea28f",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Metoda este o functie definita in interiorul unei clase, cu ajutorul careia atasam atribute obiectelor (instantelor).\n",
    "\n",
    "### - metoda constituie interfata cu ajutorul careia modificam functionalitatile obiectului\n",
    "\n",
    "### - sintaxa pentru aplicarea unei metode:\n",
    "\t\tNumeObiect.Metoda([parametrii]) \t\n",
    "\n",
    "### - toate obiectele unei clase au acces la metodele acesteia\n",
    "### - aplicarea metodei modifica starea obiectului\n",
    "### - metoda preia automat primul argument (self)\n",
    "### - self asigura atribuirea de valoare atributului caruia ii aplicam metoda si numai aceluia\n",
    "### - self asigura accesarea atributului unui obiect in interiorul intregii clase (in toate metodele clasei)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5940470",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# Sintaxa pentru crearea unei metode:\n",
    "def numeMetoda(self [,parametri, optional]):\n",
    "    \"\"\"docstring\"\"\"\n",
    "    # bloc_instructiuni"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e220f0ab",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "class Auto:\n",
    "    \"\"\"refactoring clasa Auto - cu metode\"\"\"\n",
    "\n",
    "    nr_roti = 4\n",
    "    model = 'no_name'\n",
    "    siguranta = '-'\n",
    "\n",
    "    def set_model(self, model):\n",
    "        \"\"\"atribuie model propriu\"\"\"\n",
    "        self.model = model\n",
    "\n",
    "    def set_siguranta(self, elem_siguranta):\n",
    "        \"\"\"atribuie siguranta proprie\"\"\"\n",
    "        self.siguranta = elem_siguranta"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d2925fc2",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# instantiem\n",
    "logan = Auto()\n",
    "duster = Auto()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "0b054c4c",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no_name\n",
      "-\n"
     ]
    }
   ],
   "source": [
    "# accesam atributele actuale si verificam in __dict__\n",
    "print(logan.model)\n",
    "print(duster.siguranta)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "761f5867",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n",
      "{}\n"
     ]
    }
   ],
   "source": [
    "print(logan.__dict__)\n",
    "print(duster.__dict__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f48baa53",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# aplicam metodele si observam schimbarea in __dict__\n",
    "duster.set_model('Dacia duster')\n",
    "logan.set_siguranta('ABS')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "80e7fda7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "no_name\n",
      "-\n",
      "{'siguranta': 'ABS'}\n",
      "{'model': 'Dacia duster'}\n",
      "ABS\n",
      "Dacia duster\n"
     ]
    }
   ],
   "source": [
    "print(logan.model)\n",
    "print(duster.siguranta)\n",
    "print(logan.__dict__)\n",
    "print(duster.__dict__)\n",
    "print(logan.siguranta)\n",
    "print(duster.model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "81c42d23",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# stergerea obiectelor\n",
    "del logan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ea3a3fc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<__main__.Auto object at 0x104542cd0>\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'logan' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [28], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28mprint\u001b[39m(duster)\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43mlogan\u001b[49m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'logan' is not defined"
     ]
    }
   ],
   "source": [
    "print(duster)\n",
    "print(logan)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a48f943",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.2.4. Atribut"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e0fd9e7",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Atributul este o variabila atasata obiectului.\n",
    "\n",
    "### - un obiect poate avea atat atribute(variabile) de clasa cat si atribute proprii, date de aplicarea unor metode.\n",
    "\n",
    "### - atributul propriu este dispobibil doar dupa aplicarea metodei\n",
    "\n",
    "### - atributul de clasa NU necesita aplicarea unei metode\n",
    "\n",
    "### - daca obiectul are un atribut propriu, dat de o metoda, cu un nume similar cu al unei variabile de clasa atributul propriu are prioritate. Obiectul nu va mai avea acces la variabila de clasa."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4505635",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### O variabila de clasa aste in afara unei metode, in interiorul clasei\n",
    "\n",
    "### - exista intr-un singur exemplar (spre deosebire de atribute, care se multiplica pentru fiecare obiect)\n",
    "\n",
    "### - este accesibila tuturor obiectelor clasei, cu aceeasi valoare\n",
    "\n",
    "### - poate fi modificata printr-o metoda a clasei"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73b6dcc9",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# instantiem, accesam atributele de clasa, apelam metodele\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "a72c8107",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "class Demo:\n",
    "    \"\"\"Diferenta intre atribut de clasa si atribut de instanta\"\"\"\n",
    "    \n",
    "    atribut = 10;\n",
    "    \n",
    "    def metoda1(self, valoare):\n",
    "        self.atribut = valoare\n",
    "        \n",
    "        \n",
    "    def metoda2(self, valoare):\n",
    "        Demo.atribut = valoare"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "97c286fb",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# instantiem 2 obiecte\n",
    "o1 = Demo()\n",
    "o2 = Demo()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c79e48e4",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{}\n",
      "{}\n",
      "10\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "# accesam atributele pentru fiecare (in interiorul clasei/in exteriorul clasei - global)\n",
    "print(o1.__dict__)\n",
    "print(o2.__dict__)\n",
    "print(o1.atribut)\n",
    "print(o2.atribut)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "108a0c35",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# apelam unui obiect metodat1, celuilalt metoda2\n",
    "o1.metoda1(99)\n",
    "o2.metoda2(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0f96748e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'atribut': 99}\n",
      "{}\n",
      "99\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "print(o1.__dict__)\n",
    "print(o2.__dict__)\n",
    "print(o1.atribut)\n",
    "print(o2.atribut)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "4d792dbd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "print(Demo.atribut)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "5b6fe454",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "class Auto:\n",
    "    \"\"\"refactoring clasa Auto - cu metode\"\"\"\n",
    "\n",
    "    nr_roti = 4\n",
    "    model = 'no_name'\n",
    "    siguranta = '--'\n",
    "\n",
    "    \n",
    "    def set_model(self, model):\n",
    "        \"\"\"atribuie model propriu\"\"\"\n",
    "        self.model = model\n",
    "\n",
    "        \n",
    "    def set_siguranta(self, elem_siguranta):\n",
    "        \"\"\"atribuie siguranta proprie\"\"\"\n",
    "        self.siguranta = elem_siguranta\n",
    "        \n",
    "    def listeaza(self):\n",
    "        result  = ''\n",
    "        result += f'Model: {self.model}'\n",
    "        result += f'\\nRoti: {self.nr_roti}'\n",
    "        result += f'\\nSig: {self.siguranta}'\n",
    "        print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "9416ce9c",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# testam metodele si atributele\n",
    "bmw = Auto()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7f3f80af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 no_name --\n",
      "{}\n",
      "no_name\n"
     ]
    }
   ],
   "source": [
    "print(bmw.nr_roti, bmw.model, bmw.siguranta)\n",
    "print(bmw.__dict__)\n",
    "print(Auto.model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "bed16271",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: m4\n",
      "Roti: 4\n",
      "Sig: ABS\n"
     ]
    }
   ],
   "source": [
    "bmw.set_model('m4')\n",
    "bmw.set_siguranta('ABS')\n",
    "bmw.listeaza()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "2fceeaea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 m4 ABS\n",
      "{'model': 'm4', 'siguranta': 'ABS'}\n",
      "no_name\n"
     ]
    }
   ],
   "source": [
    "print(bmw.nr_roti, bmw.model, bmw.siguranta)\n",
    "print(bmw.__dict__)\n",
    "print(Auto.model)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "afef5537",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: m4\n",
      "Roti: 4\n",
      "Sig: ABS\n"
     ]
    }
   ],
   "source": [
    "bmw.listeaza()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b880aaaf",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\"> 5.2.5. Namespace(scope)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aadd5db5",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Exista mai multe niveluri de namespace:\n",
    "### - al functiilor predefinite, creat la start si disponibil pe toata durata rularii aplicatiei\n",
    "### - al modulelor, creat la pornirea (import-ul) acestora\n",
    "### - local, al functiilor, disponibil pe durata apelarii acestora\n",
    "### - global, unde putem accesa functiile definite in afara unui bloc de cod (in global namespace)\n",
    "### - global si nonlocal in inner functions\n",
    "\n",
    "### - Fiecare clasa, obiect sau metoda au namespace-uri proprii.\n",
    "\n",
    "### - O functie care apartine de global namespace, e vizibila oriunde avem nevoie de ea;\n",
    "\n",
    "### - O metoda e vizibila doar in namespace-ul clasei in care a fost creata. \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "917e2f53",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "# exercitiul Cap5_07_scope - cu debugger"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a9fb454",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.2.6. Metode speciale <span class=\"red\">__ init __"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05a91fd8",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Metoda <span class=\"vio\">__ init __</span> (constructor) este o metoda speciala, privata, care este rulata automat de fiecare data când un obiect este creat\n",
    "### - metoda <span class=\"vio\">__ init __</span> poate initializa diferite atribute ale obiectului (de regula cele obligatorii)\n",
    "### - prin intermediul acestei metode putem introduce elemente de validare a acestor atribute\n",
    "### - metoda speciala <span class=\"vio\">__ init __</span> nu poate folosi return.\n",
    "### - putem initializa sau modifica atribute de clasa prin intermediul acestei metode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "685a11b7",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "class Auto:\n",
    "    \"\"\"refactoring clasa Auto - cu metoda __init__\"\"\"\n",
    "\n",
    "    nr_roti = 4\n",
    "\n",
    "    def __init__(self, model, siguranta='-'):\n",
    "        self.model = model\n",
    "        self.siguranta = siguranta\n",
    "        self.claxon = 'da'\n",
    "\n",
    "    def set_model(self, model):\n",
    "        self.model = model\n",
    "\n",
    "    def set_siguranta(self, elem_siguranta):\n",
    "        self.siguranta = elem_siguranta\n",
    "\n",
    "    def listeaza(self):\n",
    "        result  = ''\n",
    "        result += f'Model: {self.model}'\n",
    "        result += f'\\nRoti: {self.nr_roti}'\n",
    "        result += f'\\nSig: {self.siguranta}'\n",
    "        return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "7d8c94f4",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "mercedes = Auto('sc300', 'abs')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "6e525a36",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'model': 'sc300', 'siguranta': 'abs', 'claxon': 'da'}"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mercedes.__dict__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "bc28a09f",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: sc300\n",
      "Roti: 4\n",
      "Sig: abs\n"
     ]
    }
   ],
   "source": [
    "print(mercedes.listeaza())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "47ee9002",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<__main__.Auto object at 0x103fc0990>\n"
     ]
    }
   ],
   "source": [
    "print(mercedes)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5dd43914",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.2.7. Metode speciale <span class=\"red\">__ str __"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a82368df",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Metoda <span class=\"vio\">__ str __</span> este o metoda speciala care este rulata de fiecare data cand printam un obiect: print(numeObiect)  \n",
    "### - metoda speciala <span class=\"vio\">__ str __</span> are obligatoriu un return si va returna un sir de caractere\n",
    "### - exista o implementare default, care afiseaza numele clasei din care face parte obiectul. Implementarea noastra va suprascrie metoda default"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "3364e8fc",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "class Auto:\n",
    "    \"\"\"refactoring clasa Auto - cu metodele __init__ si __str__\"\"\"\n",
    "\n",
    "    nr_roti = 4\n",
    "\n",
    "    def __init__(self, model, siguranta='--'):\n",
    "        self.model = model\n",
    "        self.siguranta = siguranta\n",
    "        self.claxon = 'da'\n",
    "\n",
    "        \n",
    "    def set_model(self, model):\n",
    "        self.model = model\n",
    "\n",
    "        \n",
    "    def set_siguranta(self, elem_siguranta):\n",
    "        self.siguranta = elem_siguranta\n",
    "\n",
    "\n",
    "    def __str__(self):\n",
    "        result  = ''\n",
    "        result += f'Model: {self.model}'\n",
    "        result += f'\\nRoti: {self.nr_roti}'\n",
    "        result += f'\\nSig: {self.siguranta}'\n",
    "        return result        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "f70551d0",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "porsche = Auto('Chayene', 'abs') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "295d6bbb",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'model': 'Chayene', 'siguranta': 'abs', 'claxon': 'da'}\n"
     ]
    }
   ],
   "source": [
    "print(porsche.__dict__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "a1505fd6",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: Chayene\n",
      "Roti: 4\n",
      "Sig: abs\n"
     ]
    }
   ],
   "source": [
    "print(porsche)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8d6ece6",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "## <span class=\"trcz\">5.2.6. Metode speciale <span class=\"red\">__ del __"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02330d9d",
   "metadata": {
    "pycharm": {
     "name": "#%% md\n"
    }
   },
   "source": [
    "### Metoda <span class=\"vio\">__ del __</span> este o metoda speciala care este rulata de fiecare data cand stergem un obiect: del numeObiect.  \n",
    "### - metoda are o implementare default, care va sterge obiectul (destructor)\n",
    "### - implementarea noastra va adauga noi functionalitati metodei (nu ii schimba scopul - va sterge in continuare obiectul)\n",
    "### - poate inchide conexiuni, poate afisa mesaje, etc, in plus fata de ceea ce avea oricum de facut - stergerea obiectului"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "086aaf94",
   "metadata": {
    "pycharm": {
     "name": "#%%\n"
    }
   },
   "outputs": [],
   "source": [
    "class Auto:\n",
    "    \"\"\"refactoring clasa Auto - cu metodele __init__ si __str__\"\"\"\n",
    "\n",
    "    nr_roti = 4\n",
    "    nr_modele = 0\n",
    "\n",
    "    def __init__(self, model, siguranta='-'):\n",
    "        self.model = model\n",
    "        self.siguranta = siguranta\n",
    "        self.claxon = 'da'\n",
    "        Auto.nr_modele += 1\n",
    "\n",
    "        \n",
    "    def set_model(self, model):\n",
    "        self.model = model\n",
    "\n",
    "        \n",
    "    def set_siguranta(self, elem_siguranta):\n",
    "        self.siguranta = elem_siguranta\n",
    "\n",
    "\n",
    "    def __str__(self):\n",
    "        result  = ''\n",
    "        result += f'Model: {self.model}'\n",
    "        result += f'\\nRoti: {self.nr_roti}'\n",
    "        result += f'\\nSig: {self.siguranta}'\n",
    "        return result        \n",
    "    \n",
    "    \n",
    "    def __del__(self):\n",
    "        print(f'Obiectul {self.model} a fost sters. Numar modele inainte: {Auto.nr_modele}')\n",
    "        Auto.nr_modele -= 1    \n",
    "        print(f'Numar modele dupa: {Auto.nr_modele}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "bf649350",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Obiectul Chayene a fost sters. Numar modele inainte: 2\n",
      "Numar modele dupa: 1\n"
     ]
    }
   ],
   "source": [
    "porsche = Auto('Chayene', 'abs') \n",
    "bmw = Auto('m4')\n",
    "logan = Auto('mcv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "586bbe5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Auto.nr_modele"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "16b0d85f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Obiectul mcv a fost sters. Numar modele inainte: 3\n",
      "Numar modele dupa: 2\n"
     ]
    }
   ],
   "source": [
    "del logan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "1d1541d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: m4\n",
      "Roti: 4\n",
      "Sig: -\n"
     ]
    }
   ],
   "source": [
    "print(bmw)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
