# Google Speech To Text Python Implementation
This module is implementation of Google Speech To Text API. Google Speech To Text supports multiple languages such as English, Turkish, German while converting speeches into text.

# SETUP
## Setting Up The Google Cloud Platform
NOTE: If you have your JSON credential file for your GCP, skip to the step 17!

### GCP Access
1. Login or Sign in to Google Cloud Platform Console through <a href="https://cloud.google.com/">here</a>

### Creating New Project
2. Create a new project: 
<img width="1394" alt="image" src="https://user-images.githubusercontent.com/28951869/167868246-7ed8f796-ba2e-4ea4-8ba9-df2ce2e3f95d.png">

### Enabling Speech To Text API
3. Navigate to your newly created project:
<img width="1392" alt="image" src="https://user-images.githubusercontent.com/28951869/167869636-31d690d0-92d6-4e5e-b5e6-111e44bf95b5.png">

4. Navigate to APIs & Services:
<img width="1392" alt="image" src="https://user-images.githubusercontent.com/28951869/167869160-ec5d3ac2-ce22-484c-96f4-6fe529b18ba8.png">

5. Click ENABLE APIS AND SERVICES button:
<img width="1388" alt="image" src="https://user-images.githubusercontent.com/28951869/167869866-c1ede81d-a635-4495-9cf6-e750dfa352c8.png">

6. Search for Cloud Speech To Text API and click it:
<img width="1391" alt="image" src="https://user-images.githubusercontent.com/28951869/167870278-e6c783d1-0cd2-40cb-a2c8-22a0976d5ed3.png">

7. Click enable (You need to add payment to enable this service but don't worry Google gives you free credits at the beginning):
<img width="641" alt="image" src="https://user-images.githubusercontent.com/28951869/167870513-07446259-1665-401d-a946-5d3596472376.png">

### Creating a New Service Account and Gathering The JSON file for Authorization
8. Navigate to the IAM & Admin -> Service Accounts:
<img width="1386" alt="image" src="https://user-images.githubusercontent.com/28951869/167871032-cfbdaddd-b9a0-4621-a438-b8ff4d6b289e.png">

9. Click to Create Service Account button:
<img width="947" alt="image" src="https://user-images.githubusercontent.com/28951869/167871377-3cbcd63c-ace8-4f6f-b6a7-3bb3146b1fb3.png">

10. You can give any name you want as service account name. For 2nd step of service account creation, you may give "Owner" role as the image suggests but you can give any desired role of course of this service account:
<img width="865" alt="image" src="https://user-images.githubusercontent.com/28951869/167871814-5bd1cb3f-cb9c-4679-a079-5ff23981bba8.png">

11. For 3rd step, after writing yout service account's name you can clearly see Google suggeste you the mail address that is related to yout newly created service account. You should fill two fields with this email address:
<img width="566" alt="image" src="https://user-images.githubusercontent.com/28951869/167872405-76404b00-2687-44d0-a082-7eef4320ab52.png">

12. Now you can see you service account has been created!

13. Click the 3 dots that is at right corner of your service account and select Manage Keys option:
<img width="1119" alt="image" src="https://user-images.githubusercontent.com/28951869/167872941-1cabd80f-8a07-42f8-ae8a-d3c79a8da6bc.png">

14. Click Add Key -> Create New Key:
<img width="918" alt="image" src="https://user-images.githubusercontent.com/28951869/167873204-3a418705-4241-402b-8406-83d2f53bb48b.png">

15. Select JSON and click Create:
<img width="1021" alt="image" src="https://user-images.githubusercontent.com/28951869/167873471-706f71ee-b070-495b-8f2f-e51d828471d4.png">

16. Your JSON file should be downloaded to your PC. Save it with safe! We will be using this JSON file for Google API Authentication.

### Setting Up GCP Storage

17. Search for Storage from the searchbox and select the Cloud Storage:
<img width="1394" alt="image" src="https://user-images.githubusercontent.com/28951869/167875497-e229c349-8c17-445b-84c0-352bf910548a.png">

18. Create a new bucket:
<img width="1091" alt="image" src="https://user-images.githubusercontent.com/28951869/167875783-69e02628-881f-45ee-aa5b-8d24b3e8fea4.png">

19. Name your bucket (which should be unique worlwide) and click Next for every step until you create a bucket. Now you are in your bucket
<img width="1089" alt="image" src="https://user-images.githubusercontent.com/28951869/167876156-41696e6f-baa1-485a-87e0-07728bc2d32a.png">
This bucket will hold you audio files which will be translated into texts. You may upload you files here.


20. I'm uploading my file name 'uzuntrim.wav' here. My audio file here has the wav extension.


# Demo
21. Clone the repository:
```bash
git clone ...
```

22. Create a new virtual environemnt:
```bash
python3 -m venv myvenv
```

23-1. Activate your virtual environment (FOR MAC):
```bash
source myvenv/bin/activate
```

23-2. Activate your virtual environment (FOR WINDOWS):
```bash
source myvenv/bin/activate
```

NOTE: If you got error like this;
<img width="1352" alt="image" src="https://user-images.githubusercontent.com/28951869/167883817-9d48042c-99cb-4c64-b885-88dfd0ca7c7e.png">
You should do the following:

- Start Windows Powershell as Administrator
- Type ```Set-ExecutionPolicy RemoteSigned``` and hit enter
- When Powershell waits for your input, enter ```A``` and hit Enter button

Now you should be able to move forward with the venv activation script

24. Install all the requirements via the following command:
```bash
pip3 install -r requirements.txt
```
25. Add your JSON file that is being downloaded at step 16 to the main directory of the project.
26. Add .env file to you main directory of the project. This file should contain the name of your JSON file with the key of JSON_NAME.
```
JSON_NAME={name}.json
```
27. In ```main.py``` file, you should change this line:
```python
audio = dict(uri="gs://diarizationuv/uzuntrim.wav")
```
with the corresponding url you've taken from GCP Storage. To achieve this just select your desired audio file from Cloud platform and click to the 3 dots at the right o that line. Then choose ```Copy gsutil URI``` option.
<img width="935" alt="image" src="https://user-images.githubusercontent.com/28951869/167887027-4dfb0b26-a2ce-41f3-9aad-347fa89d17b5.png">

28. If you have a recoırding more than 1 minute, you should use ```speech_to_text_long``` but if you have a recording that is not exceeding 1 minute, you may use ```speech_to_text``` functions in ```main.py``` file.

29. You should set your ```language_code``` parameter in your config dictionary which is in ```main.py``` file according to your audio's language. For example if your audio contains Turkish language, then you should set the language_code parameter as ```tr-TR'```

30. To run the python script, enter the following command:
```bash
python3 main.py
```
31. And you should be able to see the results:
<img width="393" alt="image" src="https://user-images.githubusercontent.com/28951869/167888024-077ef51b-2986-4dc6-ab5a-919e656ada9c.png">

32. CONGRATULATIONS! Now you converted your speech audio into text :)
