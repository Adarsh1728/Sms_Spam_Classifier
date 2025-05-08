<<<<<<< HEAD
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
=======
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
>>>>>>> 3785f4f76d85cd007e25796e4041549e7c398167
  