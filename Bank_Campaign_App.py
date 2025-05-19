{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4de4c725-12aa-421a-8f03-b7af4146a6ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "loaded_model = pickle.load(open(\"Bank_model_trained.pkl\",\"rb\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "18f73ad1-b920-4c1e-b388-880f9f29c8f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-19 17:14:07.769 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Caesar\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-05-19 17:14:07.769 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import streamlit as st\n",
    "\n",
    "loaded_model = pickle.load(open(r\"C:\\Users\\Caesar\\Downloads\\ML Deployment Folder\\Bank_model_trained.pkl\",'rb'))\n",
    "\n",
    "def bank_function(input_data):\n",
    "    \n",
    "\n",
    "# changing the input_data to numpy array\n",
    "    input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "# reshape the array as we are predicting for one instance\n",
    "    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "    prediction = loaded_model.predict(input_data_reshaped)\n",
    "    print(prediction)\n",
    "\n",
    "    if (prediction[0] == 0):\n",
    "        return 'The client will not subscribe to our term deposit'\n",
    "    else:\n",
    "        return 'The client will subscribe to our term deposit'\n",
    "    \n",
    "\n",
    "def main():\n",
    "    st.title(\"Bank Marketing for Term Deposit Prediction Web App\")\n",
    "    \n",
    "    \n",
    "    Age= st.text_input(\"Number of Age: \")\n",
    "    Balance= st.text_input(\"Account  Balance: \")\n",
    "    Day= st.text_input(\"Last Contact Day of the Month: \")\n",
    "    Duration= st.text_input(\"Duration of Last Contact: \")\n",
    "    Campaign= st.text_input(\"Number of Contacts During Campaign: \")\n",
    "    Pdays= st.text_input(\"Days Since Last Contact: \")\n",
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
    "    \n",
    "    result = \"\"\n",
    "    if st.button(\"Bank Marketing Campaign Test Result:\"):\n",
    "        result = bank_function([Age, Balance, Day, Duration, Campaign, Pdays, Previous,\n",
    "                                Job, Marital, Education, Default, Housing, Loan,\n",
    "                                contact, Month, poutcome])\n",
    "    st.success(result)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6c9b2ad-9e10-4a44-8278-0d170a985a53",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d311e2a-d33f-4c6e-8ec3-abac152ab2c2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a803f816-dc65-44dd-897d-22a713ad234f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de1de86a-0450-41c1-b555-4b7c9da54fb0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbc19abd-29b5-43a3-868c-b5e7d9c0a429",
   "metadata": {},
   "outputs": [],
   "source": []
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
