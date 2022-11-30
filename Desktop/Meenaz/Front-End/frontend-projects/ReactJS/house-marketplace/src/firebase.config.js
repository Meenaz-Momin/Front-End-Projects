// Import the functions you need from the SDKs you need
import { getFirestore } from "firebase/firestore";
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBnkEufhezAGbntYJehy6zv5ZzEHz8CxyY",
  authDomain: "house-marketplace-app-8f765.firebaseapp.com",
  projectId: "house-marketplace-app-8f765",
  storageBucket: "house-marketplace-app-8f765.appspot.com",
  messagingSenderId: "467311889098",
  appId: "1:467311889098:web:409a94a297c67fda2ac233",
};

// Initialize Firebase
initializeApp(firebaseConfig);
export const db = getFirestore();
