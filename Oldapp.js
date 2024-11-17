// Firebase configuration
const firebaseConfig = {
      apiKey: "AIzaSyDpJ9cb6VdMSV_Lrxy5MrM4S7_3alqm_AE",
      authDomain: "speech-lab-iot.firebaseapp.com",
      databaseURL: "https://speech-lab-iot-default-rtdb.europe-west1.firebasedatabase.app",
      projectId: "speech-lab-iot",
      storageBucket: "speech-lab-iot.firebasestorage.app",
      messagingSenderId: "160784896852",
      appId: "1:160784896852:web:c23b998e2c846491676ec1"
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
