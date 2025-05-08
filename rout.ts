fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',  // ✅ must be POST, not GET
    body: new URLSearchParams({ message: "your text here" }),
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    }
  })
    .then(res => res.text())  // or .json() if response is JSON
    .then(data => {
      console.log("Result:", data);
    });
  