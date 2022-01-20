// show/close board Modal
const createBoardBtn = document.querySelector("#createBoardBtn");
const modal = document.querySelector("#simpleModal");

createBoardBtn.addEventListener("click", openModal);
window.addEventListener("click", clickOutside);

function openModal() {
  modal.style.display = "block";
}

function clickOutside(e) {
  if (e.target === modal) {
    modal.style.display = "none";
  }
}

// send board name to /boards/<board_name>
document.querySelector('#form').addEventListener('submit', (e) => {
  e.preventDefault();
  var boardName = document.querySelector('#board-name-input').value;
  window.location.pathname = '/boards/' + boardName + '/';
})


