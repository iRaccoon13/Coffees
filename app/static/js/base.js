const body = document.querySelector("body");
body.style.backgroundPosition = '50% 0px';

window.addEventListener("scroll", (e) => {
  let scrolled = window.pageYOffset;
  body.style.backgroundPosition = `50% -${scrolled * 0.5}px`;
});