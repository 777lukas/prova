
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
function comprarProduto(nomeProduto) {
    alert("Você selecionou: " + nomeProduto);
}
function searchPlant() {
    const query = document.getElementById('searchInput').value;
    if (query) {
        window.location.href = 'resultados.html?query=' + encodeURIComponent(query);
    } else {
        alert("Digite algo para pesquisar.");
    }
}

const formCadastro = document.querySelector('form[action="/cadastro"]');
const formLogin = document.querySelector('form[action="/login"]');

if (formCadastro) {
    formCadastro.addEventListener('submit', (e) => {
        const senha = formCadastro.querySelector('input[name="senha"]').value;
        if (senha.length < 6) {
            e.preventDefault();
            alert("A senha deve ter pelo menos 6 caracteres.");
        }
    });
}

if (formLogin) {
    formLogin.addEventListener('submit', (e) => {
        const email = formLogin.querySelector('input[name="email"]').value;
        if (!email.includes("@")) {
            e.preventDefault();
            alert("Por favor, insira um e-mail válido.");
        }
    });
}


const searchInput = document.querySelector('#search');
if (searchInput) {
    searchInput.addEventListener('input', () => {
        const searchTerm = searchInput.value.toLowerCase();
        document.querySelectorAll('.produto').forEach((produto) => {
            const title = produto.querySelector('h3').innerText.toLowerCase();
            produto.style.display = title.includes(searchTerm) ? '' : 'none';
        });
    });
}
// Mostra alerta ao clicar em "Comprar"
function comprarProduto(nomeProduto) {
    alert("Você selecionou: " + nomeProduto);
}

// Pesquisa
function searchPlant() {
    const query = document.getElementById('searchInput').value;
    if (query) {
        alert("Você pesquisou por: " + query);
    } else {
        alert("Digite algo para pesquisar.");
    }
}
function openModal() {
    document.getElementById('modal').style.display = 'block';
}
function closeModal() {
    document.getElementById('modal').style.display = 'none';
}
function enviarSugestao() {
    const nomePlanta = document.getElementById('plantaInput').value;
    if (nomePlanta.trim() !== '') {
        alert("Sugestão enviada: " + nomePlanta);
        closeModal();
    } else {
        alert("Por favor, escreva o nome da planta.");
    }
}
