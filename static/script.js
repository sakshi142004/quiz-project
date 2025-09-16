// Get all radio options
const options = document.querySelectorAll('input[name="answer"]');
const form = document.querySelector('form');

options.forEach(option => {
  option.addEventListener('change', () => {
    // Highlight selected option
    options.forEach(o => o.parentElement.style.background = '#f9f9f9');
    option.parentElement.style.background = '#d1ffd1';
  });
});

// Optional: Show alert on submit (before POST)
form.addEventListener('submit', (e) => {
  const selected = document.querySelector('input[name="answer"]:checked');
  if (!selected) {
    alert('Please select an answer!');
    e.preventDefault(); // stop form submission
  }
});
