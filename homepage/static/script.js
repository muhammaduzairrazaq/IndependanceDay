document.addEventListener("DOMContentLoaded", function () {
    const h1Element = document.getElementById("ans");
    const colors = ["red", "green", "blue", "orange"]; // Add more colors if needed
    let colorIndex = 0;

    function changeColor() {
        h1Element.style.transition = "color 0.5s"; // Define the transition effect
        h1Element.style.color = colors[colorIndex];
        colorIndex = (colorIndex + 1) % colors.length;
    }

    setInterval(changeColor, 1000); // Change color every second (1000 milliseconds)
});
