const leftArrow = document.querySelector('.left-arrow');
const rightArrow = document.querySelector('.right-arrow');
const carImage = document.querySelector('.car-image');

const colorOptions = document.querySelectorAll('.color-option');

let currentIndex = 0;
const carImages = ['car1.jpg', 'car2.jpg', 'car3.jpg'];

leftArrow.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + carImages.length) % carImages.length;
  carImage.src = carImages[currentIndex];
});

rightArrow.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % carImages.length;
  carImage.src = carImages[currentIndex];
});

colorOptions.forEach((option, index) => {
  option.addEventListener('click', () => {
    carImage.src = `car${index + 1}.jpg`;
  });
}); 




  
  