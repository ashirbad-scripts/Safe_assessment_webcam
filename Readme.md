# Flask Webcam Lockdown Browser

This project is a Flask-based Lockdown Browser that requires users to log in before accessing a webcam feed. Once the webcam is active, pressing any key will terminate the session.



## 📌 Features

✔️ **User Authentication:** Login required before accessing the webcam.

✔️ **Webcam Streaming:** Live video feed using OpenCV.

✔️ **Lockdown Mode:** Pressing any key while the webcam is active will end the session.

✔️ **Screenshot Capture:** Take a snapshot of the webcam feed.

✔️ **Session Termination:** Automatically closes the session upon pressing a key.

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

    git clone https://github.com/your-username/flask-webcam-lockdown.git
    cd flask-webcam-lockdown

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3️⃣ Install Dependencies

    pip install -r flask, opencv-python, pillow, response, request, jsonify

### 4️⃣ Run the Application
    
    python app.py

### 5️⃣ Access the App
    
    Open your browser and go to:

    http://127.0.0.1:5000/

## 📁 Project Structure

#### flask-webcam-lockdown/

**static/**

 ──> script.js 

**templates/**

  ──> index.html  
   ──> login.html  

**app.py**   


**README.md**


## 🔥 How It Works

1️⃣ User logs in using their credentials.

2️⃣ If login is successful, the user is redirected to the webcam page.

3️⃣ Webcam starts streaming, and additional options like screenshot capture appear.

4️⃣ If any key is pressed, the session ends and the browser closes.

## 🛠️ Future Enhancements

Implement database authentication instead of hardcoded users.

Improve UI with additional security features.

Support multiple camera inputs.


Happy coding! 🚀

