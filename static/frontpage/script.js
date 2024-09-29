document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {
            nome: formData.get('nome'),
            email: formData.get('email'),
            mensagem: formData.get('mensagem')
        };

        try {
            const response = await fetch('/api/enviar-contato', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error('Erro ao enviar o formulário');
            }

            const result = await response.json();
            console.log('Sucesso:', result);
        } catch (error) {
            console.error('Erro:', error);
        }
    });
});
