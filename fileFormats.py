image_formats = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".raw", ".ico", ".psd"}
video_formats = (".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mpg", ".mpeg")
compressedFile_formats = (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz")
executables_formats = (".exe", ".msi")

file_types = {
    'Images': tuple(image_formats),
    'Videos': tuple(video_formats),
    'Compressed Files': tuple(compressedFile_formats),
    'Executable Files': tuple(executables_formats),
}

