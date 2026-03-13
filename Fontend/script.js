<script>

async function optimizeCode(){

const code = document.getElementById("codeInput").value;
const inputLanguage = document.getElementById("inputLanguage").value;
const outputLanguage = document.getElementById("outputLanguage").value;

if(code.trim() === ""){
alert("Please enter code");
return;
}

document.getElementById("outputCode").innerText = "Algomancer is processing your code...";

try{

const response = await fetch("https://algomancer.onrender.com/optimize",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body: JSON.stringify({
code: code,
input_language: inputLanguage,
output_language: outputLanguage
})

});

const data = await response.json();

document.getElementById("outputCode").innerText = data.optimized_code;

}catch(error){

document.getElementById("outputCode").innerText = "Error connecting to backend";

}

}

function copyCode(){

const code = document.getElementById("outputCode").innerText;

navigator.clipboard.writeText(code);

alert("Code copied!");

}

</script>