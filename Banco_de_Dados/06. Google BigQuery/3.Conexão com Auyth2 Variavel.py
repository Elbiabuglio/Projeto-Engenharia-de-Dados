{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from google.cloud import bigquery\n",
    "import pandas as pd\n",
    "from google.oauth2 import service_account"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Especifique as informaçoes de credenciais\n",
    "credencial = {\n",
    "    \n",
    "  \"type\": \"service_account\",\n",
    "  \"project_id\": \"pythonengenharia\",\n",
    "  \"private_key_id\": \"e4145aaaeb10a3\",\n",
    "  \"private_key\": \"-----pythonengenhariaprojeto@pythonengenharia.iam.gserviceaccount.com\",\n",
    "  \"client_id\": \"10068232482\",\n",
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n",
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n",
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n",
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/pythonengenhariaprojeto%40pythonengenharia.iam.gserviceaccount.com\",\n",
    " \n",
    "}\n",
    "\n",
    "\n",
    "# Crie o cliente BigQuery\n",
    "client = bigquery.Client(credentials=service_account.Credentials.from_service_account_info(credencial))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Construa sua consulta\n",
    "query = \"\"\" \n",
    "\n",
    "  SELECT \n",
    "  id\n",
    "  ,first_name\n",
    "  ,last_name\n",
    "  ,email  \n",
    "  ,state\n",
    " FROM `pythoncurso-398511.AulaPython.Clientes` \n",
    " where state in ('Piauí','Alagoas',\n",
    " 'Amazonas','Maranhão','Rondônia')\n",
    "\"\"\"\n",
    "# Execute a consulta\n",
    "resultado = client.query(query)\n",
    "\n",
    "# Converta os resultados em um DataFrame\n",
    "df = resultado.to_dataframe()\n",
    "df.head(30)\n"
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
