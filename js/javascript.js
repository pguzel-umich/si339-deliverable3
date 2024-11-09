document.querySelectorAll('img').forEach(img => {
    console.log("Default image path runs");
    img.onerror = function () {
        this.onerror = null;

        console.log("Path is establishing");

        const defaultImage = new Image();
        defaultImage.src = 'images/default_image.jpg';

        defaultImage.onload = () => {
            this.src = defaultImage.src;
            this.alt = "placeholder image";
            console.log("Default image success");
        };

        defaultImage.onerror = () => {
            this.onerror = null;
            console.log("Rerouting path since no access.");
            this.src = '../images/default_image.jpg';
            this.alt = "placeholder image";
        };
    };
});


document.getElementById("theme-switch").addEventListener("change", function () {
    document.body.className = this.value;
});
