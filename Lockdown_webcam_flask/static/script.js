document.addEventListener("DOMContentLoaded", function () {
    let loginForm = document.getElementById("login-form");

    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            event.preventDefault();

            let email = document.getElementById("email").value;
            let password = document.getElementById("password").value;

            fetch("/", {
                method: "POST",
                body: new URLSearchParams({ email, password }),
                headers: { "Content-Type": "application/x-www-form-urlencoded" }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = "/main"; // Redirect after login
                } else {
                    alert("Invalid credentials. Try again!");
                }
            });
        });
    }
});

function captureScreenshot() {
    let video = document.querySelector("img");
    let link = document.createElement("a");
    link.href = video.src;
    link.download = "screenshot.jpg";
    link.click();
}

function exitWebcam() {
    fetch("/shutdown").then(response => {
        alert("Webcam session ended.");
        window.close();
    });
}

let webcamActive = false;

function startWebcam() {
    document.getElementById("lockdown-alert").style.display = "none";
    document.getElementById("video-container").style.display = "block";
    document.querySelector(".controls").style.display = "block";
    webcamActive = true; // Mark that webcam is now active
}

document.addEventListener("keydown", function (event) {
    if (webcamActive) {
        exitWebcam();
    }
});