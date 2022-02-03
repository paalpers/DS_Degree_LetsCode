{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "__main__.LinkedList"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# vamos reproduzir o comportamento abaixo\n",
    "# na LinkedList\n",
    "# sequencial = []\n",
    "# sequencial.append(9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "# class Node:\n",
    "#     def __init__(self, data):\n",
    "#         self.data = data\n",
    "#         self.next = None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from node import Node\n",
    "\n",
    "class LinkedList:\n",
    "    def __init__(self):\n",
    "        self.head = None\n",
    "        self.size = 0 \n",
    "    \n",
    "    def append(self, element):\n",
    "# há dois casos ao add um novo elemento\n",
    "# 1 a lista pode estar vazia, (head = None) o else da função abaixo\n",
    "# 2 a lista já possui elementos nela o if da função abaixo\n",
    "        '''\n",
    "        adiciona um novo elemento\n",
    "        ao final da lista\n",
    "        '''\n",
    "        \n",
    "        if self.head:\n",
    "            pointer = self.head\n",
    "            # inserção quando a lista já possui elementos\n",
    "            while(pointer.next):# A\n",
    "                pointer = pointer.next\n",
    "            pointer.next = Node(element) # B\n",
    "\n",
    "        # tanto pointer quanto head\n",
    "        # apontam para o mesmo espaço\n",
    "        # de memoria\n",
    "         \n",
    "        # A    \n",
    "        # o while será executado e\n",
    "        # enquanto um elemento possuir um next != None\n",
    "        # eu consigo chegar ao próximo elemento da lista\n",
    "        \n",
    "        # B\n",
    "        # Quando a expressão do while for falsa\n",
    "        # teremos chegado ao ultimo elemento\n",
    "        # Então guardamaos este novo elemento\n",
    "        # dentro de um Node()\n",
    "        # Desta forma o ultimo elemento da lista\n",
    "        # que antes possuia um .next vazio\n",
    "        # agora terá como .next este novo elemento criado     \n",
    "            \n",
    "        else:\n",
    "            # primeira inserção\n",
    "            self.head = Node(element)\n",
    "        self.size += 1\n",
    "        \n",
    "    \n",
    "        \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
