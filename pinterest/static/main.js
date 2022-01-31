// show/close board Modal
const createBoardBtn = document.querySelector("#createBoardBtn");
const modal = document.querySelector("#simpleModal");

createBoardBtn.addEventListener("click", (e) => {
  e.preventDefault();
  modal.style.display = "block";

});

window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});


