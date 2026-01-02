import React, { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import UserForm from "./components/UserForm";
import Question from "./components/Question";
import Results from "./components/Results";
import { UserProvider } from "./UserContext";
import Header from "./components/Header";

export default function App() {
  // Questions Array
  const questions = [
    {
      question: "What's your favorite color?",
      options: ["Red 🔴", "Blue 🔵", "Green 🟢", "Yellow 🟡"],
    },
  ];

  // Keywords
  const keywords = {
    Fire: "fire",
    Water: "water",
    Earth: "earth",
    Air: "air",
  };

  // Element Mapping
  const elements = {
    "Red 🔴": "Fire",
    "Blue 🔵": "Water",
    "Green 🟢": "Earth",
    "Yellow 🟡": "Air",
  };

  // State
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [userName, setUserName] = useState("");
  const [element, setElement] = useState("");
  const [artwork, setArtwork] = useState(null);

  // Handlers
  function handleAnswer(answer) {
    setAnswers([...answers, answer]);
    setCurrentQuestionIndex(currentQuestionIndex + 1);
  }

  function handleUserFormSubmit(name) {
    setUserName(name);
  }

  function determineElement(answers) {
    const counts = {};
    answers.forEach((answer) => {
      const element = elements[answer];
      counts[element] = (counts[element] || 0) + 1;
    });
    return Object.keys(counts).reduce((a, b) =>
      counts[a] > counts[b] ? a : b
    );
  }

  // Fetch MET artwork
  async function fetchArtwork(keyword) {
    try {
      const response = await fetch(
        `https://collectionapi.metmuseum.org/public/collection/v1/search?q=${keyword}`
      );
      const data = await response.json();

      if (!data.objectIDs) {
        setArtwork(null);
        return;
      }

      const firstId = data.objectIDs[0];
      const artRes = await fetch(
        `https://collectionapi.metmuseum.org/public/collection/v1/objects/${firstId}`
      );
      const artData = await artRes.json();

      setArtwork(artData);
    } catch (err) {
      console.error("Error fetching artwork:", err);
    }
  }

  // useEffect for quiz completion
  useEffect(() => {
    if (currentQuestionIndex === questions.length) {
      const selectedElement = determineElement(answers);
      setElement(selectedElement);
      fetchArtwork(keywords[selectedElement]);
    }
  }, [currentQuestionIndex, answers]);

  // RETURN UI
  return (
    <UserProvider value={{ name: userName, setName: setUserName }}>
      <Header />

      <Routes>
        <Route
          path="/"
          element={<UserForm onSubmit={handleUserFormSubmit} />}
        />

        <Route
          path="/quiz"
          element={
            currentQuestionIndex < questions.length ? (
              <Question
                question={questions[currentQuestionIndex].question}
                options={questions[currentQuestionIndex].options}
                onAnswer={handleAnswer}
              />
            ) : (
              <Results element={element} artwork={artwork} />
            )
          }
        />
      </Routes>
    </UserProvider>
  );
}
