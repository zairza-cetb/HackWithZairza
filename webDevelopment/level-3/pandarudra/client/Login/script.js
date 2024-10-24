// Log a message indicating the login page is loaded
console.log("Hello from Login Page");

// Add an event listener that triggers when the DOM is fully loaded
window.addEventListener("DOMContentLoaded", () => {
  // Check if a token exists in local storage
  if (localStorage.getItem("token")) {
    const token = localStorage.getItem("token"); // Retrieve the token
    const id = localStorage.getItem("curid"); // Retrieve the current user ID
    console.log(token, id); // Log the token and ID
    window.location.href = `/profile`; // Redirect to profile page if already logged in
  }
});

// Initialize Notyf notification library for user notifications
var notify = new Notyf();

// Define the login function to handle form submission
const login = async (e) => {
  e.preventDefault(); // Prevent the default form submission behavior

  try {
    // Retrieve input values from the login form
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const db = JSON.parse(localStorage.getItem("users")); // Get users from local storage

    // Send a POST request to the server for user authentication
    await fetch("http://localhost:3000/signin", {
      method: "POST", // Set the request method to POST
      headers: {
        "Content-Type": "application/json", // Set content type to JSON
      },
      body: JSON.stringify({ email, password, db }), // Send email, password, and users database in the request body
    })
      .then((res) => res.json()) // Parse the response as JSON
      .then((data) => {
        // Check for an error in the response
        if (data.error) {
          notify.error(data.error); // Notify the user about the error
        } else {
          notify.success(data.message); // Notify that login was successful
          // Save token and user ID in local storage
          localStorage.setItem("token", data.token);
          localStorage.setItem("curid", data.id);

          // Redirect to the profile page after login
          window.location.href = `/profile`;
        }
      });
  } catch (error) {
    console.error("Error: ", error); // Log any errors that occur during login
  }
};

// Add an event listener to the login form to trigger the login function on submit
document.getElementById("loginform").addEventListener("submit", login);
