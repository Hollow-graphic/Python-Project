import { mkdir, open } from "fs/promises";
import path from "path";

const uploadDir = path.join(
    process.cwd(),
    "uploads"
);

export async function POST({ request, url }) {

    await mkdir(uploadDir, {
        recursive: true
    });

    const filenameParam =
        url.searchParams.get("filename");

    if (!filenameParam) {
        return new Response(
            JSON.stringify({
                error: "Nom du fichier manquant"
            }),
            {
                status: 400,
                headers: {
                    "Content-Type": "application/json"
                }
            }
        );
    }

    // Empêche les chemins du genre ../../fichier
    const filename = path.basename(filenameParam);

    const filePath = path.join(
        uploadDir,
        filename
    );

    if (!request.body) {
        return new Response(
            JSON.stringify({
                error: "Fichier manquant"
            }),
            {
                status: 400,
                headers: {
                    "Content-Type": "application/json"
                }
            }
        );
    }

    const file = await open(filePath, "w");

    try {
        const reader = request.body.getReader();

        while (true) {
            const { done, value } = await reader.read();

            if (done) {
                break;
            }

            await file.write(value);
        }

    } finally {
        await file.close();
    }

    console.log("Upload terminé :", filename);

    return new Response(
        JSON.stringify({
            status: "success",
            filename
        }),
        {
            headers: {
                "Content-Type": "application/json"
            }
        }
    );
}