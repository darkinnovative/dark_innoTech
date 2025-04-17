
  document.getElementById("contactForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;

    // Show loading indicator
    document.querySelector(".loading").style.display = "block";
    document.querySelector(".error-message").style.display = "none";
    document.querySelector(".sent-message").style.display = "none";

    axios.post("http://127.0.0.1:8001/contact", {
      name: name,
      email: email,
      subject: subject,
      message: message
    })
    .then(function (response) {
      document.querySelector(".loading").style.display = "none";
      document.querySelector(".sent-message").style.display = "block";
    })
    .catch(function (error) {
      document.querySelector(".loading").style.display = "none";
      document.querySelector(".error-message").style.display = "block";
      console.error("Submission error:", error);
    });
  });

