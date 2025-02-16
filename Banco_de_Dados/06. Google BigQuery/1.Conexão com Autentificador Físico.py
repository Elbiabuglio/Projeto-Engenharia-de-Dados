{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install  google-cloud-bigquery\n",
    "#pip install --upgrade google-cloud-bigquery\n",
    "#pip install  pandas_gbq\n",
    "#pip install  pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\Note reserva\\Desktop\\Curso Engenharia Dados\\Python - SGBDS\\sgbds\\Lib\\site-packages\\google\\cloud\\bigquery\\table.py:1820: UserWarning: BigQuery Storage module not found, fetch data with the REST endpoint instead.\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "from google.cloud import bigquery\n",
    "import pandas as pd\n",
    "\n",
    "# Especifique o caminho para o arquivo JSON de credenciais\n",
    "credencial = r\"C:\\Users\\Note reserva\\Downloads\\pythonengenharia-e4145aaaeb10.json\"\n",
    "\n",
    "# Crie um cliente BigQuery usando as credenciais\n",
    "client = bigquery.Client.from_service_account_json(credencial)\n",
    "\n",
    "# Construa sua consulta\n",
    "query = \"\"\" \n",
    "\n",
    "  SELECT \n",
    "  id\n",
    "  ,first_name\n",
    "  ,last_name\n",
    "  ,email  \n",
    " FROM `pythonengenharia.ProjetoPython.Clientes`\n",
    " where state in ('Piauí','Alagoas','Amazonas')\n",
    "\n",
    "\"\"\"\n",
    "# Execute a consulta\n",
    "resultado = client.query(query)\n",
    "\n",
    "\"\"\"\n",
    "for row in resultado:\n",
    "    print(row)\n",
    "\"\"\"\n",
    "\n",
    "# Converta os resultados em um DataFrame\n",
    "df = resultado.to_dataframe()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
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
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>email</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>18</td>\n",
       "      <td>Jair</td>\n",
       "      <td>Magalhães</td>\n",
       "      <td>jair@exemplo.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>80</td>\n",
       "      <td>Daniela</td>\n",
       "      <td>Góes</td>\n",
       "      <td>daniela@usuario.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>83</td>\n",
       "      <td>Frida</td>\n",
       "      <td>Freire</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>23</td>\n",
       "      <td>Maria</td>\n",
       "      <td>Pires</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>69</td>\n",
       "      <td>Gustavo</td>\n",
       "      <td>Cardoso</td>\n",
       "      <td>gustavo@teste.com</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id first_name  last_name                email\n",
       "0  18       Jair  Magalhães     jair@exemplo.com\n",
       "1  80    Daniela       Góes  daniela@usuario.com\n",
       "2  83      Frida     Freire                 None\n",
       "3  23      Maria      Pires                 None\n",
       "4  69    Gustavo    Cardoso    gustavo@teste.com"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(5)"
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
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
