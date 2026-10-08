import {
    mkdir,
    readdir,
    stat,
    open
} from "fs/promises";

import {
    createReadStream
} from "fs";

import path from "path";


const uploadDir = path.join(
    process.cwd(),
    "uploads"
);


// =====================================
// GET
// =====================================

export async function GET({ url }) {

    await mkdir(uploadDir, {
        recursive: true
    });


    const download =
        url.searchParams.get("download");


    // =================================
    // DOWNLOAD
    // =================================

    if (download) {

        const filename =
            path.basename(download);

        const filePath =
            path.join(
                uploadDir,
                filename
            );


        try {

            const info =
                await stat(filePath);


            const stream =
                createReadStream(filePath);


            return new Response(
                stream as any,
                {
                    headers: {

                        "Content-Type":
                            "application/octet-stream",

                        "Content-Length":
                            info.size.toString(),

                        "Content-Disposition":
                            `attachment; filename="${filename}"`

                    }
                }
            );


        } catch (error) {

            console.error(error);

            return new Response(
                "Fichier introuvable",
                {
                    status: 404
                }
            );

        }

    }


    // =================================
    // LISTE DES FICHIERS
    // =================================

    try {

        const files =
            await readdir(uploadDir);


        return new Response(

            JSON.stringify({
                files: files
            }),

            {
                status: 200,

                headers: {
                    "Content-Type":
                        "application/json"
                }
            }

        );

    } catch (error) {

        console.error(error);

        return new Response(

            JSON.stringify({
                files: []
            }),

            {
                status: 500,

                headers: {
                    "Content-Type":
                        "application/json"
                }
            }

        );

    }

}


// =====================================
// POST
// =====================================

export async function POST({ request, url }) {

    await mkdir(uploadDir, {
        recursive: true
    });


    const requestedFilename =
        url.searchParams.get("filename");


    if (!requestedFilename) {

        return new Response(

            JSON.stringify({
                status: "error",
                error: "Nom du fichier manquant"
            }),

            {
                status: 400,

                headers: {
                    "Content-Type":
                        "application/json"
                }
            }

        );

    }


    const filename =
        path.basename(
            requestedFilename
        );


    const filePath =
        path.join(
            uploadDir,
            filename
        );


    // =================================
    // Vérifier le body
    // =================================

    if (!request.body) {

        return new Response(

            JSON.stringify({
                status: "error",
                error: "Aucun fichier reçu"
            }),

            {
                status: 400,

                headers: {
                    "Content-Type":
                        "application/json"
                }
            }

        );

    }


    console.log(
        "Upload de :",
        filename
    );


    // =================================
    // Ouvrir le fichier
    // =================================

    const handle =
        await open(
            filePath,
            "w"
        );


    try {

        const reader =
            request.body.getReader();


        while (true) {

            const result =
                await reader.read();


            if (result.done) {
                break;
            }


            await handle.write(
                result.value
            );

        }


        await handle.close();


    } catch (error) {

        console.error(
            "Erreur pendant l'upload :",
            error
        );


        await handle.close();


        return new Response(

            JSON.stringify({
                status: "error",
                error: "Erreur pendant l'upload"
            }),

            {
                status: 500,

                headers: {
                    "Content-Type":
                        "application/json"
                }
            }

        );

    }


    console.log(
        "Upload terminé :",
        filename
    );


    return new Response(

        JSON.stringify({
            status: "success",
            filename: filename
        }),

        {
            status: 200,

            headers: {
                "Content-Type":
                    "application/json"
            }
        }

    );

}