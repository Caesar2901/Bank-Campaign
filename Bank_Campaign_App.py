{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "76e07db8-c649-4c71-863d-65cdadebb13b",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'Bank_model_trained.pkl'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 5\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpickle\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[1;32m----> 5\u001b[0m loaded_model \u001b[38;5;241m=\u001b[39m pickle\u001b[38;5;241m.\u001b[39mload(\u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mBank_model_trained.pkl\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m'\u001b[39m))\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mbank_function\u001b[39m(input_data):\n\u001b[0;32m      8\u001b[0m     input_data_as_numpy_array \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39masarray(input_data)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:324\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    318\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    319\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    320\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    321\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    322\u001b[0m     )\n\u001b[1;32m--> 324\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m io_open(file, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'Bank_model_trained.pkl'"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import streamlit as st\n",
    "\n",
    "loaded_model = pickle.load(open(\"Bank_model_trained.pkl\", 'rb'))\n",
    "\n",
    "def bank_function(input_data):\n",
    "    input_data_as_numpy_array = np.asarray(input_data)\n",
    "    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)\n",
    "    prediction = loaded_model.predict(input_data_reshaped)\n",
    "\n",
    "    if prediction[0] == 0:\n",
    "        return 'The client will not subscribe to our term deposit'\n",
    "    else:\n",
    "        return 'The client will subscribe to our term deposit'\n",
    "\n",
    "def main():\n",
    "    st.title(\"Bank Marketing for Term Deposit Prediction Web App\")\n",
    "\n",
    "    Age = st.text_input(\"Number of Age: \")\n",
    "    Balance = st.text_input(\"Account Balance: \")\n",
    "    Day = st.text_input(\"Last Contact Day of the Month: \")\n",
    "    Duration = st.text_input(\"Duration of Last Contact: \")\n",
    "    Campaign = st.text_input(\"Number of Contacts During Campaign: \")\n",
    "    Pdays = st.text_input(\"Days Since Last Contact: \")\n",
    "    Previous = st.text_input(\"Number of Previous Contacts: \")\n",
    "    Job = st.text_input(\"Job Type: \")\n",
    "    Marital = st.text_input(\"Marital Status: \")\n",
    "    Education = st.text_input(\"Education Level: \")\n",
    "    Default = st.text_input(\"Have Credit in Default?: \")\n",
    "    Housing = st.text_input(\"Have Housing Loan?: \")\n",
    "    Loan = st.text_input(\"Have Personal Loan?: \")\n",
    "    contact = st.text_input(\"Contact Communication Type: \")\n",
    "    Month = st.text_input(\"Last Contact Month: \")\n",
    "    poutcome = st.text_input(\"Outcome of Previous Campaign: \")\n",
    "\n",
    "    result = \"\"\n",
    "    if st.button(\"Bank Marketing Campaign Test Result:\"):\n",
    "        try:\n",
    "            result = bank_function([\n",
    "                float(Age), float(Balance), float(Day), float(Duration),\n",
    "                float(Campaign), float(Pdays), float(Previous),\n",
    "                Job, Marital, Education, Default, Housing, Loan,\n",
    "                contact, Month, poutcome\n",
    "            ])\n",
    "            st.success(result)\n",
    "        except ValueError:\n",
    "            st.error(\"Please enter valid numeric values for the numeric fields.\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
