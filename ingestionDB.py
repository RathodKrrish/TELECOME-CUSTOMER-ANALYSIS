{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f72393f6-d2d8-433c-9f8a-9029fa624f46",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "engine = create_engine('sqlite:///Inventory.db')\n",
    "\n",
    "def ingest_db(df,table_name,engine):\n",
    "    df.to_sql(table_name , con=engine ,if_exists = 'replace',index=False)\n",
    "\n",
    "for file in os.listdir('data'):\n",
    "    if'.csv' in file:\n",
    "        df = pd.read_csv('data/'+file)\n",
    "        ingest_db(df,file[:-4],engine)"
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
