const copyButton = document.getElementById("copyLauncher");
const status = document.getElementById("copyStatus");

async function copyLauncher() {
    status.textContent = "Loading launcher...";

    try {
        const response = await fetch("bookmarklet/bookmarklet.txt", {
            cache: "no-store"
        });

        if (!response.ok) {
            throw new Error("Launcher file could not be loaded.");
        }

        const launcher = (await response.text()).trim();

        if (!launcher.startsWith("javascript:")) {
            throw new Error("Launcher file is invalid.");
        }

        if (navigator.clipboard && window.isSecureContext) {
            await navigator.clipboard.writeText(launcher);
        } else {
            const textarea = document.createElement("textarea");
            textarea.value = launcher;
            textarea.style.position = "fixed";
            textarea.style.opacity = "0";
            document.body.appendChild(textarea);
            textarea.focus();
            textarea.select();
            document.execCommand("copy");
            textarea.remove();
        }

        status.textContent = "Launcher copied. Paste it into the URL field of a new bookmark.";
    } catch (error) {
        status.textContent = error.message || "Could not copy the launcher.";
    }
}

copyButton.addEventListener("click", copyLauncher);
