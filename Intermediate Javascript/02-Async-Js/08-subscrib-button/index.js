const subscribeBtn = document.getElementById("subscribeBtn");
const message = document.getElementById("message");

subscribeBtn.addEventListener("click",() => {
  message.classList.remove("hidden")
  subscribeBtn.innerText = "Subscribed"

  setTimeout(() => {
    message.classList.add("hidden")
  }, 3000);
});