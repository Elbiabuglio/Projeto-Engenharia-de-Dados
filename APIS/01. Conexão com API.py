{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install requests\n",
    "#pip install --upgrade requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<Response [200]>\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "url = \"https://servicodados.ibge.gov.br/api/v1/localidades/estados\"\n",
    "response = requests.get(url)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "GET = Solicitar dados \n",
    "POST= Enviar dados \n",
    "PUT = atualizar um recurso existente ou criar um novo recurso se ele não existir\n",
    "DELETE = Excluir \n",
    "PATCH  = aplicar modificações parciais a um recurso.\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ok\n"
     ]
    }
   ],
   "source": [
    "# Mapeamento de códigos de status HTTP para seus respectivos nomes\n",
    "codigo_para_nome = {\n",
    "    100: 'continuar',\n",
    "    101: 'mudando_protocolos',\n",
    "    102: 'processando',\n",
    "    103: 'checkpoint',\n",
    "    122: 'uri_muito_longa',  # ou 'pedido_uri_muito_longo'\n",
    "    200: 'ok',  # ou 'certo', 'tudo_certo', 'tudo_bem', '\\o/', '✓'\n",
    "    201: 'criado',\n",
    "    202: 'aceito',\n",
    "    203: 'informacao_nao_autoritativa',  # ou 'informacao_nao_autorizada'\n",
    "    204: 'sem_conteudo',\n",
    "    205: 'conteudo_redefinido',  # ou 'redefinir'\n",
    "    206: 'conteudo_parcial',  # ou 'parcial'\n",
    "    207: 'multi_status',  # ou 'status_multiplas', 'multi_stati', 'status_multiplos'\n",
    "    208: 'ja_reportado',\n",
    "    226: 'im_usado',\n",
    "    300: 'escolhas_multiplas',\n",
    "    301: 'movido_permanentemente',  # ou 'movido', '\\o-'\n",
    "    302: 'encontrado',\n",
    "    303: 'ver_outro',  # ou 'outro'\n",
    "    304: 'nao_modificado',\n",
    "    305: 'usar_proxy',\n",
    "    306: 'trocar_proxy',\n",
    "    307: 'redirecionamento_temporario',  # ou 'mover_temporario', 'temporario'\n",
    "    308: 'redirecionamento_permanente',  # ou 'continuar_incompleto', 'continuar'\n",
    "    400: 'requisicao_invalida',  # ou 'ruim'\n",
    "    401: 'nao_autorizado',\n",
    "    402: 'pagamento_necessario',  # ou 'pagamento'\n",
    "    403: 'proibido',\n",
    "    404: 'nao_encontrado',  # ou '-o-'\n",
    "    405: 'metodo_nao_permitido',  # ou 'nao_permitido'\n",
    "    406: 'nao_aceitavel',\n",
    "    407: 'autenticacao_proxy_necessaria',  # ou 'proxy_auth', 'autenticacao_proxy'\n",
    "    408: 'tempo_esgotado_requisicao',  # ou 'tempo_esgotado'\n",
    "    409: 'conflito',\n",
    "    410: 'desaparecido',\n",
    "    411: 'tamanho_necessario',\n",
    "    412: 'pre_condicao_falhou',  # ou 'pre_condicao'\n",
    "    413: 'entidade_requisicao_grande',\n",
    "    414: 'uri_requisicao_grande',\n",
    "    415: 'tipo_midia_nao_suportado',  # ou 'midia_nao_suportada', 'tipo_midia'\n",
    "    416: 'intervalo_requisitado_nao_satisfatorio',  # ou 'intervalo_requisitado', 'intervalo_nao_satisfatorio'\n",
    "    417: 'expectativa_falhou',\n",
    "    418: 'sou_um_bule',  # ou 'bule', 'eu_sou_um_bule'\n",
    "    421: 'requisicao_errada',\n",
    "    422: 'entidade_nao_processavel',  # ou 'nao_processavel'\n",
    "    423: 'trancado',\n",
    "    424: 'dependencia_falhou',  # ou 'falha_dependencia'\n",
    "    425: 'colecao_desordenada',  # ou 'desordenada', 'muito_cedo'\n",
    "    426: 'atualizacao_necessaria',  # ou 'atualizacao'\n",
    "    428: 'pre_condicao_necessaria',  # ou 'pre_condicao'\n",
    "    429: 'muitas_requisicoes',  # ou 'muitas'\n",
    "    431: 'campos_cabecalho_grandes',  # ou 'campos_grandes'\n",
    "    444: 'sem_resposta',  # ou 'nenhum'\n",
    "    449: 'tentar_com',  # ou 'tentar'\n",
    "    450: 'bloqueado_por_controles_parentais_windows',  # ou 'controles_parentais'\n",
    "    451: 'indisponivel_por_motivos_legais',  # ou 'motivos_legais'\n",
    "    499: 'cliente_fechou_requisicao',\n",
    "    500: 'erro_servidor_interno',  # ou 'erro_servidor', '/o\\\\', '✗'\n",
    "    501: 'nao_implementado',\n",
    "    502: 'bad_gateway',\n",
    "    503: 'servico_indisponivel',  # ou 'indisponivel'\n",
    "    504: 'tempo_esgotado_gateway',\n",
    "    505: 'versao_http_nao_suportada',  # ou 'versao_http'\n",
    "    506: 'variante_negocia_tambem',\n",
    "    507: 'armazenamento_insuficiente',\n",
    "    509: 'limite_banda_excedido',  # ou 'banda'\n",
    "    510: 'nao_extendido',\n",
    "    511: 'autenticacao_rede_necessaria',  # ou 'autenticacao_rede'\n",
    "}\n",
    "\n",
    "# Exemplo de uso:\n",
    "print(codigo_para_nome[200])  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ver o resultado"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'id': 11,\n",
       "  'sigla': 'RO',\n",
       "  'nome': 'Rondônia',\n",
       "  'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}},\n",
       " {'id': 12,\n",
       "  'sigla': 'AC',\n",
       "  'nome': 'Acre',\n",
       "  'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}},\n",
       " {'id': 13,\n",
       "  'sigla': 'AM',\n",
       "  'nome': 'Amazonas',\n",
       "  'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}},\n",
       " {'id': 14,\n",
       "  'sigla': 'RR',\n",
       "  'nome': 'Roraima',\n",
       "  'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}},\n",
       " {'id': 15,\n",
       "  'sigla': 'PA',\n",
       "  'nome': 'Pará',\n",
       "  'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}},\n",
       " {'id': 16,\n",
       "  'sigla': 'AP',\n",
       "  'nome': 'Amapá',\n",
       "  'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}},\n",
       " {'id': 17,\n",
       "  'sigla': 'TO',\n",
       "  'nome': 'Tocantins',\n",
       "  'regiao': {'id': 1, 'sigla': 'N', 'nome': 'Norte'}},\n",
       " {'id': 21,\n",
       "  'sigla': 'MA',\n",
       "  'nome': 'Maranhão',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 22,\n",
       "  'sigla': 'PI',\n",
       "  'nome': 'Piauí',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 23,\n",
       "  'sigla': 'CE',\n",
       "  'nome': 'Ceará',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 24,\n",
       "  'sigla': 'RN',\n",
       "  'nome': 'Rio Grande do Norte',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 25,\n",
       "  'sigla': 'PB',\n",
       "  'nome': 'Paraíba',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 26,\n",
       "  'sigla': 'PE',\n",
       "  'nome': 'Pernambuco',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 27,\n",
       "  'sigla': 'AL',\n",
       "  'nome': 'Alagoas',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 28,\n",
       "  'sigla': 'SE',\n",
       "  'nome': 'Sergipe',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 29,\n",
       "  'sigla': 'BA',\n",
       "  'nome': 'Bahia',\n",
       "  'regiao': {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}},\n",
       " {'id': 31,\n",
       "  'sigla': 'MG',\n",
       "  'nome': 'Minas Gerais',\n",
       "  'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}},\n",
       " {'id': 32,\n",
       "  'sigla': 'ES',\n",
       "  'nome': 'Espírito Santo',\n",
       "  'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}},\n",
       " {'id': 33,\n",
       "  'sigla': 'RJ',\n",
       "  'nome': 'Rio de Janeiro',\n",
       "  'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}},\n",
       " {'id': 35,\n",
       "  'sigla': 'SP',\n",
       "  'nome': 'São Paulo',\n",
       "  'regiao': {'id': 3, 'sigla': 'SE', 'nome': 'Sudeste'}},\n",
       " {'id': 41,\n",
       "  'sigla': 'PR',\n",
       "  'nome': 'Paraná',\n",
       "  'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}},\n",
       " {'id': 42,\n",
       "  'sigla': 'SC',\n",
       "  'nome': 'Santa Catarina',\n",
       "  'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}},\n",
       " {'id': 43,\n",
       "  'sigla': 'RS',\n",
       "  'nome': 'Rio Grande do Sul',\n",
       "  'regiao': {'id': 4, 'sigla': 'S', 'nome': 'Sul'}},\n",
       " {'id': 50,\n",
       "  'sigla': 'MS',\n",
       "  'nome': 'Mato Grosso do Sul',\n",
       "  'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}},\n",
       " {'id': 51,\n",
       "  'sigla': 'MT',\n",
       "  'nome': 'Mato Grosso',\n",
       "  'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}},\n",
       " {'id': 52,\n",
       "  'sigla': 'GO',\n",
       "  'nome': 'Goiás',\n",
       "  'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}},\n",
       " {'id': 53,\n",
       "  'sigla': 'DF',\n",
       "  'nome': 'Distrito Federal',\n",
       "  'regiao': {'id': 5, 'sigla': 'CO', 'nome': 'Centro-Oeste'}}]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "url = \"https://servicodados.ibge.gov.br/api/v1/localidades/estados\"\n",
    "response = requests.get(url)\n",
    "\n",
    "data = response.json()\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Transformando dados Json em um DF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
       "      <th>regiao</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>11</td>\n",
       "      <td>RO</td>\n",
       "      <td>Rondônia</td>\n",
       "      <td>{'id': 1, 'sigla': 'N', 'nome': 'Norte'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>12</td>\n",
       "      <td>AC</td>\n",
       "      <td>Acre</td>\n",
       "      <td>{'id': 1, 'sigla': 'N', 'nome': 'Norte'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>13</td>\n",
       "      <td>AM</td>\n",
       "      <td>Amazonas</td>\n",
       "      <td>{'id': 1, 'sigla': 'N', 'nome': 'Norte'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>14</td>\n",
       "      <td>RR</td>\n",
       "      <td>Roraima</td>\n",
       "      <td>{'id': 1, 'sigla': 'N', 'nome': 'Norte'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>15</td>\n",
       "      <td>PA</td>\n",
       "      <td>Pará</td>\n",
       "      <td>{'id': 1, 'sigla': 'N', 'nome': 'Norte'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>16</td>\n",
       "      <td>AP</td>\n",
       "      <td>Amapá</td>\n",
       "      <td>{'id': 1, 'sigla': 'N', 'nome': 'Norte'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>17</td>\n",
       "      <td>TO</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>{'id': 1, 'sigla': 'N', 'nome': 'Norte'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>21</td>\n",
       "      <td>MA</td>\n",
       "      <td>Maranhão</td>\n",
       "      <td>{'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>22</td>\n",
       "      <td>PI</td>\n",
       "      <td>Piauí</td>\n",
       "      <td>{'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>23</td>\n",
       "      <td>CE</td>\n",
       "      <td>Ceará</td>\n",
       "      <td>{'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id sigla       nome                                        regiao\n",
       "0  11    RO   Rondônia      {'id': 1, 'sigla': 'N', 'nome': 'Norte'}\n",
       "1  12    AC       Acre      {'id': 1, 'sigla': 'N', 'nome': 'Norte'}\n",
       "2  13    AM   Amazonas      {'id': 1, 'sigla': 'N', 'nome': 'Norte'}\n",
       "3  14    RR    Roraima      {'id': 1, 'sigla': 'N', 'nome': 'Norte'}\n",
       "4  15    PA       Pará      {'id': 1, 'sigla': 'N', 'nome': 'Norte'}\n",
       "5  16    AP      Amapá      {'id': 1, 'sigla': 'N', 'nome': 'Norte'}\n",
       "6  17    TO  Tocantins      {'id': 1, 'sigla': 'N', 'nome': 'Norte'}\n",
       "7  21    MA   Maranhão  {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}\n",
       "8  22    PI      Piauí  {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}\n",
       "9  23    CE      Ceará  {'id': 2, 'sigla': 'NE', 'nome': 'Nordeste'}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "url = \"https://servicodados.ibge.gov.br/api/v1/localidades/estados\"\n",
    "response = requests.get(url)\n",
    "data = response.json()\n",
    "\n",
    "df= pd.DataFrame(data) #Transformando resposta json em df \n",
    "df.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Transformando em DF e Normalizando dados "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html"
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
       "      <td>11</td>\n",
       "      <td>RO</td>\n",
       "      <td>Rondônia</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>Norte</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>12</td>\n",
       "      <td>AC</td>\n",
       "      <td>Acre</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>Norte</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>13</td>\n",
       "      <td>AM</td>\n",
       "      <td>Amazonas</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>Norte</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>14</td>\n",
       "      <td>RR</td>\n",
       "      <td>Roraima</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>Norte</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>15</td>\n",
       "      <td>PA</td>\n",
       "      <td>Pará</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>Norte</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>16</td>\n",
       "      <td>AP</td>\n",
       "      <td>Amapá</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>Norte</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>17</td>\n",
       "      <td>TO</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>1</td>\n",
       "      <td>N</td>\n",
       "      <td>Norte</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>21</td>\n",
       "      <td>MA</td>\n",
       "      <td>Maranhão</td>\n",
       "      <td>2</td>\n",
       "      <td>NE</td>\n",
       "      <td>Nordeste</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>22</td>\n",
       "      <td>PI</td>\n",
       "      <td>Piauí</td>\n",
       "      <td>2</td>\n",
       "      <td>NE</td>\n",
       "      <td>Nordeste</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>23</td>\n",
       "      <td>CE</td>\n",
       "      <td>Ceará</td>\n",
       "      <td>2</td>\n",
       "      <td>NE</td>\n",
       "      <td>Nordeste</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id sigla       nome  regiao.id regiao.sigla regiao.nome\n",
       "0  11    RO   Rondônia          1            N       Norte\n",
       "1  12    AC       Acre          1            N       Norte\n",
       "2  13    AM   Amazonas          1            N       Norte\n",
       "3  14    RR    Roraima          1            N       Norte\n",
       "4  15    PA       Pará          1            N       Norte\n",
       "5  16    AP      Amapá          1            N       Norte\n",
       "6  17    TO  Tocantins          1            N       Norte\n",
       "7  21    MA   Maranhão          2           NE    Nordeste\n",
       "8  22    PI      Piauí          2           NE    Nordeste\n",
       "9  23    CE      Ceará          2           NE    Nordeste"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "url = \"https://servicodados.ibge.gov.br/api/v1/localidades/estados\"\n",
    "response = requests.get(url)\n",
    "data = response.json()\n",
    "\n",
    "df= pd.json_normalize(data)\n",
    "df.head(10)"
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
