const burgerBtn = document.querySelector('.burger-btn');
const nav = document.querySelector('.nav');

burgerBtn.addEventListener('click', () => {
  nav.classList.toggle('active'); // Добавляем/убираем класс .active
  
  // Анимация бургер-иконки в "крестик"
  burgerBtn.classList.toggle('active');
});

