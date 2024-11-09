document.querySelectorAll('img').forEach(img => {
    console.log("runs")
    img.onerror = function () {
        this.onerror = null;

        console.log("Path is establishing");
        const defaultImage = new Image();
        defaultImage.src = 'images/default_image.jpg';

        defaultImage.onerror = () => {
            console.log("Rerouting path since no access.");
            defaultImage.src = '../images/default_image.jpg';
        };

        this.src = defaultImage.src;
        this.alt = "placeholder image";

        console.log("Default image success");
    };
});

document.getElementById("theme-switch").addEventListener("change", function () {
    document.body.className = this.value;
});
