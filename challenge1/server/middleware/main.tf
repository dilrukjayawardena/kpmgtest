data "archive_file" "middleware_app_zip" {
  type        = "zip"
  source_dir  = "${path.root}/middleware_app/"
  output_path = "${path.root}/middleware_app.zip"
}


resource "google_storage_bucket" "middleware_app_bucket" {
  name     = "middleware_app_bucket"
  location = "US"
}

resource "google_storage_bucket_object" "middleware_app_zip_object" {
  name   = "middleware_app.zip"
  bucket = google_storage_bucket.middleware_app_bucket.name
  source = "${path.root}/middleware_app.zip"
}


resource "google_cloudfunctions_function" "middleware_app_function" {
  name                  = "server-app-function"
  description           = "server app function"
  available_memory_mb   = 512
  source_archive_bucket = google_storage_bucket.middleware_app_bucket.name
  source_archive_object = google_storage_bucket_object.middleware_app_zip_object.name
  timeout               = 60
  entry_point           = "data_store"
  trigger_http          = true
  runtime               = "python39"

}
