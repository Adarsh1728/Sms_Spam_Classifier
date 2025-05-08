fetch('http://127.0.0.1:5000/predict', {
    method: 'POST', // Must be POST
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      message: "Congratulations! You've won a free iPhone."
    }),
  })
    .then(res => res.text())
    .then(data => console.log(data))
    .catch(err => console.error("Error:", err));
  