document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("searchForm");
    const input = document.getElementById("searchInput");

    if (form && input) {
        form.addEventListener("submit", function (e) {
            if (input.value.trim() === "") {
                alert("Please enter something to search.");
                e.preventDefault();
            }
        });
    }
});
