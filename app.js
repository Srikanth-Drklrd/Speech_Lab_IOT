// Firebase configuration
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  databaseURL: "https://YOUR_PROJECT_ID.firebaseio.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const database = firebase.database();

// Authenticate user using Google Sign-In
auth.signInWithPopup(new firebase.auth.GoogleAuthProvider())
  .then((result) => {
    console.log("User signed in:", result.user.email);
    fetchDatabaseContent();
  })
  .catch((error) => {
    console.error("Error signing in:", error);
  });

// Function to fetch and display database content
function fetchDatabaseContent() {
  const dbRef = database.ref('/');  // Adjust path as needed
  dbRef.on('value', (snapshot) => {
    const data = snapshot.val();
    displayData(data);
  });
}

// Function to display data on the page
function displayData(data) {
  const contentDiv = document.getElementById("content");
  contentDiv.innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
}
