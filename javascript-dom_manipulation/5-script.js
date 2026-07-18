const updateHeader = document.querySelector('#update_header');
updateHeader.onclick = function () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
};
