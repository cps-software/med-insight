document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('trackingForm');
  const tableBody = document.getElementById('trackingTableBody');

  form.addEventListener('submit', (event) => {
    event.preventDefault();

    const date = form.date.value;
    const time = form.time.value;
    const username = form.username.value;
    const data = form.data.value;

    const newRow = document.createElement('tr');
    newRow.innerHTML = `
          <td>${date}</td>
          <td>${time}</td>
          <td>${username}</td>
          <td>${data}</td>
      `;
    tableBody.appendChild(newRow);

    form.reset();
  });
});