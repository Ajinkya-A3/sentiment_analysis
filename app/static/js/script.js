document.getElementById('reviewForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get the review text
    const reviewText = document.getElementById('review').value;

    // Send the review to the server using fetch
    fetch('/predict', {
        method: 'POST',
        body: new URLSearchParams({
            'review': reviewText
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Display prediction result
        const resultDiv = document.getElementById('predictionResult');
        resultDiv.innerHTML = `<h3>Prediction: ${data.sentiment}</h3>`;

        // Optionally, clear the form
        document.getElementById('review').value = '';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
