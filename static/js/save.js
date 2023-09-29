setInterval(saveProg,5000)

function saveProg(formIds) {

    const inputIds = formIds;

    inputIds.forEach((id) => {
        const inputElement = document.getElementById(id);

        inputElement.addEventListener('input', () => {
            localStorage.setItem(id, inputElement.value);
        });

        const storedValue = localStorage.getItem(id);
        if (storedValue) {
            inputElement.value = storedValue;
        }
    });

    document.getElementById('myForm').addEventListener('submit', () => {
        inputIds.forEach((id) => {
            localStorage.removeItem(id);
        });
    });
}