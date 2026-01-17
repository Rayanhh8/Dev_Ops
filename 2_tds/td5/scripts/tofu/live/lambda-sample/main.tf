provider "aws" {
  region = "us-east-2"
}

module "function" {
  source  = "brikis98/devops/book//modules/lambda"
  version = "1.0.0"

  name = var.name

  src_dir = "${path.module}/src"
  runtime = "nodejs20.x"
  handler = "index.handler"

  memory_size = 128
  timeout     = 5

  create_url = true


  environment_variables = {
    NODE_ENV = "production"
  }
}

module "test_endpoint" {
  source = "../../modules/test-endpoint"

  name     = var.name
  endpoint = module.function.function_url
}
