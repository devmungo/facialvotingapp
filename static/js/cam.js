
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('capture-btn');
const imageInput = document.getElementById('image-input');
const uploadForm = document.getElementById('upload-form');
const constraints = {
	video: true
};

navigator.mediaDevices.getUserMedia(constraints)
	.then(function (mediaStream) {
		video.srcObject = mediaStream;
	})
	.catch(function (error) {
		console.log('Unable to access camera: ', error);
	});

captureBtn.addEventListener('click', function () {
	canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
	const image = canvas.toDataURL('image/png');
	imageInput.value = image.replace('data:image/png;base64,', '');
	uploadForm.submit();
});
