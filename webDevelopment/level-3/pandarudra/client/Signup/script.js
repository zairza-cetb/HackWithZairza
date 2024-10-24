// Log a message indicating the signup page is loaded
console.log("Signup page");

// Add an event listener that triggers when the DOM is fully loaded
window.addEventListener("DOMContentLoaded", () => {
  const token = localStorage.getItem("token"); // Retrieve token from local storage
  const id = localStorage.getItem("curid"); // Retrieve current user ID from local storage

  // Check if token and ID exist, redirect to profile page if they do
  if (token && id) {
    console.log(token, id); // Log the token and ID
    window.location.href = `/profile`; // Redirect to profile page
  }

  // Log a message indicating the signup page is active
  console.log("Signup page ip");
});

// Initialize Notyf notification library for user notifications
var notyFy = new Notyf();

// Define the signup function to handle form submission
const signup = async (e) => {
  e.preventDefault(); // Prevent the default form submission behavior

  try {
    // Retrieve input values from the signup form
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Send a POST request to the server for user registration
    await fetch("http://localhost:3000/register", {
      method: "POST", // Set the request method to POST
      headers: {
        "Content-Type": "application/json", // Set content type to JSON
      },
      body: JSON.stringify({ name, email, password }), // Send user data in the request body
    }).then((res) => {
      // Check the response status
      if (res.status === 200) {
        // Retrieve existing users from local storage or initialize an empty array
        let users = JSON.parse(localStorage.getItem("users")) || [];

        // Check if a user with the same email already exists
        const user = users.find((user) => user.email === email);
        if (user) {
          notyFy.error("User already exists"); // Notify that the user already exists
          return; // Exit the function
        }

        // Add the new user to the users array
        users.push({
          name,
          email,
          password,
          tasks: [], // Initialize tasks as an empty array
          id: crypto.randomUUID(), // Generate a unique ID for the user
        });

        // Save the updated users array back to local storage
        localStorage.setItem("users", JSON.stringify(users));
        notyFy.success("Signup successful"); // Notify that signup was successful

        // Redirect to login page after a short delay
        setTimeout(() => {
          window.location.href = "/login";
        }, 3000);
      } else {
        notyFy.error("Signup failed"); // Notify that signup failed
      }
    });
  } catch (error) {
    console.log(error); // Log any errors that occur during signup
  }
};

// Add an event listener to the signup form to trigger the signup function on submit
document.getElementById("signupform").addEventListener("submit", signup);
