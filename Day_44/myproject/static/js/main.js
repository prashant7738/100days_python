// Smooth scroll for navigation links
document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', function (e) {
        if (this.hash !== "") {
            e.preventDefault();
            const hash = this.hash;

            document.querySelector(hash)?.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Back-to-top button
const backToTopButton = document.createElement('button');
backToTopButton.textContent = '↑ Top';
backToTopButton.id = 'back-to-top';
document.body.appendChild(backToTopButton);

// Show or hide back-to-top button based on scroll position
window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
        backToTopButton.style.display = 'block';
    } else {
        backToTopButton.style.display = 'none';
    }
});

// Scroll to top when the button is clicked
backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
