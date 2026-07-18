const redHeader = document.querySelector('#red_header');
redHeader.onclick = function () {
  const header = document.querySelector('header');
  header.classList.add('red');
};
