const imageInput = document.getElementById("imageInput");
const uploadBox = document.querySelector(".upload-box");
const previewArea = document.querySelector(".preview-area");
const originalImage = document.getElementById("originalImage");

let selectedFile = null;

// اختيار صورة
imageInput.addEventListener("change", function () {
    if (this.files.length > 0) {
        handleImage(this.files[0]);
    }
});

// Drag & Drop
uploadBox.addEventListener("dragover", function (e) {
    e.preventDefault();
    uploadBox.classList.add("dragging");
});

uploadBox.addEventListener("dragleave", function () {
    uploadBox.classList.remove("dragging");
});

uploadBox.addEventListener("drop", function (e) {
    e.preventDefault();
    uploadBox.classList.remove("dragging");

    const file = e.dataTransfer.files[0];

    if (file && file.type.startsWith("image/")) {
        handleImage(file);
    }
});

// معالجة الصورة
function handleImage(file) {

    if (!file.type.startsWith("image/")) {
        alert("من فضلك اختر صورة صحيحة.");
        return;
    }

    selectedFile = file;

    const imageURL = URL.createObjectURL(file);

    originalImage.src = imageURL;

    previewArea.style.display = "block";

    console.log("Image selected:", file.name);
}
