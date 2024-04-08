## Step to run Medical Chatbot
- Clone emedicalchatbotllma2 in your local machine
- Download and install Anaconda from https://www.anaconda.com/download
- Type anaconda on windows search and open anaconda command prompt
- Navigate to emedicalchatbotllma2 progect (in step 1) from conda prompt and/by follow below commands
    * cd <basepath>/emedicalchatbotllma2
    * conda create -n mchatbot python=3.11 -y
    * conda activate mchatbot
    * pip install -r requirement.txt
    * python setup.py install
- Open app.py (notepad++ or VS Code) and configure port and host (optional) 
- Run Medical-Chatbot with below command
    * python app.py
- By default it will run on http://localhost:8080
