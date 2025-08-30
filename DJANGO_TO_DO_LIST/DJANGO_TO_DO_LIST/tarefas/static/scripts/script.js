document.addEventListener("DOMContentLoaded", () => {
    const checkboxes = document.querySelectorAll(".checkbox");

    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", () => {
            const tarefaId = checkbox.dataset.id;
            const concluida = checkbox.checked;

            fetch(`/atualizar_status/${tarefaId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: JSON.stringify({ concluida: concluida }),
            })
            .then((response) => response.json())
            .then((data) => {
                if (data.sucesso) {
                    location.reload(); 
                } else {
                    alert("Erro ao atualizar tarefa.");
                }
            });
        });
    });

    // Função para obter o valor de um cookie pelo nome (Mantém o valor original)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
