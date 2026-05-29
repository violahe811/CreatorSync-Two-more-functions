document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("campaign-search");

    if (!searchInput) return;

    searchInput.addEventListener("keyup", function () {

        const value = searchInput.value.toLowerCase();

        const cards = document.querySelectorAll(".campaign-card");

        cards.forEach(card => {

            const title = card.dataset.title;
            const description = card.dataset.description;

            if (
                title.includes(value) ||
                description.includes(value)
            ) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }

        });

    });

});