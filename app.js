const imageInput = document.getElementById("imageInput");
const uploadBox = document.querySelector(".upload-box");
const previewArea = document.querySelector(".preview-area");

const originalImage = document.getElementById("originalImage");
const resultImage = document.getElementById("resultImage");

const loading = document.getElementById("loading");

const removeBackgroundBtn =
    document.getElementById("removeBackgroundBtn");

const backgroundBtn =
    document.getElementById("backgroundBtn");

const downloadBtn =
    document.getElementById("downloadBtn");


let selectedFile = null;
let resultBlob = null;


// ===============================
// اختيار الصورة
// ===============================

imageInput.addEventListener("change", function () {

    if (this.files.length > 0) {
        handleImage(this.files[0]);
    }

});


// ===============================
// Drag & Drop
// ===============================

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


// ===============================
// عرض الصورة
// ===============================

function handleImage(file) {

    if (!file.type.startsWith("image/")) {

        alert("من فضلك اختر صورة صحيحة.");

        return;
    }


    selectedFile = file;

    resultBlob = null;


    const imageURL = URL.createObjectURL(file);

    originalImage.src = imageURL;

    resultImage.removeAttribute("src");


    previewArea.style.display = "block";


    console.log("Image selected:", file.name);

}


// ===============================
// إزالة الخلفية
// ===============================

removeBackgroundBtn.addEventListener(
    "click",
    async function () {

        if (!selectedFile) {

            alert("اختر صورة أولاً.");

            return;
        }


        loading.style.display = "block";

        removeBackgroundBtn.disabled = true;


        try {

            const formData = new FormData();

            formData.append(
                "image",
                selectedFile
            );


            /*
             * عنوان الـ Python Backend
             *
             * أثناء التطوير:
             * http://localhost:5000/process
             *
             * عند رفع الـ Backend على السيرفر:
             * سنغيره إلى رابط السيرفر الحقيقي.
             */

            const response = await fetch(
                "https://superman-spoon-pang.ngrok-free.dev/process",
                {
                    method: "POST",
                    body: formData
                }
            );


            if (!response.ok) {

                let errorMessage =
                    "حدث خطأ أثناء معالجة الصورة.";

                try {

                    const errorData =
                        await response.json();

                    if (errorData.error) {
                        errorMessage = errorData.error;
                    }

                } catch (e) {}

                throw new Error(errorMessage);
            }


            // استلام صورة PNG من Python
            resultBlob = await response.blob();


            const resultURL =
                URL.createObjectURL(resultBlob);


            resultImage.src = resultURL;


        } catch (error) {

            console.error(error);

            alert(
                "تعذر معالجة الصورة:\n" +
                error.message
            );

        } finally {

            loading.style.display = "none";

            removeBackgroundBtn.disabled = false;

        }

    }
);


// ===============================
// تحميل النتيجة
// ===============================

downloadBtn.addEventListener(
    "click",
    function () {

        if (!resultBlob) {

            alert("قم بإزالة الخلفية أولاً.");

            return;
        }


        const downloadURL =
            URL.createObjectURL(resultBlob);


        const link =
            document.createElement("a");


        link.href = downloadURL;

        link.download =
            "imageai-result.png";


        document.body.appendChild(link);

        link.click();

        link.remove();


        URL.revokeObjectURL(downloadURL);

    }
);


// ===============================
// زر إضافة الخلفية
// ===============================

backgroundBtn.addEventListener(
    "click",
    function () {

        if (!resultBlob) {

            alert("قم بإزالة الخلفية أولاً.");

            return;
        }


        alert(
            "ميزة إضافة الخلفية سنبنيها في الخطوة التالية."
        );

    }
);
