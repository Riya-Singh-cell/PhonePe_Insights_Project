function fetchTransactions() {
  fetch("http://127.0.0.1:8000/aggregated/transactions")
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById("transaction-data");
      container.innerHTML = "<pre>" + JSON.stringify(data.slice(0, 5), null, 2) + "</pre>";
    })
    .catch(error => console.error("Error:", error));
}
