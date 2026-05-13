{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d740198",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Obtener Network ID de una Organizacion\n",
    "\n",
    "import requests\n",
    "\n",
    "url = \"https://api.meraki.com/api/v1/organizations/Organization-ID/networks\" # Asegúrate de reemplazar esto por tu  Organization ID real\n",
    "\n",
    "payload = None\n",
    "\n",
    "headers = {\n",
    "    \"Authorization\": \"Bearer 92\",  # Asegúrate de reemplazar esto por tu token real\n",
    "    \"Accept\": \"application/json\"\n",
    "}\n",
    "\n",
    "response = requests.request('GET', url, headers=headers, data = payload)\n",
    "\n",
    "print(response.text.encode('utf8'))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a58e1394",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Obtener Network ID de una Organizacion y filtrarlo por nombre\n",
    "\n",
    "import requests\n",
    "import json\n",
    "\n",
    "url = \"https://api.meraki.com/api/v1/organizations/Organization-ID/networks\"\n",
    "\n",
    "headers = {\n",
    "    \"Authorization\": \"Bearer x\",  # Asegúrate de reemplazar esto por tu token real\n",
    "    \"Accept\": \"application/json\"\n",
    "}\n",
    "\n",
    "response = requests.get(url, headers=headers)\n",
    "\n",
    "if response.status_code == 200:\n",
    "    networks = response.json()\n",
    "    for network in networks:\n",
    "        print('---')\n",
    "        print(f\"ID: {network.get('id')}\")\n",
    "        print(f\"Nombre: {network.get('name')}\")\n",
    "        print(f\"Tipo: {network.get('type')}\")\n",
    "        print(f\"Time Zone: {network.get('timeZone')}\")\n",
    "        print(f\"Tags: {network.get('tags')}\")\n",
    "else:\n",
    "    print(f\"Error: {response.status_code}\")\n",
    "    print(response.text)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
