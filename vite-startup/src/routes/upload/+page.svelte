<script>
    let file = $state(null);
    let uploading = $state(false);
    let message = $state("");

    function selectFile(event) {
        file = event.currentTarget.files[0];
        message = "";
    }

    async function upload() {
        if (!file) {
            message = "Sélectionne un fichier";
            return;
        }

        uploading = true;
        message = "Upload en cours...";

        try {
            const response = await fetch(
                "/api/upload?filename=" +
                encodeURIComponent(file.name),
                {
                    method: "POST",
                    body: file
                }
            );

            const data = await response.json();

            if (response.ok) {
                message = "Upload terminé !";
                console.log(data);
            } else {
                message = "Erreur : " + data.error;
            }

        } catch (error) {
            console.error(error);
            message = "Erreur de connexion au serveur";
        }

        uploading = false;
    }
</script>


<h1>Upload</h1>

<input
    type="file"
    onchange={selectFile}
    disabled={uploading}
/>

{#if file}
    <p>
        Fichier : {file.name}
    </p>

    <p>
        Taille :
        {(file.size / 1024 / 1024).toFixed(2)} MB
    </p>

    <button
        onclick={upload}
        disabled={uploading}
    >
        {uploading ? "Upload..." : "Envoyer"}
    </button>
{/if}

<p>{message}</p>