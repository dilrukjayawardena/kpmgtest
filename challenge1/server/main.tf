
module "db" {
  source = "./db"
  project_id = var.project_id
  location = var.db_location
}

module "server" {
  source = "./middleware"
  location = var.server_location
}