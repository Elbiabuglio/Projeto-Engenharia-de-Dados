{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>sigla</th>\n",
       "      <th>nome</th>\n",
       "      <th>regiao.id</th>\n",
       "      <th>regiao.sigla</th>\n",
       "      <th>regiao.nome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>31</td>\n",
       "      <td>MG</td>\n",
       "      <td>Minas Gerais</td>\n",
       "      <td>3</td>\n",
       "      <td>SE</td>\n",
       "      <td>Sudeste</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id sigla          nome  regiao.id regiao.sigla regiao.nome\n",
       "0  31    MG  Minas Gerais          3           SE     Sudeste"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "estado = 'MG'\n",
    "\n",
    "url = f\"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}\"\n",
    "response = requests.get(url)\n",
    "data = response.json()\n",
    "df = pd.json_normalize(data) # transformando resultado em DF \n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>sigla</th>\n",
       "      <th>nome</th>\n",
       "      <th>regiao.id</th>\n",
       "      <th>regiao.sigla</th>\n",
       "      <th>regiao.nome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>35</td>\n",
       "      <td>SP</td>\n",
       "      <td>São Paulo</td>\n",
       "      <td>3</td>\n",
       "      <td>SE</td>\n",
       "      <td>Sudeste</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>31</td>\n",
       "      <td>MG</td>\n",
       "      <td>Minas Gerais</td>\n",
       "      <td>3</td>\n",
       "      <td>SE</td>\n",
       "      <td>Sudeste</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>33</td>\n",
       "      <td>RJ</td>\n",
       "      <td>Rio de Janeiro</td>\n",
       "      <td>3</td>\n",
       "      <td>SE</td>\n",
       "      <td>Sudeste</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>50</td>\n",
       "      <td>MS</td>\n",
       "      <td>Mato Grosso do Sul</td>\n",
       "      <td>5</td>\n",
       "      <td>CO</td>\n",
       "      <td>Centro-Oeste</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id sigla                nome  regiao.id regiao.sigla   regiao.nome\n",
       "0  35    SP           São Paulo          3           SE       Sudeste\n",
       "1  31    MG        Minas Gerais          3           SE       Sudeste\n",
       "2  33    RJ      Rio de Janeiro          3           SE       Sudeste\n",
       "3  50    MS  Mato Grosso do Sul          5           CO  Centro-Oeste"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Percorrer entre estados\n",
    "\n",
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "estado = ['SP','MG','RJ','MS']\n",
    "\n",
    "dados_estado = []\n",
    "\n",
    "for loop in estado:\n",
    "    response = requests.get(f\"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{loop}\").json()\n",
    "    dados_estado.append(response)\n",
    "\n",
    "df = pd.json_normalize(dados_estado) \n",
    "df.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "sgbds",
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
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
