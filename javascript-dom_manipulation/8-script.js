function displayHello() {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      const hello = document.querySelector('#hello');
      hello.textContent = data.hello;
    });
}

document.addEventListener('DOMContentLoaded', displayHello);
