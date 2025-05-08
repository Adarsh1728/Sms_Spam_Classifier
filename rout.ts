fetch('http://localhost:5000/predict', {
    method: 'POST',
    body: new URLSearchParams({ message: "your text here" }),
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    }
  })
    .then(res => res.json())
    .then(data => {
      console.log("Result:", data.result);
    });
  