// Get welcome message element
const welcomeMsg = document.getElementById('welcome-message');

// on page load ask for username if it not in local storage
window.addEventListener('load', () => {
	let username = localStorage.getItem('username');
	// Check if username is already in local storage, if yes display it
	if (username != null) {
		// Error handler when routing to a template that does not have this message
		welcomeMsg != null
		? (welcomeMsg.textContent = 'Welcome Back, ' + username + '!')
			: '';
		} else {
			//  If it is not in local storage, ask the user to enter his/her name
		// Using sweet alert to take user input
		Swal.fire({
			title: 'What is your name?',
			input: 'text',
			inputPlaceholder: 'Enter Your Name',
			showCancelButton: true,
			confirmButtonText: 'Save',
			cancelButtonText: 'Cancel',
			allowOutsideClick: false,
			allowEscapeKey: false,
		}).then((result) => {
			// if the result is confirmed and the user enters a value
			// assign the result (input value) to the username variable
			if (result.isConfirmed && result.value) {
				username = result.value.trim();
				// set new username in localstorage
				localStorage.setItem('username', username);
				// display welcome message with the user name
				welcomeMsg != null
					? (welcomeMsg.textContent = 'Welcome Back, ' + username + '!')
					: '';
			} else {
				// if the user did not enter a name, welcome guest message
				welcomeMsg != null ? (welcomeMsg.textContent = 'Welcome, Guest!') : '';
			}
		});
	}
});

// Function to get the current time dynamically
function updateTime() {
	let currentTime = new Date();
	let hours = currentTime.getHours();
	let minutes = currentTime.getMinutes();
	let seconds = currentTime.getSeconds();
	let ampm = hours >= 12 ? 'PM' : 'AM';
	hours = hours % 12;
	hours = hours ? hours : 12;
	minutes = minutes < 10 ? '0' + minutes : minutes;
	seconds = seconds < 10 ? '0' + seconds : seconds;
	let timeString = hours + ':' + minutes + ':' + seconds + ' ' + ampm;
	document.getElementById('current-time').innerHTML = timeString;
}

// Invoke the updateTime function
updateTime();
// Repeat it every second so it counts the time constantly
setInterval(updateTime, 1000);

// Limit the date input fields to the current days of the month we are currently in
const today = new Date();

// Get Last day of the month
const lastDay = new Date(today.getFullYear(), today.getMonth() + 1, 1); // => Date Fri Apr 1 2023 00:00:00 GMT+0200 (Eastern European Standard Time)

// Format the last day to a string so the it could be used as max value for input date field
const maxDate = lastDay.toISOString().slice(0, 10); // 2023-3-31

const firstDay = new Date(today.getFullYear(), today.getMonth(), 1); // Date Wed Mar 01 2023 00:00:00 GMT+0200 (Eastern European Standard Time)

// Format the first day to a string so the it could be used as min value for input date field
const minDate = firstDay.toISOString().slice(0, 10);

// Loop through eaxh date input field and add the max min attributes
document.querySelectorAll("input[type='date']").forEach((input) => {
	input.setAttribute('max', maxDate);
	input.setAttribute('min', minDate);
});
