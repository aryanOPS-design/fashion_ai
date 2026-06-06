const form = document.getElementById("generatorForm");
const statusDiv = document.getElementById("status");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    alert("Starting request...");

    const formData = new FormData(form);

    try {

        const response = await fetch(
            "https://fashion-ai-svkj.onrender.com/generate",
            {
                method: "POST",
                body: formData
            }
        );

        alert("Response received: " + response.status);

    }
    catch(err){

        alert("ERROR: " + err);

    }

});