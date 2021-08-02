let u = document.querySelectorAll(".btn");
Array.from(btns).forEach(item => {
   item.addEventListener("click", () => {
      var selected = document.getElementsByClassName("active");
      selected[0].className = selected[0].className.replace(" active", "");
      item.className += " active";
   });
