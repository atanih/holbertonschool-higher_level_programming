const toggleHeader = document.querySelector('#toggle_header');
toggleHeader.onclick = function () {
  const header = document.querySelector('header');
  header.classList.toggle('red');
  header.classList.toggle('green');
};
