const addItem = document.querySelector('#add_item');
addItem.onclick = function () {
  const list = document.querySelector('.my_list');
  const item = document.createElement('li');
  item.textContent = 'Item';
  list.appendChild(item);
};
