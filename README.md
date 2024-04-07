## Step to run Medical Chatbot
- Clone emedicalchatbotllma2 in your local machine
- Download and install Anaconda from https://www.anaconda.com/download
- Type anaconda on windows search and open anaconda command prompt
- Navigate to emedicalchatbotllma2 progect (in step 1) from conda prompt and/by follow below commands
    * cd <basepath>/emedicalchatbotllma2
    * conda create -p env python=3.11 -y
    * pip install -r requirement.txt
- Open StreamlitAPP.py (notepad++ or VS Code) and configure Response.json file path at line number 11 with appropriate value 
- Run mcqgen with below command
    * streamlit run StreamlitAPP.py --server.port 8080
