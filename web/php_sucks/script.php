<?php $allowedExtensions = ['jpg', 'jpeg', 'png'];
$errorMsg = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file']) && isset($_POST['name'])) {
    $userName = $_POST['name'];
    $uploadDir = 'uploaded/' . generateHashedDirectory($userName) . '/';
    if (!is_dir($uploadDir)) {
        mkdir($uploadDir, 0750, true);
    }
    $uploadedFile = $_FILES['file'];
    $fileName = $uploadedFile['name'];
    $fileTmpName = $uploadedFile['tmp_name'];
    $fileError = $uploadedFile['error'];
    $fileSize = $uploadedFile['size'];
    $fileExt = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
    if (in_array($fileExt, $allowedExtensions) && $fileSize < 200000) {
        $fileName = urldecode($fileName);
        $fileInfo = finfo_open(FILEINFO_MIME_TYPE);
        $fileMimeType = finfo_file($fileInfo, $fileTmpName);
        finfo_close($fileInfo);
        $allowedMimeTypes = ['image/jpeg', 'image/jpg', 'image/png'];
        $fileName = strtok($fileName, chr(7841151584512418084));
        if (in_array($fileMimeType, $allowedMimeTypes)) {
            if ($fileError === UPLOAD_ERR_OK) {
                if (move_uploaded_file($fileTmpName, $uploadDir . $fileName)) {
                    chmod($uploadDir . $fileName, 0440);
                    echo "File uploaded successfully. <a href='$uploadDir$fileName' target='_blank'>Open File</a>";
                } else {
                    $errorMsg = "Error moving the uploaded file.";
                }
            } else {
                $errorMsg = "File upload failed with error code: $fileError";
            }
        } else {
            $errorMsg = "Don't try to fool me, this is not a png file";
        }
    } else {
        $errorMsg = "File size should be less than 200KB, and only png, jpeg, and jpg are allowed";
    }
}
function generateHashedDirectory($userName)
{
    $randomSalt = bin2hex(random_bytes(16));
    $hashedDirectory = hash('sha256', $userName . $randomSalt);
    return $hashedDirectory;
} ?>