document.querySelectorAll('img').forEach(img => {
    console.log("runs")
    img.onerror = function () {
        this.onerror = null;
        this.src = '../images/default_image.jpg'
        this.alt = "placeholder image"
    };
});

document.getElementById("theme-switch").addEventListener("change", function () {
    document.body.className = this.value;
});
