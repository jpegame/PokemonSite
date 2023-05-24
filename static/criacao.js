const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
context.beginPath();
context.rect(0, 0, 700, 700);
context.lineWidth = 5;
context.fillStyle = "white";
context.fill();
let isDrawing = false;
let lastX = 0;
let lastY = 0;


function startDrawing(event) {
    isDrawing = true;
    [lastX, lastY] = [event.offsetX, event.offsetY];
}

function draw(event) {
    if (!isDrawing) return;
    context.beginPath();
    context.moveTo(lastX, lastY);
    context.lineTo(event.offsetX, event.offsetY);
    context.stroke();
    [lastX, lastY] = [event.offsetX, event.offsetY];
}

function stopDrawing() {
    isDrawing = false;
}

function saveDrawing() {
    const dataURL = canvas.toDataURL();
    document.getElementById('imagem').value = dataURL
    //const link = document.createElement('a');
    // link.download = 'drawing.txt';
    // link.href = 'data:text/plain;charset=utf-8,' + encodeURIComponent(dataURL);
    // const base64String = "data:image/png;base64,iVBORw0KG...";
    // const img = new Image();
    // img.src = dataURL;//base64String;
    // document.body.appendChild(img);
    // context.clearRect(0, 0, canvas.width, canvas.height);
    //link.click();
}

canvas.addEventListener('mousedown', startDrawing);
canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', stopDrawing);
canvas.addEventListener('mouseout', stopDrawing);

document.getElementById('submit').addEventListener('click', saveDrawing);