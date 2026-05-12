const formulario = document.getElementById("formulario");

formulario.addEventListener("submit", function(event) {

    event.preventDefault();

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const mensagem = document.getElementById("mensagem").value;

    if(nome === "" || email === "" || mensagem === "") {
        alert("Preencha todos os campos!");
        return;
    }

    alert("Mensagem enviada com sucesso!");

    formulario.reset();
});