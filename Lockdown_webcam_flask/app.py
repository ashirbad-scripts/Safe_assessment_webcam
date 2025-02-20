from flask import Flask, render_template, request, redirect, url_for, session, Response, jsonify
import cv2

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Simulated database with stored Gmail and passwords
USERS = {
    "user1@gmail.com": "123",
    "user2@gmail.com": "password2",
    "user3@gmail.com": "password3",
    "user4@gmail.com": "password4",
    "user5@gmail.com": "password5"
}

# Open webcam
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in USERS and USERS[email] == password:
            session['user'] = email  # Store user session
            return jsonify(success=True)  # Send JSON response for JavaScript to handle fullscreen
        else:
            return jsonify(success=False)  # JSON response for failed login
    return render_template('login.html')

@app.route('/main')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/shutdown')
def shutdown():
    global cap
    cap.release()
    session.pop('user', None)  # Clear session
    return "Webcam closed!", 200

if __name__ == '__main__':
    app.run(debug=True)
