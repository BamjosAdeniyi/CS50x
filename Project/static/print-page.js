document.getElementById('downloadPdfBtn').addEventListener('click', function () {
    window.print();
});

document.getElementById('downloadPdfBtn').addEventListener('click', async function () {
    // Convert canvas to image
    const charts = document.querySelectorAll('canvas');
    for (const canvas of charts) {
        const imgData = await html2canvas(canvas).then(canvas => canvas.toDataURL());
        const img = document.createElement('img');
        img.src = imgData;
        img.style.maxWidth = '100%';
        img.style.display = 'block';
        canvas.replaceWith(img);
    }
    // Trigger print
    window.print();
});
