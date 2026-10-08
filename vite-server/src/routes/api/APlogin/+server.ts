export async function POST() {

    const response = await fetch("http://localhost:38281", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    });

    const data = await response.json();

    return new Response(JSON.stringify(data), {
        headers: {
            "Content-Type": "application/json"
        }
    });
}