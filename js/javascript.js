// IMAGE PATH TESTER
function setimage_path() {
    document.querySelectorAll('img').forEach(img => {
        console.log("Running: Default image path check");
        img.onerror = function () {
            this.onerror = null;

            console.log("Path is establishing");

            defaultImage = new Image();
            defaultImage.src = 'images/default_image.jpg';

            defaultImage.onload = () => {
                this.src = defaultImage.src;
                console.log("Default image success");
            };

            defaultImage.onerror = () => {
                this.onerror = null;
                console.log("Rerouting path since no access.");
                this.src = '../images/default_image.jpg';
            };

            this.alt = "placeholder image";
        };
    });
};

// COLOR SCHEME SELECTOR

document.getElementById("theme-switch").addEventListener("change", function () {
    document.body.className = this.value;
});

function setColorScheme() {
    lightMode = window.matchMedia('(prefers-color-scheme: light)').matches;
    darkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    highContrast = window.matchMedia('(prefers-contrast: high)').matches;
    lowContrast = window.matchMedia('(prefers-contrast: low)').matches;

    if (lightMode) {
        document.body.className = 'light-mode';
    } else if (darkMode) {
        document.body.className = 'dark-mode';
    } else if (highContrast || lowContrast) {
        document.body.className = 'high-contrast';
    }
};

// SEARCH BAR

function searchBar() {
    searchBar = document.getElementById('search_bar_id');
    results = document.querySelectorAll('.search_result');

    searchBar.addEventListener('input', function () {
        input = searchBar.value.toLowerCase();

        results.forEach(result => {
            if (result.textContent.toLowerCase().includes(input)) {
                result.classList.remove('search_hidden', 'search_fade_out');
            } else {
                result.classList.add('search_fade_out');

                setTimeout(() => {
                    result.classList.add('search_hidden');
                }, 500);
            }
        });
    });
}

setimage_path();
setColorScheme();
searchBar();
