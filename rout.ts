fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      message: "Congratulations! You've won a free iPhone."
    }),
  })
    .then(res => res.json())  // Expect JSON
    .then(data => console.log("Prediction:", data.result))
    .catch(err => console.error("Error:", err));
  