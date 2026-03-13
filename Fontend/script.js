<script>
async function optimizeCode() {

    const code = document.getElementById("codeInput").value;
    const language = document.getElementById("language").value;

    const response = await fetch("http://127.0.0.1:8000/optimize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            code: code,
            language: language
        })
    });

    const data = await response.json();

    document.getElementById("result").innerText = data.optimized_code;
}
</script>